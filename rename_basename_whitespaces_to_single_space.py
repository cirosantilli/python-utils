#!/usr/bin/env python

import re
import os.path

import utils
from rename_argparse import rename_argparse

def remove_track(bname):
    return utils.whitespaces_to_single_space(bname)

if __name__ == '__main__':

    rename_argparse(remove_track, act_basename_only=True)
