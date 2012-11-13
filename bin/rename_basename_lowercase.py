#!/usr/bin/env python

import files
from rename_argparse import rename_argparse

if __name__ == '__main__':

    rename_argparse(
                files.act_basename_only(lambda s:s.lower()),
                add_act_noext_only=True,
            )
