# -*- coding: utf-8 -*-

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
