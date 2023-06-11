import os
import sys
import json


#---------------- Added items to support emulation and debug --------------------------
# Added stuff has underscore _name.

_settings = None
_clipboard = ''
_window = None
_view_id = 0


def _etrace(*args):
    s = ' | '.join(map(str, args))
    print(f'EMU {s}')

def _next_view_id():
    _view_id += 1
    return _view_id


#---------------- sublime.definitions --------------------------

TRANSIENT = 4
IGNORECASE = 2
LITERAL = 1


#---------------- sublime.functions() --------------------------

def version():
    return '4143'

def packages_path():
    return os.path.expandvars('$APPDATA\\Sublime Text\\Packages')

def executable_path():
    raise NotImplementedError()

def installed_packages_path():
    raise NotImplementedError()

def status_message(msg):
    _etrace(f'status_message():{msg}')

def error_message(msg):
    _etrace(f'error_message():{msg}')

def message_dialog(msg):
    _etrace(f'message_dialog():{msg}')

def ok_cancel_dialog(msg, ok_title=""):
    _etrace(f'ok_cancel_dialog():{msg}')
    return True

def run_command(cmd, args=None):
    # Run the named ApplicationCommand.
    raise NotImplementedError()

def set_clipboard(text):
    _clipboard = text

def get_clipboard():
    return _clipboard

def load_settings(base_name):
    global _settings
    _settings = json.loads(base_name)
    return _settings

def set_timeout(f, timeout_ms=0):
    # Schedules a function to be called in the future. Sublime Text will block while the function is running.
    f()

def active_window():
    global _window
    return _window


#---------------- sublime.View --------------------------

