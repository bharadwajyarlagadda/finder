# -*- coding: utf-8 -*-

import os
import queue
import threading
import time

from .schema import FinderSchema, DataSchema, ErrorSchema
from .utils import search, iterfiles


class FileReader(threading.Thread):
    """Thread class for finding the given pattern in a given file.

    Args:
        path (str): File path.
        pattern (str): A string to be searched in the given file path.

    .. versionadded:: 1.0.0
    """
    def __init__(self, path=None, pattern=None, _queue=None):
        self.path = path
        self.pattern = pattern
        self._queue = _queue
        threading.Thread.__init__(self)

    def run(self):
        """Runs methods for reading the file and searching the pattern in a
        line of text from the file.
        """
        items = []
        error = []
        pattern_found = False
        errors_occurred = False

        try:
            for line_number, line in read(self.path):
                if search(line, self.pattern):
                    items.append(self.set_data(line_number, line))
                    pattern_found = True
        except PermissionError as exc:
            error.append(self.make_error(type='PermissionError',
                                         message=exc,
                                         extra=None))
            errors_occurred = True
        except OSError as exc:
            error.append(self.make_error(type='OSError',
                                         message=exc,
                                         extra='File might be a kernel file'))
            errors_occurred = True
        except UnicodeDecodeError as exc:
            # TODO: Support all the file encodings.
            error.append(self.make_error(type='UnicodeDecodeError',
                                         message=exc,
                                         extra=None))
            errors_occurred = True

        if pattern_found or errors_occurred:
            # Serialize to a JSON-encoded string.
            response = FinderSchema().dumps({'path': self.path,
                                             'total_items': len(items),
                                             'items': items,
                                             'error': error})

            self._queue.put(response.data)

    def set_data(self, line_number, line):
        """Returns the serialized data."""
        data = {'line_number': line_number,
                'line': line}

        return DataSchema().dump(data).data

    def make_error(self, type, message, extra):
        """Returns the error serialized data."""
        error = {'type': type,
                 'message': message,
                 'extra': extra}

        return ErrorSchema().dump(error).data


def find(*paths, **kwargs):
    """Main method for finding the pattern in the given file paths.

    Args:
        paths (list): List of paths to be walked through.
        kwargs (str): Positional arguments.

    .. versionadded:: 1.0.0

    .. versionchanged:: TODO
        Add time.sleep() call to reduce CPU utilization percentage.
    """
    pattern = kwargs.get('pattern', None)
    _queue = queue.Queue()

    for path in iterfiles(*paths):
        reader = FileReader(path, pattern, _queue)
        reader.start()
        reader.join()

        # Sleep call reduces the CPU utilization percentage. If CPU
        # performance is not a concern, this line can be commented out.
        time.sleep(0.03)

        while not _queue.empty():
            yield _queue.get()


def read(path):
    """Yields line by line from the file path provided.

    Args:
        path (str): File path provided.

    Yields:
        int: Line number.
        str: Line of text corresponding to the line number from the file.

    .. versionadded:: 1.0.0
    """
    with open(path, 'r', encoding='utf-8') as fp:
        count = 0

        for line in fp:
            count += 1
            yield (count, line.strip('\n'))
