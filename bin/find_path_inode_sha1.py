#!/usr/bin/env python

#------------------------------------------------------------
#
# Ciro D. Santilli 
#
# Prints a list of paths which are files followed by their inodes and sha1 sums.
#
# Useful to make a backup of paths names before mass renaming them,
# supposing your files are distinct by SHA1 and that SHA1 has not changed,
# or that the inodes have not changed.
#
#------------------------------------------------------------

import os
import os.path
import stat
import hashlib
import sys

KBYTE = 2**10
SHA1_MAX_BYTES_READ_DEFAULT = 100*KBYTE

def sha1_hex_file(filepath, max_bytes=None):
    """
    Returns the SHA1 of a given filepath in hexadecimal.

    Opt-args:

    * max_bytes. If given, reads at most max_bytes bytes from the file.
    """

    sha1 = hashlib.sha1()
    f = open(filepath, 'rb')
    try:
        if max_bytes:
            data = f.read(max_bytes)
        else:
            data = f.read()
        sha1.update(data)
    finally:
        f.close()
    return sha1.hexdigest()

if __name__ == '__main__':


    import argparse
    from argparse import RawTextHelpFormatter

    parser = argparse.ArgumentParser(description="""Finds files and creates a lists of their paths, inodes and sha1 checksums.' +

Useful to make a backup of filepaths before renaming them, for example before a large number of renames by a script.""",
    formatter_class=RawTextHelpFormatter,
        )

    parser.add_argument('-n', '--sha1-max-nbytes',
        nargs=1,
        action="store", 
        dest="sha1_max_bytes_read_default",
        default=SHA1_MAX_BYTES_READ_DEFAULT,
        help='Maximun number of bytes to read to calculate SHA1 checksum.'+
            'Reading the whole file might be too slow, and unnecessary for some applications.')

    parser.add_argument('-w', '--write-output-to-file', 
        action="store_true", 
        dest="write_output_to_file",
        default=False, 
        help='a is False if not present')

    args = parser.parse_args(sys.argv[1:])
    sha1_max_bytes_read = args.sha1_max_bytes_read_default
    write_output_to_file = args.write_output_to_file

    file_output = ""

    print "sha1_max_bytes_read"
    print sha1_max_bytes_read
    print

    paths = []
    for root, dirs, files in os.walk('.'):
        for bname in files:
            paths.append(os.path.join(root,bname))
    paths.sort()

    for path in paths:
        print path
        print str(os.stat(path)[stat.ST_INO])
        print str(sha1_hex_file(path,sha1_max_bytes_read))
        print




