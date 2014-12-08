
def test_it(my_test_fixture):
    print my_test_fixture


# We'll have the error below if we go to the tests folder (i.e.: pack/tests) and run pytest full/path/to/pack/tests/test_fixture.py

# INTERNALERROR>   File "C:\Shared\dist\12.0-all\pytest-2.6.4\lib\site-packages\_pytest\main.py", line 84, in wrap_session
# INTERNALERROR>     doit(config, session)
# INTERNALERROR>   File "C:\Shared\dist\12.0-all\pytest-2.6.4\lib\site-packages\_pytest\main.py", line 121, in _main
# INTERNALERROR>     config.hook.pytest_collection(session=session)
# INTERNALERROR>   File "C:\Shared\dist\12.0-all\pytest-2.6.4\lib\site-packages\_pytest\core.py", line 413, in __call__
# INTERNALERROR>     return self._docall(methods, kwargs)
# INTERNALERROR>   File "C:\Shared\dist\12.0-all\pytest-2.6.4\lib\site-packages\_pytest\core.py", line 424, in _docall
# INTERNALERROR>     res = mc.execute()
# INTERNALERROR>   File "C:\Shared\dist\12.0-all\pytest-2.6.4\lib\site-packages\_pytest\core.py", line 315, in execute
# INTERNALERROR>     res = method(**kwargs)
# INTERNALERROR>   File "C:\Shared\dist\12.0-all\pytest-2.6.4\lib\site-packages\_pytest\main.py", line 125, in pytest_collection
# INTERNALERROR>     return session.perform_collect()
# INTERNALERROR>   File "C:\Shared\dist\12.0-all\pytest-2.6.4\lib\site-packages\_pytest\main.py", line 546, in perform_collect
# INTERNALERROR>     items = self._perform_collect(args, genitems)
# INTERNALERROR>   File "C:\Shared\dist\12.0-all\pytest-2.6.4\lib\site-packages\_pytest\main.py", line 566, in _perform_collect
# INTERNALERROR>     rep = collect_one_node(self)
# INTERNALERROR>   File "C:\Shared\dist\12.0-all\pytest-2.6.4\lib\site-packages\_pytest\runner.py", line 400, in collect_one_node
# INTERNALERROR>     ihook.pytest_collectstart(collector=collector)
# INTERNALERROR>   File "C:\Shared\dist\12.0-all\pytest-2.6.4\lib\site-packages\_pytest\main.py", line 166, in call_matching_hooks
# INTERNALERROR>     plugins = self.config._getmatchingplugins(self.fspath)
# INTERNALERROR>   File "C:\Shared\dist\12.0-all\pytest-2.6.4\lib\site-packages\_pytest\config.py", line 688, in _getmatchingplugins
# INTERNALERROR>     plugins += self._conftest.getconftestmodules(fspath)
# INTERNALERROR>   File "C:\Shared\dist\12.0-all\pytest-2.6.4\lib\site-packages\_pytest\config.py", line 521, in getconftestmodules
# INTERNALERROR>     mod = self.importconftest(conftestpath)
# INTERNALERROR>   File "C:\Shared\dist\12.0-all\pytest-2.6.4\lib\site-packages\_pytest\config.py", line 554, in importconftest
# INTERNALERROR>     self._onimport(mod)
# INTERNALERROR>   File "C:\Shared\dist\12.0-all\pytest-2.6.4\lib\site-packages\_pytest\config.py", line 674, in _onimportconftest
# INTERNALERROR>     self.pluginmanager.consider_conftest(conftestmodule)
# INTERNALERROR>   File "C:\Shared\dist\12.0-all\pytest-2.6.4\lib\site-packages\_pytest\core.py", line 201, in consider_conftest
# INTERNALERROR>     if self.register(conftestmodule, name=conftestmodule.__file__):
# INTERNALERROR>   File "C:\Shared\dist\12.0-all\pytest-2.6.4\lib\site-packages\_pytest\core.py", line 95, in register
# INTERNALERROR>     name, plugin, self._name2plugin))
# INTERNALERROR> ValueError: Plugin already registered: x:\workspace1\check_pytest\pack\conftest.pyc=<module 'pack.conftest' from 'x:\workspace1\check_pytest\pack\conftest.pyc'>
# INTERNALERROR> {'helpconfig': <module '_pytest.helpconfig' from 'C:\Shared\dist\12.0-all\pytest-2.6.4\lib\site-packages\_pytest\helpconfig.pyc'>, 'pytestconfig': <_pytest.config.Config object at 0x028C1A10>, '42733904': <_pytest.config.PytestPluginManager object at 0x028C1150>, 'unittest': <module '_pytest.unittest' from 'C:\Shared\dist\12.0-all\pytest-2.6.4\lib\site-packages\_pytest\unittest.pyc'>, 'pytest-mock': <module 'pytest_mock' from 'C:\Shared\dist\12.0-all\pytest_mock-0.2.0\lib\site-packages\pytest_mock.pyc'>, 'xdist': <module 'xdist.plugin' from 'C:\Shared\dist\12.0-all\pytest_xdist-1.10\lib\site-packages\xdist\plugin.pyc'>, 'pastebin': <module '_pytest.pastebin' from 'C:\Shared\dist\12.0-all\pytest-2.6.4\lib\site-packages\_pytest\pastebin.pyc'>, 'skipping': <module '_pytest.skipping' from 'C:\Shared\dist\12.0-all\pytest-2.6.4\lib\site-packages\_pytest\skipping.pyc'>, 'genscript': <module '_pytest.genscript' from 'C:\Shared\dist\12.0-all\pytest-2.6.4\lib\site-packages\_pytest\genscript.pyc'>, 'session': <Session 'tests'>, 'tmpdir': <module '_pytest.tmpdir' from 'C:\Shared\dist\12.0-all\pytest-2.6.4\lib\site-packages\_pytest\tmpdir.pyc'>, 'capture': <module '_pytest.capture' from 'C:\Shared\dist\12.0-all\pytest-2.6.4\lib\site-packages\_pytest\capture.pyc'>, 'terminalreporter': <_pytest.terminal.TerminalReporter instance at 0x034FCEE0>, 'assertion': <module '_pytest.assertion' from 'C:\Shared\dist\12.0-all\pytest-2.6.4\lib\site-packages\_pytest\assertion\__init__.pyc'>, 'mark': <module '_pytest.mark' from 'C:\Shared\dist\12.0-all\pytest-2.6.4\lib\site-packages\_pytest\mark.pyc'>, 'terminal': <module '_pytest.terminal' from 'C:\Shared\dist\12.0-all\pytest-2.6.4\lib\site-packages\_pytest\terminal.pyc'>, 'runner': <module '_pytest.runner' from 'C:\Shared\dist\12.0-all\pytest-2.6.4\lib\site-packages\_pytest\runner.pyc'>, 'main': <module '_pytest.main' from 'C:\Shared\dist\12.0-all\pytest-2.6.4\lib\site-packages\_pytest\main.pyc'>, 'nose': <module '_pytest.nose' from 'C:\Shared\dist\12.0-all\pytest-2.6.4\lib\site-packages\_pytest\nose.pyc'>, 'python': <module '_pytest.python' from 'C:\Shared\dist\12.0-all\pytest-2.6.4\lib\site-packages\_pytest\python.pyc'>, 'recwarn': <module '_pytest.recwarn' from 'C:\Shared\dist\12.0-all\pytest-2.6.4\lib\site-packages\_pytest\recwarn.pyc'>, 'funcmanage': <_pytest.python.FixtureManager instance at 0x034E3210>, 'localserver': <module 'pytest_localserver.plugin' from 'C:\Shared\dist\12.0-all\pytest_localserver-0.3\lib\site-packages\pytest_localserver\plugin.pyc'>, 'monkeypatch': <module '_pytest.monkeypatch' from 'C:\Shared\dist\12.0-all\pytest-2.6.4\lib\site-packages\_pytest\monkeypatch.pyc'>, 'resultlog': <module '_pytest.resultlog' from 'C:\Shared\dist\12.0-all\pytest-2.6.4\lib\site-packages\_pytest\resultlog.pyc'>, 'pydev_runfiles_pytest2': <module 'pydev_runfiles_pytest2' from 'X:\workspace_liclipse\Pydev\plugins\org.python.pydev\pysrc\pydev_runfiles_pytest2.pyc'>, 'cov': <module 'pytest_cov' from 'C:\Shared\dist\12.0-all\pytest_cov-1.8\lib\site-packages\pytest_cov.pyc'>, 'capturemanager': <_pytest.capture.CaptureManager instance at 0x034D35D0>, 'x:\\workspace1\\check_pytest\\pack\\conftest.pyc': <module 'pack.conftest' from 'x:\workspace1\check_pytest\pack\conftest.pyc'>, 'junitxml': <module '_pytest.junitxml' from 'C:\Shared\dist\12.0-all\pytest-2.6.4\lib\site-packages\_pytest\junitxml.pyc'>, 'doctest': <module '_pytest.doctest' from 'C:\Shared\dist\12.0-all\pytest-2.6.4\lib\site-packages\_pytest\doctest.pyc'>, 'timeout': <module 'pytest_timeout' from 'C:\Shared\dist\12.0-all\pytest_timeout-0.3\lib\site-packages\pytest_timeout.pyc'>, 'pdb': <module '_pytest.pdb' from 'C:\Shared\dist\12.0-all\pytest-2.6.4\lib\site-packages\_pytest\pdb.pyc'>}


# And if we don't add the full path and run test_fixture.py from the tests dir (i.e.: go to pack/tests) the fixture is not found and we get:

# =================================== ERRORS ====================================
# __________________________ ERROR at setup of test_it __________________________
# file X:\workspace1\check_pytest\pack\tests\test_fixtures.py, line 2
#   def test_it(my_test_fixture):
#         fixture 'my_test_fixture' not found
#         available fixtures: pytestconfig, smtpserver, cov, recwarn, httpsserver, httpserver, monkeypatch, mock, capfd, capsys, tmpdir
#         use 'py.test --fixtures [testpath]' for help on them.
#
# X:\workspace1\check_pytest\pack\tests\test_fixtures.py:2
# =========================== 1 error in 0.01 seconds ===========================

