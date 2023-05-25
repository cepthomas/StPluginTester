# Sublime Text Plugin Unit Tester

Uses unittest + mocks to debug Sublime Text plugins. This is not an easy thing to do and requires
some finesse in organizing the source and test projects. Documentation is spotty and somewhat
ambiguous. Also complicated by the fact that goal is to support both standard command line
unittest running and a Visual Studio hosted environment for plugin development (intellisense)
and debug. This latter support should be helpful also for debugging non-ST python applications.

There's a sparsely populated sublime api emulation in st_emul. To be used in conjunction with mocks.
It can grow as needed.

Also several suites for the plugins next door to this repository.


## General Notes

**Who invented the abomination of python package and module management?**

> ST doesn't load modules like plain python and can cause some surprises. The problem is that sbot_common
> gets reloaded but it appears to be a different module from the one linked to by the other modules.
> This makes handling globals difficult.


> Or perhaps you don't actually want to run moduleX, you just want to run some other script, say myfile.py, that uses functions
> inside moduleX. If that is the case, put myfile.py somewhere else – not inside the package directory – and run it.
> If inside myfile.py you do things like from package.moduleA import spam, it will work fine.


## Implementation

Has to (TODO?) be at same level as Packages being tested.

```
StPluginTester
|   run_test.cmd
|   run_test.py
|   StPluginTester.pyproj
|   StPluginTester.sln
|   sublime.py
|   sublime_plugin.py
|   test_format.py
|   test_logger.py
|   test_notr.py
|   
\---files
        ...
```


Do this:
```
Sublime settings:
    "ignored_packages":
    [
        "StPluginTester",
    ]
```

In StPluginTester.pyproj:
```
    <Environment>UNIT_TEST=1;
PYTHONPATH=$(APPDATA)\Sublime Text\Packages;$(APPDATA)\Sublime Text\Packages\StPluginTester
    </Environment>
```
- UNIT_TEST=1 is not really needed - VS wizard sticks it in there.
- PYTHONPATH StPluginTester so code-under-test can see sublime/sublime_api

In e.g. test_notr.py:

`from ..Notr import notr`

TODO This supports VS intellisense but doesn't run in VS or cli.

`from Notr import notr`

Vice versa. Run/break/view vars works though.


In creating plugins care must be taken to separate controller from view. A small amount of architectural consideration will go
  a long way to keep mock madness to a minimum.
