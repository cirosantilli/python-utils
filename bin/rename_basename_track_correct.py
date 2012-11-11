#!/usr/bin/env python

import re
import os.path

import utils
from rename_argparse import rename_argparse

track_double_digit_resub = [re.compile(r"^(\d) - "),r"0\1 - "]
track_correct_resub= [re.compile(r"^(\d+)(\. | - | )"),r"\1 - "]

def remove_track(bname):
    bname = utils.resub(track_correct_resub, bname)
    bname = utils.resub(track_double_digit_resub, bname)
    return bname

if __name__ == '__main__':

    rename_argparse(
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
