#!/usr/bin/env python

import os.path

from rename_argparse import rename_argparse
import unidecode

def unidecode_lowercase(bname):
    return unidecode.unidecode(bname).lower()

if __name__ == '__main__':

    rename_argparse(unidecode_lowercase,
            act_basename_only=True,
            description="""Command line interface for renaming with unidecode and then to lowercase.

Takes paths from stdin null separated and from arguments and adds them up.

EXAMPLE:

find subdir -print0 | rename_basename_unidecode_lowercase.py path1 path2 0
#will rename basename inside subdir tree and of path1 and path2 (but not of their subtrees)
""")
