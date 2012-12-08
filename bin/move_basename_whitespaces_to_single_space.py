#!/usr/bin/env python

import re
import os.path

from cirosantilli import utils
from cirosantilli.move_argparse import move_argparse
from cirosantilli import files

@files.act_basename_only
def rename_func(path):
    return utils.whitespaces_to_single_space(path)

if __name__ == '__main__':

    move_argparse(rename_func)










