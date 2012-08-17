#!/usr/bin/env python

import os

from rename_argparse import rename_argparse
from unidecode_wrap import unidecode_wrap

def unidecode_basename(path):
    head, bname = os.path.split(path)
    new_bname = unidecode_wrap(bname)
    return os.path.join(head, new_bname)

if __name__ == '__main__':

    rename_argparse(unidecode_basename, description="""Command line interface for renaming with unidecode,

based on rename_argparse.

Takes paths from stdin null separated and from arguments and adds them up.

EXAMPLE:

find subdir -print0 | rename_basename_unidecode.py path1 path2 0
#will rename basename inside subdir tree and of path1 and path2 (but not of their subtrees)
""")
