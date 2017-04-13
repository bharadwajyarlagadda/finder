# -*- coding: utf-8 -*-

import os


def is_executable(path):
    """Validates whether a given file path is binary or not.

    Args:
        path (str): File path.

    Returns:
        bool: True if the file is a binary else False.

    .. versionadded:: TODO
    """
    return os.access(path, os.X_OK)

