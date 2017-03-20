# -*- coding: utf-8 -*-

import pytest

from finder.api import search
from .fixtures import parametrize


@parametrize('kargs,expected', [
    ({'text': 'hello world 1122', 'pattern': 'wor'}, True),
    ({'text': 'hello world 1122', 'pattern': 'w'}, True),
    ({'text': 'hello world 1122', 'pattern': '1122'}, True),
    ({'text': 'hello world 1122', 'pattern': ' '}, True),
    ({'text': 'hello world 1122', 'pattern': 'row'}, False)
])
def test_search_text(kargs, expected):
    """Test for validating the search function."""
    assert search(text=kargs['text'], pattern=kargs['pattern']) == expected


@parametrize('kargs,error_text', [
    ({'text': '', 'pattern': 'wor'}, 'Pattern should be provided'),
    ({'text': 'hello world', 'pattern': ''},
     'Text that needs to be searched should be provided.')
])
def test_search_text_error(kargs, error_text):
    """Test for validating whether the search function can raise an exception
    or not.
    """
    with pytest.raises(ValueError) as exc:
        search(text=kargs['text'], pattern=kargs['pattern'])
        assert error_text in str(exc)
