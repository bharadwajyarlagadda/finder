Changelog
=========


v1.0.2 (2017-05-07)
-------------------

- FIX bug in CHANGELOG.


v1.0.1 (2017-05-07)
-------------------

- Minor updates.


v1.0.0 (2017-05-07)
-------------------

- Add ``search`` method to search for a given pattern in the text provided.
- Add ``iterfiles`` method to yield all the file paths in a given folder path.
- Add ``is_executable`` method to validate whether the given file is a executable or not.
- Add ``read`` method to read a given file line by line.
- Add wrapper method ``find`` to iterate through the given list of files/directories and find the given pattern in the files.
- Add ``FileReader`` class to searching all the files concurrently.
- Add schemas for serializing the data to a JSON-encoded string.
- Add command line wrapper around the API. User can now use the command line interface to get all the search results.
