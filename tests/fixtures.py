# -*- coding: utf-8 -*-

import pytest

parametrize = pytest.mark.parametrize

# Random text retrieved from lorem ipsum generator. For further reference,
# check http://www.lipsum.com/.
_TEXT = '''Lorem ipsum dolor sit amet, vestibulum dui dictumst mauris in
turpis. Neque augue leo, pellentesque purus neque ornare atque, nec vitae,
tortor justo risus justo. Aptent pellentesque ipsum lacinia lacinia consequat,
at consectetuer eleifend rhoncus, hendrerit et amet erat, quisque mus sem hac
donec et.

Leo ut nullam, condimentum in accumsan eu dolor vestibulum, ac egestas
imperdiet felis amet. Id odio.

'''


@pytest.fixture
def create_temp_folder(tmpdir):
    """Fixture for creating temporary folder for tests."""
    def _create_temp_folder(subdirs, filenames):
        parent_dir = tmpdir.mkdir('parent')

        for subdir in subdirs:
            childdir = parent_dir.mkdir(subdir)

            for filename in filenames:
                fp = childdir.join(filename)
                fp.write(_TEXT)

        return str(parent_dir)
    return _create_temp_folder


@pytest.fixture
def create_temp_file(tmpdir):
    """Fixture for creating a temporary file."""
    def _create_temp_file(filename):
        fp = tmpdir.mkdir('parent').mkdir('child').join(filename)
        fp.write(_TEXT)
        return str(fp)
    return _create_temp_file
