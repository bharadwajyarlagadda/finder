******
finder
******

|version| |travis| |coveralls| |license|

Command Line Interface tool which helps in finding a given text/pattern in a given folder/file path(s).

Links
=====

Project: https://github.com/bharadwajyarlagadda/finder
Documentation: Wiki_
Pypi: https://pypi.python.org/pypi/finder
TravisCI: https://travis-ci.org/bharadwajyarlagadda/finder

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


What does the API do?
=====================

1. The main entry point for our API is the ``api.find()`` method. You can pass in both file/directory paths and the pattern to be searched for.
2. If you provide a directory path, it will go ahead and do a ``os.walk`` and brings out all the files in that directory path.
3. While searching for the pattern,
    * It avoids all the non-readable files:
        * Audio files.
        * Video files.
        * Image files.
        * Some of the kernel based files such as the files under ``/proc`` in ``Ubuntu/Linux.``
    * It reads the file line by line so that we can avoid saving the whole file in the memory (which of course will be memory issue for huge files).
4. This whole process runs concurrently. As in, the API allots thread for each file to be searched and once the search is complete, the thread comes and joins back in the main process.
5. I personally have tested the performance and the memory usage is very low. If you face any of the performance issues, please report it at Issues_.
6. The data from the API looks is explained under ``Schema`` section. The output fields are also explained in the same section.
7. The output data is a JSON-encoded string and it is generated only when ``finder`` finds tha pattern in a given file.


Schema
======

::

    {
        "api_version": "<api_version>",
        "requested_on": "<datetime>",
        "path": "<file_path>",
        "total_items": "<total_items>",
        "items": [
            {"line_number": "<line_number>",
             "line": "<line>"},
            {"line_number": "<line_number>",
             "line": "<line>"},
            ...
        ],
        "error": [
            {"type": "<error_type>",
             "message": "<error_message>",
             "extra": "<extra_message>"}
        ]
    }


Data fields:

    - ``api_version``: Finder tool's version
    - ``requested_on``: Datetime value (when the tool was requested)
    - ``path``: File path
    - ``total_items``: Total items returned.
    - ``items``: All the data items returned from the finder tool. The items comprise of:
        * ``line_number``: Line number at which the pattern was found.
        * ``line``: Actual line in which the pattern was found.
    - ``error``: Errors from the finder tool if any.
        * ``type``: Error type (Ex. PermissionError, OSError, etc.)
        * ``message``: Error message from the finder tool.
        * ``extra``: Any extra error message from the finder tool.


Example

::

    {
        "api_version": "1.0.0",
        "requested_on": "2017-04-14T04:17:41.204588",
        "path": "/home/aj/Projects/finder/api.py",
        "total_items": "7",
        "items": [
            {"line_number": "3",
             "line": "import os"},
            {"line_number": "4",
             "line": "import queue"},
            ...
        ]
        "error": []
    }


When there are errors while searching the file,

::

    {
        "api_version": "1.0.0",
        "requested_on": "2017-04-14T04:17:41.204588",
        "path": "/etc/init.d/apache2",
        "total_items": "0",
        "items": []
        "error": [
            {"type": "PermissionError",
             "message": "...",
             "extra": "..."}
        ]
    }


.. |version| image:: https://img.shields.io/pypi/v/finder.svg?style=flat-square
    :target: https://pypi.python.org/pypi/finder/

.. |travis| image:: https://img.shields.io/travis/bharadwajyarlagadda/finder/master.svg?style=flat-square
    :target: https://travis-ci.org/bharadwajyarlagadda/finder

.. |coveralls| image:: https://img.shields.io/coveralls/bharadwajyarlagadda/finder/master.svg?style=flat-square
    :target: https://coveralls.io/r/bharadwajyarlagadda/finder

.. |license| image:: https://img.shields.io/pypi/l/finder.svg?style=flat-square
    :target: https://github.com/bharadwajyarlagadda/finder/blob/master/LICENSE.rst


.. _Wiki: https://github.com/bharadwajyarlagadda/finder/wiki
.. _Issues: https://github.com/bharadwajyarlagadda/finder/issues