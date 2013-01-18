#!/usr/bin/env python

import re
import os.path

from cirosantilli import utils
from cirosantilli.move_argparse import move_argparse
from cirosantilli import files

track_correct_resub = [re.compile(r"(^| - )(\d+)( - |[._\-]( |)| )"),r"\1\2 - "]
track_double_digit_resub = [re.compile(r"^(\d) - "),r"0\1 - "]

@files.act_noext_only
@files.act_basename_only
def track_correct(path):
    path = utils.resub(track_correct_resub, path)
    path = utils.resub(track_double_digit_resub, path)
    path = path.replace('_',' ')
    return path

if __name__ == '__main__':

    move_argparse(
            track_correct,
            description="converts many common track formats into my standard r\"\d\d - title.mpr\"",
            epilog="""EXAMPLES

    %(f)s '1. title.mp3' '11 title.mp3'
    #dry run
    #new names:
    # 01 - title.mp3
    # 11 - title.mp3

    %(f)s -D '1. title.mp3' '11 title.mp3'
    #not dry run

    find . -iname '*mp3' | %(f)s
    #act on multiple files
""")
