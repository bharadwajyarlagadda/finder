# -*- coding: utf-8 -*-

import pytest
from click.testing import CliRunner

from finder.cli import finder

from .fixtures import create_temp_folder, parametrize


@pytest.yield_fixture
def cli():
    runner = CliRunner()
    yield runner


@parametrize('subdirs,filenames,pattern', [
    (['child1', 'child2'],
     ['childfile1.txt', 'childfile2.txt'],
     'Lorem')
])
def test_search_cli(cli,
                    create_temp_folder,
                    subdirs,
                    filenames,
                    pattern):
    """Test for validating CLI functionality."""
    folder_path = create_temp_folder(subdirs, filenames)

    args = ['search',
            '--path={0}'.format(folder_path),
            '--pattern={0}'.format(pattern)]

    result = cli.invoke(finder, args)

    assert result.exit_code == 0
