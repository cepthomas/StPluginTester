# Sublime Text Plugin Unit Tester

The primary focus is to debug logic and algorithms defined in the various EventListener, TextCommand, WindowCommand
application-specific derived classes.

- Uses Visual Studio 2022 to develop Sublime Text plugins.
- Uses python unittest + mock to debug plugins using VS.
- Tests can also be executed from the command line or using unittest test runners.
- This should also be useful for debugging non-ST python applications.

Built for ST4 on Windows. May be useful on Linux also.

## Background

It's fairly painful and laborious to debug ST plugins, usually ending up relying on copious print() statements.
There are three aspects that need to be juggled here:
- ST has its own internal implementation of python 3.8 to support plugins. It does not handle packages and modules
  the same as standard python. This means you can't just import your plugin into an external instance of python
  and expect it to work. Also the plugin code and the test code both expect to see the ST API interface somewhere.
- A standard python 3.8+ install is required to support the unittest framework used herein.
- VS has its own way of handling PYTHONPATH that is a bit puzzling.  

## Implementation

Bearing in mind the limitations described above, after much wrestling here is an example directory/file structure of a
tester for a typical plugin application being developed.

```
StPluginTester
|   StPluginTester.pyproj - VS file
|   StPluginTester.sln - VS file
|   run_test.cmd - run from cl
|   sublime.py - ST emulation
|   sublime_plugin.py - ST emulation
|   test_myplugin.py - test-code
|   ... other source and test files
|
\---files - test files as needed

$APPDATA\Sublime Text\Packages\MyPlugin
    myplugin.py - code-under-test
    Context.sublime-menu
    MyPlugin.sublime-settings
    ... other source and config files
```

Since this project is performing a specific function (debugging my plugins) it is hard-coded to support them.
If you want your own flavor you would replace the code-under-test and test-code with your own flavors and
modify the `.pyproj` file - it's recommended to edit it manually rather than in VS.

## Sublime API Emulation
The emulation modules implement a simple subset of the `sublime.py` and `sublime_plugin.py` API. The intent is to minimize
the amount of mocking required. This includes things like loading settings, creating Views and rudimentary management by Window.
Also basic text buffer management by View: insert, find, replace, etc. The more complex functions are not
supported and expected to be emulated using mocks.

General categories:
- function fully implemented.
- function partially implemented - unused args will throw `NotImplementedError`.
- function defined in emulated API but not implemented - will throw `NotImplementedError`.
- function not defined in emulated API - lint-time or run-time error.

Note that `sublime_api` generally returns garbage if you try to access outside of the view buffer area.
The client needs to protect themselves. This does not emulate bad behavior - it will throw `ValueError` to help
track them down.

## Other Things to Consider

VS issue with intellisense for imported modules: https://github.com/microsoft/PTVS/issues/6713.
Sometimes it can be made to go away by closing, editing search path in `.pyproj` and reopening.

VS has isues with python exception processing:
> So the problem is that the checkboxes in the Exceptions tool window correspond to "on throw" exception filters
> (i.e. raise as soon as exception happens), but the debugger actually has two other categories: "on unhandled"
> (when it escapes out of the top-level code) and "on user-unhandled" (when it escapes from library code to your code).
> And by default, VS enables the latter for all Python exceptions, hence why it's breaking.
>
> It used to be that the Exceptions window had a mode that showed multiple checkboxes allowing to tweak this stuff,
> but it doesn't look like that's there anymore. We need to investigate and figure out how the filters work with the new UX.

_This kind of implies that you shouldn't raise exceptions for normal error processing, only to catch lib/sys thrown._

Note that both VS and python module loading insert the current path in sys.path. This is needed so that the code under test can "see"
the ST eulation modules.

In general, python package/module management is cryptic, crufty and a PIA to work with.
In addition, ST has its own built-in version so that ST doesn't load modules like plain python and can cause some surprises.
The problem is that e.g. sbot_common gets reloaded but it is a physically different module from the one linked to by the other modules.
This makes handling globals interesting.

> To use functions defined in package\moodule.py you need to import them directly:
>
```
from package import module

module.function()
```