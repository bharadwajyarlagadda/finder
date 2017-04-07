# -*- coding: utf-8 -*-
# Module used in searching the given pattern in the text provided.

import os


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


def iterfiles(*paths):
    """Yields all the file paths in a given directory.

    Args:
        paths (list): List of paths to be walked through.

    Yields:
        path (str): File path (files in the given directory path).

    .. versionadded:: TODO
    """
    for path in paths:
        if os.path.isfile(path) and not is_executable(path):
            yield path
        elif os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                for file in files:
                    yield os.path.join(root, file)


def is_executable(path):
    """Validates whether a given file path is binary or not.

    Args:
        path (str): File path to be provided.

    Returns:
        bool: Boolean value to tell whether the given file is a binary or not.

    .. versionadded:: TODO
    """
    return os.path.isfile(path) and os.access(path, os.X_OK)
