# -*- coding: utf-8 -*-

from .fixtures import parametrize, create_temp_file
from finder.api import read


@parametrize('filename', [
    'childfile1.txt'
])
def test_read_file(filename, create_temp_file):
    """Test that validates whether the line count from the file is correct or
    not.
    """
    file_path = create_temp_file(filename)
    total_line_count = max([i for i, j in read(file_path)])

    with open(file_path, 'r') as fp:
        assert len(fp.readlines()) == total_line_count
