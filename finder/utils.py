# -*- coding: utf-8 -*-

import os
import logging as log

from .extensions import (
    IMAGE_FORMATS,
    VIDEO_FORMATS,
    AUDIO_FORMATS,
    KERNEL_DIRS
)


log.basicConfig(format='%(message)s', level=log.INFO)


def file_extension(path):
    """Returns the file extension of the given file path.

    .. versionadded:: 1.0.0
    """
    return path.split(os.path.sep)[-1].split('.')[-1]


def is_audio(path):
    """Validates whether a given file path is a audio or not.

    Args:
        path (str): File path.

    Returns:
        bool: True if the file is a audio else False.

    .. versionadded:: 1.0.0
    """
    extension = file_extension(path)

    return extension in AUDIO_FORMATS


def is_executable(path):
    """Validates whether a given file path is binary or not.

    Args:
        path (str): File path.

    Returns:
        bool: True if the file is a binary else False.

    .. versionadded:: 1.0.0
    """
    return os.access(path, os.X_OK)


def is_image(path):
    """Validates whether a given file path is image or not.

    Args:
        path (str): File path.

    Returns:
        bool: True if the file is an image else False.

    .. versionadded:: 1.0.0
    """
    extension = file_extension(path)

    return extension in IMAGE_FORMATS


def is_kernel_file(path):
    """Validates whether the file path is a kernel file or not.

    Args:
        path (str): File path.

    Returns:
        bool: True if the file path is a kernel file else False.

    .. versionadded:: 1.0.0
    """
    return any([path.startswith(parent_dir) for parent_dir in KERNEL_DIRS])


def is_readable(path):
    """Validates whether a given file path is readable or not.

    Args:
        path (str): File path.

    Returns:
        bool: True if the file is readable else False.

    .. versionadded:: 1.0.0
    """
    return os.access(path, os.R_OK)


def is_video(path):
    """Validates whether a given file path is a video or not.

    Args:
        path (str): File path.

    Returns:
        bool: True if the file is a video else False.

    .. versionadded:: 1.0.0
    """
    extension = file_extension(path)

    return extension in VIDEO_FORMATS


def iterfiles(*paths):
    """Yields all the non-executable file paths in a given directory.

    Args:
        paths (list): List of paths to be walked through.

    Yields:
        path (str): File path (files in the given directory path).

    .. versionadded:: 1.0.0

    .. versionchanged: TODO
        Move from finder.api to finder.utils.
    """
    for path in paths:
        path = os.path.expanduser(path) if not os.path.isabs(path) else path

        if not os.path.exists(path):
            log.info("{path} is not a valid path. Please provide a valid path."
                     .format(path=path))
            continue

        if os.path.isfile(path) and not is_executable(path):
            yield path
        elif os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                for file in files:
                    file_path = os.path.join(root, file)

                    if (os.path.isfile(file_path) and
                            is_readable(file_path) and
                            not is_image(file_path) and
                            not is_executable(file_path) and
                            not is_kernel_file(file_path) and
                            not is_audio(file_path) and
                            not is_video(file_path)):
                        yield file_path


def search(text=None, pattern=None):
    """Searches the given pattern in the given text.

    Args:
        text (str): Text in which the pattern needs to be searched.
        pattern (str): A string to be searched in the given `text`.

    Returns:
        bool: A boolean value stating whether the pattern is found in the
            given text or not.

    .. versionadded:: 1.0.0

    .. versionchanged:: TODO
        Move from finder.api to finder.utils.
    """
    return True if pattern in text else False


def split_params(params):
    """Returns a list of values from a given string of comma-separated values.

    .. versionadded:: 1.0.0
    """
    return params.split(',')