class View():

    def __init__(self, view_id):
        self._view_id = view_id
        self._window = Window(-1)
        self._file_name = None
        self._buffer = ''
        self._selection = Selection(view_id)
        self._scratch = False
        self._regions = []
        self._syntax = None

    def __len__(self):
        return len(self._buffer)

    def __eq__(self, other):
        return isinstance(other, View) and other._view_id == self._view_id

    def __bool__(self):
        return self._view_id != 0

    def id(self):
        return self._view_id

    def window(self):
        return self._window

    def file_name(self):
        return self._file_name

    def is_loading(self):
        return False

    def close(self):
        _etrace(f'View.close()')
        return True

    def is_scratch(self):
        return self._scratch

    def set_scratch(self, scratch):
        self._scratch = scratch

    def size(self):
        return len(self._buffer)

    def syntax(self):
        return self._syntax

    def settings(self):
        global _settings
        return _settings

    def show_popup(self, content, flags=0, location=-1, max_width=320, max_height=240, on_navigate=None, on_hide=None):
        _etrace(f'View.show_popup():{content}')
        raise NotImplementedError()

    def run_command(self, cmd, args=None):
        # Run the named TextCommand 
        # run_command("goto_line", {"line": line})
        pass # TODO2

    def sel(self):
        return self._selection

    def set_status(self, key, value):
        _etrace(f'set_status(): key:{key} value:{value}')


    ##### translation between row/col and index

    def rowcol(self, point):
        self._validate(point)
        row = 0
        col = 0
        for ind in range(point):
            col += 1
            if self._buffer[ind] = '\n':
                row += 1
                col = 0
        return (row, col)

    def text_point(self, row, col):
        # Calculates the character offset of the given, 0-based, row and col
        point = 0
        row_i = 0
        col_i = 0
        found = False

        for ind in range(len(self._buffer)):
            if row_i == row and col_i == col:
                found = True
                break
            else: # bump
                point += 1
                col_i += 1
                if self._buffer[ind] = '\n':
                    row_i += 1
                    col_i = 0

        return point if found else -1

    ##### string ops

    def insert(self, edit, point, text):
        self._validate(point)
        self._buffer = self._buffer[:pos] + text + self._buffer[pos:]

    def replace(self, edit, region, text):
        self._validate(region)
        self._buffer = self._buffer[:region.a] + text + self._buffer[region.b:]

    def split_by_newlines(self, region):
        self._validate(region)
        #split_by_newlines(region: Region) ret: list[Region]  Splits the region up such that each Region returned exists on exactly one line.
        return [region] # TODO2

    ##### find/replace        

    def find(self, pattern, start_pt, flags=0):
        self._validate(start_pt)
        # find(pattern: str, start_pt: Point, flags=FindFlags.NONE) ret: Region
        # pattern: The regex or literal pattern to search by.
        # start_pt: The Point to start searching from.
        # flags: Controls various behaviors of find. See FindFlags.
        return None # Region TODO2

    def find_all(self, pattern, flags=0, fmt=None, extractions=None):
        return [] # [Region] TODO2

    def substr(self, x):
        # The string at the Point or within the Region provided.
        self._validate(x)
        if isinstance(x, Region):
            return self._buffer[x.a:x.b]
        else: # Point
            return self._buffer[x]

    def _find_word(self, start_pt, end_pt):
        # Find space/nl/start before
        # Find space/nl/end after
        # find(pattern: str, start_pt: Point, flags=FindFlags.NONE) ret: Region
        return Region() # TODO1

    def _find_line(self, start_pt, end_pt, incl_line_end):
        # Find nl/start before
        # Find nl/end after
        # find(pattern: str, start_pt: Point, flags=FindFlags.NONE) ret: Region
        return Region() # TODO1

    def word(self, x):
        # The word Region that contains the Point. If a Region is provided its beginning/end are expanded to word boundaries.
        self._validate(x)
        if isinstance(x, Region):
            return self._find_word(x.a, x.b)
        else: # Point
            return self._find_word(x, x)

    def line(self, x):
        # Returns The line Region that contains the Point or an expanded Region to the beginning/end of lines, excluding the newline character.
        self._validate(x)
        if isinstance(x, Region):
            return self._find_line(x.a, x.b, False)
        else: # Point
            return self._find_line(x, x, False)

    def full_line(self, x):
        # full_line(x: Region | Point) ret: Region The line that contains the Point or an expanded Region to the beginning/end of lines, including the newline character.
        self._validate(x)
        if isinstance(x, Region):
            return self._find_line(x.a, x.b, True)
        else: # Point
            return self._find_line(x, x, True)

    ##### scopes and regions

    def scope_name(self, point):
        self._validate(point)
        return 'TODO3'

    def style_for_scope(self, scope):
        return 'TODO3'

    def add_regions(self, key, regions, scope="", icon="", flags=0):
        self._regions.extend(regions) # TODO2 key

    def get_regions(self, key):
        return self._regions # TODO2 key

    def erase_regions(self, key):
        pass # TODO2 key

    ##### helpers

    def _validate(self, x):
        if isinstance(x, Region):
            if x.a >= len(self._buffer) or if x.b >= len(self._buffer) or if x.a < 0 or if x.b < 0:
                raise ValueError()
        else: # Point
            if x >= len(self._buffer):
                raise ValueError()


#---------------- sublime.Window --------------------------

class Window():
    def __init__(self, id):
        self._id = id
        self._settings = None
        self._views = []
        self._active_view = -1 # index into _views
        self._project_data = None

    def id(self):
        return self._id

    def active_view(self):
        if self._active_view >= 0:
            return self._views[self._active_view]
        else:
            return None

    def show_input_panel(self, caption, initial_text, on_done, on_change, on_cancel):
        _etrace(f'Window.show_input_panel(): {caption}')
        raise NotImplementedError()

    def show_quick_panel(self, items, on_select, flags=0, selected_index=-1, on_highlight=None):
        _etrace(f'Window.show_quick_panel(): {items}')
        raise NotImplementedError()

    def project_file_name(self):
        return 'StPluginTester.sublime-project'

    def settings(self):
        global _settings
        return _settings

    def run_command(self, cmd, args=None):
        # Run the named WindowCommand with the (optional) given args. TODO3
        # This method is able to run any sort of command, dispatching the command via input focus.
        # run_command("goto_line", {"line": line})
        raise NotImplementedError()

    def new_file(self, flags=0, syntax=""):
        view = View(_next_view_id())
        return view

    def open_file(self, fname, flags=0, group=-1):
        view = View(_next_view_id())
        with open(fname, 'r') as file:
            view.insert(None, 0, file.read())
        return view

    def find_open_file(self, fname):
        for v in self._views:
            if v.file_name == fname:
                return v
        return None

    def focus_view(self, view):
        for i in range(len(self._views)):
            if self.views[i].id() == view.id():
                self._active_view = i
                break;

    def get_view_index(self, view):
        for i in range(len(self._views)):
            if self.views[i].id() == view.id():
                return i

    def views(self):
        return self._views

    def layout(self):
        raise NotImplementedError()

    def set_project_data(self, v):
        self._project_data = v

    def project_data(self):
        return self._project_data


