#!/usr/bin/env python

import re
import os.path

import utils
from rename_argparse import rename_argparse

remove_track_resub = [re.compile(r"\d+ - "),""]
def remove_track(path):
    head, bname = os.path.split(path)
    new_bname = utils.resub(remove_track_resub, bname)
    return os.path.join(head, new_bname)

if __name__ == '__main__':

    rename_argparse(remove_track, description="""Command line interface for removing track numbers from songs in the format ^\d - .

01 - Title.mp3 ==> Title.mp3
1 - Title.mp3 ==> Title.mp3
""")
