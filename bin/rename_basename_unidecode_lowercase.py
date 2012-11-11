#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path

from rename_argparse import rename_argparse
import unidecode

def unidecode_lowercase(bname):
    return (unidecode.unidecode(bname)).lower()

if __name__ == '__main__':

    rename_argparse(unidecode_lowercase,
            description="rename with unidecode and then to lowercase",
            epilog="""
EXAMPLES

    %(f)s ÁÊÌÕÜ.txt Çß.txt
    #renames to "aeiou.txt" and "cb.txt"

    find . | %(f)s
    #renames paths found
""")
