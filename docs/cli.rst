Command Line
============

::

    $ finder --help
      Command line interface for searching a given pattern/text in the given
      directory/file path.

      Options:
        -v, --version  Finder tool version.
        --help         Show this message and exit.

      Commands:
        search  Searches for the given pattern in the...


Checkout finder tool's version

::

    $ finder --version
    1.0.2


Sub-command ``search`` helps in searching the pattern in a given path

::

    $ finder search --help
      Searches for the given pattern in the directory/file path provided.

    Options:
      --path path1[,path2,...,pathN]  Searches for the pattern in the
                                      directory/file path provided. If a
                                      directory/file path is not provided, the
                                      tool searches for the pattern in the current
                                      working directory.
      -P, --pattern, --text <pattern>
                                      Text to be searched.  [required]
      -v, --verbose                   Some files cannot be opened and searched for
                                      the given pattern. For example, kernel files
                                      which generate content on go, files which
                                      are not utf-8 encoded, etc. You can use this
                                      flag if you need a detailed output of which
                                      file has an error.
      --help                          Show this message and exit.


Search for a pattern in a given file path

::

    $ finder search --path='~/finder/setup.py' --pattern='port'
    /home/aj/Projects/finder/setup.py:4: import os
    /home/aj/Projects/finder/setup.py:5: from setuptools import setup, find_packages


Search for a pattern in given directory path

::

    $ finder search --path='~/finder' --pattern='port'
    /home/aj/Projects/finder/.gitignore:37: # Unit test / coverage reports
    /home/aj/Projects/finder/LICENSE.rst:16: copies or substantial portions of the Software.
    /home/aj/Projects/finder/setup.cfg:2: addopts = --doctest-modules -v -s --color=yes --cov-config=setup.cfg --cov-report=term-missing
    /home/aj/Projects/finder/setup.py:4: import os
    ...


Check the error occurred only if there is an error occurred while searching the file

::

    $ finder search --path='~/finder' --pattern='port' --verbose
    /home/aj/Projects/finder/.gitignore:37: # Unit test / coverage reports
    /home/aj/Projects/finder/LICENSE.rst:16: copies or substantial portions of the Software.
    /home/aj/Projects/finder/setup.cfg:2: addopts = --doctest-modules -v -s --color=yes --cov-config=setup.cfg --cov-report=term-missing
    /home/aj/Projects/finder/setup.py:4: import os
    ...
    ...
    UnicodeDecodeError:/home/aj/Projects/finder/tests/__pycache__/test_find.cpython-35-PYTEST.pyc:'utf-8' codec can't decode byte 0xf5 in position 5: invalid start byte None
    UnicodeDecodeError:/home/aj/Projects/finder/tests/__pycache__/test_cli.cpython-35-PYTEST.pyc:'utf-8' codec can't decode byte 0xf5 in position 5: invalid start byte
    ...

