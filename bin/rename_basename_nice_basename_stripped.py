#!/usr/bin/env python

import os

from rename_argparse import rename_argparse
import utils

if __name__ == '__main__':

    rename_argparse(utils.nice_basename_stripped,
            act_basename_only=True,
            description="""Tries to correct things that are either forbidden or highly unadvisable on basenames, by simply removing what is wrong.

See utils.nice_basename_stripped for the full spec.
            
SAMPLE CALLS

find subdir -print0 | rename_basename_nice_basename_stripped.py path1 path2 0
#will rename basename inside subdir tree and of path1 and path2 (but not of their subtrees)
""")
