#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import unidecode

from cirosantilli import files
from cirosantilli.move_argparse import move_argparse

if __name__ == '__main__':

    move_argparse(
            files.act_basename_only(unidecode),
            epilog="rename mutiple files with unidecode",
            description="""takes paths from stdin null separated and from arguments and adds them up.

EXAMPLES

    %(f)s 中国.txt 美国.txt
    #renames given paths to "zhong guo.txt" and "mei guo.txt", according to unidecode

    find . | %(f)s
    #renames paths found
""")










