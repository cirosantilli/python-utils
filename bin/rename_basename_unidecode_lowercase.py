#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unidecode

from cirosantilli.move_argparse import move_argparse
from cirosantilli import files

@files.act_basename_only
def rename_func(bname):
    return (unidecode.unidecode(bname)).lower()

if __name__ == '__main__':

    rename_argparse(
            rename_func,
            description="rename with unidecode and then to lowercase",
            epilog="""
EXAMPLES

    %(f)s ÁÊÌÕÜ.txt Çß.txt
    #renames to "aeiou.txt" and "cb.txt"

    find . | %(f)s
    #renames paths found
""")




