Schema
======

API output schema

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


