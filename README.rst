******
finder
******

|version| |travis| |coveralls| |license|

Command Line Interface tool which helps in finding a given text/pattern in a given folder/file path(s).

Links
=====

- Project: https://github.com/bharadwajyarlagadda/finder
- Documentation: http://finder.readthedocs.io
- Pypi: https://pypi.python.org/pypi/finder
- TravisCI: https://travis-ci.org/bharadwajyarlagadda/finder

Quickstart
==========

Install using pip:

::

    pip install finder


Features
========

- Finds given text/pattern in the given file path(s).
- Iterates through all the non-executable files in a given directory path.
- Avoids all the non-readable files in a given directory path.
- Supported on Python 3.3+.


Command Line
============

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


.. |version| image:: https://img.shields.io/pypi/v/finder.svg?style=flat-square
    :target: https://pypi.python.org/pypi/finder/

.. |travis| image:: https://img.shields.io/travis/bharadwajyarlagadda/finder/master.svg?style=flat-square
    :target: https://travis-ci.org/bharadwajyarlagadda/finder

.. |coveralls| image:: https://img.shields.io/coveralls/bharadwajyarlagadda/finder/master.svg?style=flat-square
    :target: https://coveralls.io/r/bharadwajyarlagadda/finder

.. |license| image:: https://img.shields.io/pypi/l/finder.svg?style=flat-square
    :target: https://github.com/bharadwajyarlagadda/finder/blob/master/LICENSE.rst


.. _Issues: https://github.com/bharadwajyarlagadda/finder/issues