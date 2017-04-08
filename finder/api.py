# -*- coding: utf-8 -*-

import os
import threading
import logging as log


log.basicConfig(format='%(message)s', level=log.INFO)


class FileReader(threading.Thread):
    """Thread class for finding the given pattern in a given file.

    Args:
        path (str): File path.
        pattern (str): A string to be searched in the given file path.

    .. versionadded:: TODO
    """
    def __init__(self, path=None, pattern=None):
        self.path = path
        self.pattern = pattern
        threading.Thread.__init__(self)

    def run(self):
        """Runs methods for reading the file and searching the pattern in a
        line of text from the file.
        """
        for line_number, line in read(self.path):
            if search(line, self.pattern):
                log.info('{path}:{line_number}: {line}'
                         .format(path=self.path,
                                 line_number=line_number,
                                 line=line))


def find(paths, pattern=None):
    """Main method for finding the pattern in the given file paths.

    Args:
        paths (list): List of paths to be walked through.
        pattern (str): A string to be searched in the given file path.

    .. versionadded:: TODO
    """
    for path in iterfiles(paths):
        reader = FileReader(path, pattern)
        reader.start()


def search(text=None, pattern=None):
    """Searches the given pattern in the given text.

    Args:
        text (str): Text in which the pattern needs to be searched.
        pattern (str): A string to be searched in the given `text`.

    Returns:
        bool: A boolean value stating whether the pattern is found in the
            given text or not.

    .. versionadded:: TODO
    """
    return True if pattern in text else False


def read(path):
    """Yields line by line from the file path provided.

    Args:
        path (str): File path provided.

    Yields:
        int: Line number.
        str: Line of text corresponding to the line number from the file.

    .. versionadded:: TODO
    """
    with open(path, 'r') as fp:
        count = 0

        for line in fp:
            count += 1
            yield (count, line.strip('\n'))


def iterfiles(*paths):
    """Yields all the file paths in a given directory.

    Args:
        paths (list): List of paths to be walked through.

    Yields:
        path (str): File path (files in the given directory path).

    .. versionadded:: TODO
    """
    for path in paths:
        path = os.path.expanduser(path) if not os.path.isabs(path) else path

        if os.path.isfile(path) and not is_executable(path):
            yield path
        elif os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                for file in files:
                    file_path = os.path.join(root, file)

                    if (os.path.isfile(file_path) and
                            not is_executable(file_path)):
                        yield file_path


def is_executable(path):
    """Validates whether a given file path is binary or not.

    Args:
        path (str): File path to be provided.

    Returns:
        bool: Boolean value to tell whether the given file is a binary or not.

    .. versionadded:: TODO
    """
    return os.access(path, os.X_OK)
