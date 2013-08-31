django-discover-runner-test
===========================

Test for Issue #14

There are two test files in tests/appA
* model_test.py
* model_test_broken.py

They are the same except that model_test_broken has an ImportError.

Install
=======
* pip install -r requirements.pip

What I'm seeing
===============
If I run

    ./manage.py test
    ./manage.py test tests
    ./manage.py test tests.appA
    
I see, as expected:
    
    Creating test database for alias 'default'...
    .E
    ======================================================================
    ERROR: tests.appA.test_model_broken (unittest.loader.ModuleImportFailure)
    ----------------------------------------------------------------------
    ImportError: Failed to import test module: tests.appA.test_model_broken
    Traceback (most recent call last):
      File "/usr/lib/python2.7/unittest/loader.py", line 252, in _find_tests
        module = self._get_module_from_name(name)
      File "/usr/lib/python2.7/unittest/loader.py", line 230, in _get_module_from_name
        __import__(name)
      File "/home/bird/Dev/birdsarah/django-discover-runner-test/tests/appA/test_model_broken.py", line 2, in <module>
        from appA import Poll
    ImportError: cannot import name Poll
    
    
    ----------------------------------------------------------------------
    Ran 2 tests in 0.001s

However, when I specify the module name I start to run into trouble, the working test runs fine:

    ./manage.py test tests.appA.test_model      

    Creating test database for alias 'default'...
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.001s
  
But the broken test, instead of producing the ImportError, as above, gives an AttributeError:
  
    ./manage.py test tests.appA.test_model_broken
    
    AttributeError: 'module' object has no attribute 'test_model_broken'
