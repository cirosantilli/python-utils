#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import unidecode

import files
from rename_argparse import rename_argparse

if __name__ == '__main__':

    rename_argparse(
            files.act_basename_only(unidecode),
            epilog="rename mutiple files with unidecode",
            description="""takes paths from stdin null separated and from arguments and adds them up.

EXAMPLES

    %(f)s 中国.txt 美国.txt
    #renames given paths to "zhong guo.txt" and "mei guo.txt", according to unidecode

    find . | %(f)s
    #renames paths found
""")
