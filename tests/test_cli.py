# -*- coding: utf-8 -*-

import pytest
from click.testing import CliRunner

from finder.cli import finder
from finder.__pkg__ import __version__

from .fixtures import create_temp_folder, parametrize


@pytest.yield_fixture
def cli():
    runner = CliRunner()
    yield runner


def test_finder_version(cli):
    """Test that validates the version of finder tool."""
    result = cli.invoke(finder, ['--version'])

    assert result.exit_code == 0
    assert result.output.strip() == __version__


@parametrize('data', [
    {'subdirs': ['child1', 'child2'],
     'filenames': ['childfile1.txt', 'childfile2.txt'],
     'args': ['search',
              '--pattern={0}'.format('Lorem')],
     'expected_output':
         [['1', ' Lorem ipsum dolor sit amet, vestibulum dui dictumst mauris '
                'in']]},
    {'subdirs': ['child1', 'child2'],
     'filenames': ['childfile1.txt', 'childfile2.txt'],
     'args': ['search',
              '--pattern={0}'.format('in')],
     'expected_output':
         [['1', ' Lorem ipsum dolor sit amet, vestibulum dui dictumst mauris '
                'in'],
          ['3', ' tortor justo risus justo. Aptent pellentesque ipsum lacinia '
                'lacinia consequat,'],
          ['7', ' Leo ut nullam, condimentum in accumsan eu dolor vestibulum, '
                'ac egestas']]},
    {'subdirs': ['child1', 'child2'],
     'filenames': ['childfile1.txt', 'childfile2.txt'],
     'args': ['search',
              '--pattern={0}'.format('Lorem'),
              '--verbose'],
     'expected_output':
         [['1', ' Lorem ipsum dolor sit amet, vestibulum dui dictumst mauris '
                'in']]},
    {'subdirs': ['child1', 'child2'],
     'filenames': ['childfile1.txt', 'childfile2.txt'],
     'args': ['search',
              '--pattern={0}'.format('in'),
              '--verbose'],
     'expected_output':
         [['1', ' Lorem ipsum dolor sit amet, vestibulum dui dictumst mauris '
                'in'],
          ['3', ' tortor justo risus justo. Aptent pellentesque ipsum lacinia '
                'lacinia consequat,'],
          ['7', ' Leo ut nullam, condimentum in accumsan eu dolor vestibulum, '
                'ac egestas']]},
])
def test_search_normal_view(cli, create_temp_folder, data):
    """Test for validating finder's search functionality."""
    folder_path = create_temp_folder(data['subdirs'], data['filenames'])

    args = data['args'] + ['--path={0}'.format(folder_path)]

    result = cli.invoke(finder, args)
    out = result.output.strip()

    for output in out.split('\n'):
        assert output.split(':')[1:] in data['expected_output']

    assert result.exit_code == 0
