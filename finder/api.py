# -*- coding: utf-8 -*-
# Module used in searching the given pattern in the text provided.


def search(text=None, pattern=None):
    """Helps in searching the given pattern in the given text.

    Args:
        text (str): Text in which the pattern needs to be searched.
        pattern (str): A string to be searched in the given `text`.

    Returns:
        bool: A boolean value stating whether the pattern is found in the
            given text or not.

    .. versionadded:: TODO
    """
    if not text and pattern:
        raise ValueError('Text that needs to be searched should be provided.')

    if text and not pattern:
        raise ValueError('Pattern should be provided to be searched.')

    return True if pattern in text else False
