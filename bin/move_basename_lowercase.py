#!/usr/bin/env python

from cirosantilli import files
from cirosantilli.move_argparse import move_argparse

if __name__ == '__main__':

    move_argparse(
                files.act_basename_only(lambda s:s.lower()),
                add_act_noext_only=True,
            )










