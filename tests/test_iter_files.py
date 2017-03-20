# -*- coding: utf-8 -*-

from finder.api import iterfiles
from .fixtures import parametrize, create_temp_folder, create_temp_file


def validate_filenames(filepaths, expected_filenames):
    """Validates the results against the expected filenames."""
    results = list(iterfiles(filepaths))
    assert len(results) == len(expected_filenames)


@parametrize('subdirs,filenames,expected_filenames', [
    (['child1', 'child2'],
     ['childfile1.txt', 'childfile2.txt'],
     ['child1/childfile1.txt',
      'child1/childfile2.txt',
      'child2/childfile1.txt',
      'child2/childfile2.txt'])
])
def test_iterfiles_folder(create_temp_folder,
                          subdirs,
                          filenames,
                          expected_filenames):
    """Test for validating whether the method `iterfiles` can iterate through
    all the file names in a given folder or not.
    """
    folder_path = create_temp_folder(subdirs, filenames)
    validate_filenames(folder_path, expected_filenames)


@parametrize('filename,expected_filenames', [
    ('childfile1.txt', ['childfile1.txt'])
])
def test_iterfiles(create_temp_file, filename, expected_filenames):
    """Test for validating whether the method `iterfiles` can yield a given
    filepath (not a folder path).
    """
    file_path = create_temp_file(filename)
    validate_filenames(file_path, expected_filenames)
