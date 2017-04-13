# -*- coding: utf-8 -*-

import json

import pytest

from finder.api import find
from .fixtures import create_temp_folder, parametrize


@parametrize('data', [
    {'subdirs': ['child1', 'child2'],
     'filenames': ['childfile1.txt', 'childfile2.txt'],
     'pattern': 'Lorem',
     'expected_total_items': '1',
     'expected_items': [{
         'line_number': '1',
         'line': 'Lorem ipsum dolor sit amet, vestibulum dui dictumst mauris '
                 'in'}]},
    {'subdirs': ['child1', 'child2'],
     'filenames': ['childfile1.txt', 'childfile2.txt'],
     'pattern': 'in',
     'expected_total_items': '3',
     'expected_items': [
         {'line_number': '1',
          'line': 'Lorem ipsum dolor sit amet, vestibulum dui dictumst mauris '
                  'in'},
         {'line_number': '3',
          'line': 'tortor justo risus justo. Aptent pellentesque ipsum '
                  'lacinia lacinia consequat,'},
         {'line_number': '7',
          'line': 'Leo ut nullam, condimentum in accumsan eu dolor vestibulum,'
                  ' ac egestas'}]},
])
def test_find(create_temp_folder, data):
    """Tests that validates whether `find()` is able to retrieve the expected
    line and line number.
    """
    folder_path = create_temp_folder(data['subdirs'], data['filenames'])

    for result in find(folder_path, pattern=data['pattern']):
        _result = json.loads(result)
        assert _result['total_items'] == data['expected_total_items']

        assert _result['items'] == data['expected_items']
