# -*- coding: utf-8 -*-

import pytest

parametrize = pytest.mark.parametrize


@pytest.fixture
def create_temp_folder(tmpdir):
    """Fixture for creating temporary folder for tests."""
    def _create_temp_folder(subdirs, filenames):
        parent_dir = tmpdir.mkdir('parent')

        for subdir in subdirs:
            childdir = parent_dir.mkdir(subdir)

            for filename in filenames:
                fp = childdir.join(filename)
                fp.write('content')

        return str(parent_dir)
    return _create_temp_folder


@pytest.fixture
def create_temp_file(tmpdir):
    """Fixture for creating a temporary file."""
    def _create_temp_file(filename):
        fp = tmpdir.mkdir('parent').mkdir('child').join(filename)
        fp.write('content')
        return str(fp)
    return _create_temp_file
