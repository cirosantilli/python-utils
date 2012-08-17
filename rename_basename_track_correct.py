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

    rename_argparse(remove_track,
            act_basename_only=True,
            description="""Command line interface that puts corrects many common track formats into my standard r"\d\d - ".

SAMPLE CALLS

find . -iname '*mp3' | rename_basename_track_correct.py 0
find . -iname '*mp3' | rename_basename_track_correct.py 1

SAMPLE RESULTS

1. Title.mp3
==>
01 - Title.mp3

11 Title.mp3
==>
11 - Title.mp3
""")
