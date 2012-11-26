#!/usr/bin/env python

import os

from cirosantilli.move_argparse import move_argparse
import utils
from cirosantilli import files

if __name__ == '__main__':

    rename_argparse(
            files.act_basename_only(utils.nice_basename_stripped),
            description="corrects filenames that are forbidden" \
                "or highly unadvisable on Linux/Windows/Mac by stripping bad things if possible",
            epilog="""EXAMPLES

    %(f)s a:b;c -rf as..txt
    #dry run

    %(f)s -D a:b;c -rf as..txt
    #not Dry run
    #renames to "abc" "rf" and "as.txt"

    find . | %(f)s
    #acts on found files
""")




