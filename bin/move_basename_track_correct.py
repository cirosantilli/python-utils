#!/usr/bin/env python

import re
import os.path

from cirosantilli import utils
from cirosantilli.move_argparse import move_argparse
from cirosantilli import files

track_double_digit_resub = [re.compile(r"^(\d) - "),r"0\1 - "]
track_correct_resub = [re.compile(r"^(\d+)(\. | - | )"),r"\1 - "]

@files.act_basename_only
def remove_track(path):
    path = utils.resub(track_correct_resub, path)
    path = utils.resub(track_double_digit_resub, path)
    return bname

if __name__ == '__main__':

    move_argparse(
            remove_track,
            description="corrects many common track formats into my standard r\"\d\d - title.mpr\"",
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










