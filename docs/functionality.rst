Functionality
=============

1. The main entry point for our API is the ``api.find()`` method. You can pass in both file/directory paths and the pattern to be searched for.
2. If you provide a directory path, it will go ahead and do a ``os.walk`` and brings out all the files in that directory path.
3. While searching for the pattern,
    1. It avoids all the non-readable files:
        1. Audio files.
        2. Video files.
        3. Image files.
        4. Some of the kernel based files such as the files under ``/proc`` in ``Ubuntu/Linux.``
    2. It reads the file line by line so that we can avoid saving the whole file in the memory (which of course will be memory issue for huge files).
4. This whole process runs concurrently. As in, the API allots thread for each file to be searched and once the search is complete, the thread comes and joins back in the main process.
5. I personally have tested the performance and the memory usage is very low. If you face any of the performance issues, please report it at Issues_.
6. The data from the API looks is explained under ``Schema`` section. The output fields are also explained in the same section.
7. The output data is a JSON-encoded string and it is generated only when ``finder`` finds tha pattern in a given file.

.. _Issues: https://github.com/bharadwajyarlagadda/finder/issues