#---------------- sublime.Edit --------------------------

class Edit:
    def __init__(self, token):
        self.edit_token = token

    def __repr__(self):
        return f'Edit({self.edit_token!r})'


#---------------- sublime.Region --------------------------

class Region():
    def __init__(self, a, b=None, xpos=-1):
        if b is None:
            b = a
        self.a = a
        self.b = b
        self.xpos = xpos

     def __str__(self):
         return "(" + str(self.a) + ", " + str(self.b) + ")"

     def __repr__(self):
         return "(" + str(self.a) + ", " + str(self.b) + ")"

    def __len__(self):
        return self.size()

     def __eq__(self, rhs):
         return isinstance(rhs, Region) and self.a == rhs.a and self.b == rhs.b

     def __lt__(self, rhs):
         lhs_begin = self.begin()
         rhs_begin = rhs.begin()

         if lhs_begin == rhs_begin:
             return self.end() < rhs.end()
         else:
             return lhs_begin < rhs_begin

    def empty(self):
        return self.a == self.b

    def begin(self):
        if self.a < self.b:
            return self.a
        else:
            return self.b

    def end(self):
        if self.a < self.b:
            return self.b
        else:
            return self.a

    def size(self):
        return abs(self.a - self.b)

    def contains(self, x):
        if isinstance(x, Region):
            return self.contains(x.a) and self.contains(x.b)
        else:
            return x >= self.begin() and x <= self.end()

    def cover(self, rhs):
        a = min(self.begin(), rhs.begin())
        b = max(self.end(), rhs.end())
        if self.a < self.b:
            return Region(a, b)
        else:
            return Region(b, a)

    def intersection(self, rhs):
        if self.end() <= rhs.begin():
            return Region(0)
        if self.begin() >= rhs.end():
            return Region(0)
        return Region(max(self.begin(), rhs.begin()), min(self.end(), rhs.end()))

    def intersects(self, rhs):
        lb = self.begin()
        le = self.end()
        rb = rhs.begin()
        re = rhs.end()
        return (
            (lb == rb and le == re) or
            (rb > lb and rb < le) or (re > lb and re < le) or
            (lb > rb and lb < re) or (le > rb and le < re))


#---------------- sublime.Selection --------------------------

class Selection():

    def __init__(self, view_id):
        self.view_id = view_id
        self.regions = []

    def __len__(self):
        return len(self.regions)

    def __getitem__(self, index):
        if index >= 0  and index < len(self.regions):
            return self.regions[index]
        else:
            raise IndexError()

    def __delitem__(self, index):
        if index >= 0  and index < len(self.regions):
            self.regions.remove(index)
        else:
            raise IndexError()

    def __eq__(self, rhs):
       return rhs is not None and list(self) == list(rhs)

    def __lt__(self, rhs):
       return rhs is not None and list(self) < list(rhs)

    def __bool__(self):
       return self.view_id != 0

    def is_valid(self):
        return self.view_id != 0

    def clear(self):
        self.regions.clear()

    def add(self, x):
        if isinstance(x, Region):
            self.regions.append(Region(x.a, x.b, x.xpos))
        else:
            self.regions.append(Region(x, x, x))

    def contains(self, region):
        for r in self.regions:
            if r.contains(region):
                return True
        return False

    def add_all(self, regions):
        for r in regions:
            self.add(r)

    def subtract(self, region):
        raise NotImplementedError()


#---------------- sublime.Settings --------------------------

class Settings():  #TODO2

    def __init__(self, view_id):
        self.settings_id = view_id
        self.settings_storage = {}

    def get(self, key, default=None):
        return self.settings_storage.get(key, default)

    def has(self, key):
        return key in self.settings_storage

    def set(self, key, value):
        self.settings_storage[key] = value


#---------------- sublime.Syntax --------------------------

class Syntax():  #TODO3

    def __init__(self, path, name, hidden, scope):
        self.path = path
        self.name = name
        self.hidden = hidden
        self.scope = scope

    def name(self):
       return self.name
