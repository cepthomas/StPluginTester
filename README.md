# Sublime Text Plugin Unit Tester

- Uses Visual Studio 2022 to develop Sublime Text plugins. My preferred tool for python dev.
- Uses python unittest + mocks to debug plugins using VS.
- Tests can also be executed from the command line or using unittest test runners.
- This should also be useful for debugging non-ST python applications.

Built for ST4 on Windows. May work on Linux also.

## Background

It's fairly painful and laborious to debug ST plugins, usually ending up relying on copious print() statements.
There are three aspects that need to be juggled here:

- ST has its own internal implementation of python 3.8 to support plugins. It does not handle packages and modules
  the same as standard python. This means you can't just import your plugin into an external instance of python
  and expect it to work. Also the plugin code and the test code both expect to see the ST API interface somewhere.
- A standard python 3.8+ install is required to support the unittest framework used herein.
- VS has its own way of handling PYTHONPATH that is a bit puzzling.  

## Implementation

Bearing in mind the limitations described above, after much wrestling here is the directory/file structure of a tester for a plugin
application (Notr) being developed.

```
C:\Users\<user>\AppData\Roaming\Sublime Text\Packages
|
+---StPluginTester
|   |   StPluginTester.pyproj
|   |   StPluginTester.sln
|   |   sublime.py
|   |   sublime_plugin.py
|   |   test_notr.py
|   |   run_test.cmd (+ run_test.py)
|   |
|   \---files
|           ...as needed
|
\---Notr
    |   notr.py
    |   *.sublime-*
    |   etcetera
    |
    \---files
            ...as needed
```

- It would seem that the easiest path is to keep the plugin and tester directories at the same level. This may
  not actually be true and warrants another investigation at some point.
- `StPluginTester.pyproj/sln` are the standard VS project files.
- `sublime.py` and `sublime_plugin.py` are emulation modules for the ST API.
- `test_xxx.py` is the actual test code.
- `xxx.py` is the actual code under test.

## Sublime API Emulation
The emulation modules implement a simple subset of the ST API. The intent is to minimize the amount of mocking
required. This includes things like loading settings, creating Views and rudimentary management by Window.
Also basic text buffer management by View: insert, find, replace, etc. The more complex functions are not
supported and expected to be emulated using mocks.

General categories:
- function fully implemented.
- function partially implemented - unused args will throw `NotImplementedError`.
- function defined in emulated API but not implemented - will throw `NotImplementedError`.
- function not defined in emulated API - lint-time or run-time error.



## Other Things to Consider

It's probably best to do this:
```
Sublime settings:
    "ignored_packages":
    [
        "StPluginTester",
    ]
```

Put something like this in StPluginTester.pyproj:
```
<Environment>PYTHONPATH=$(APPDATA)\Sublime Text\Packages</Environment>
```

Note that both VS and python module loading insert the current path in sys.path. This is needed so that the code under test can "see"
the ST eulation modules.

In e.g. test_notr.py:

```
from Notr import notr
```

## Python Package And Module Management

**This "management" is a huge PIA. Clearly designed without consideration of the future
and now severely crufty (as is all of python). The lua model is much cleaner and easier to use. /rant**

> ST doesn't load modules like plain python and can cause some surprises. The problem is that sbot_common
> gets reloaded but it appears to be a different module from the one linked to by the other modules.

This makes handling globals interesting.

> To use functions defined in ex.py you either need to import them directly:
>
```
from ex import function_name()
from ex import *
```
> Or refer to the function as a part of ex:
>
```
import ex
ex.function_name()
```
