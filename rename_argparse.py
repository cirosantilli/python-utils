#!/usr/bin/env python

import sys
import argparse

import files

def rename_argparse(rename_func, **kwargs):
    """
    Convenient standard command line interface to rename files.

    Renames using the given rename_func function.

    **kwargs are given to the constructor of argparse.ArgumentParser.

    Takes paths to rename from both stdin nul separated and as arguments.

    Empty paths are ignored

    Takes 0 or 1 as last argument to decide dry run or not.

    Renaming functions acts as specified in files.rename_basenames.
    """

    act_basename_only = kwargs.pop("act_basename_only", False)

    parser = argparse.ArgumentParser(**kwargs)

    parser.add_argument("paths", 
        nargs='*',
        help="Paths to rename. Also takes paths nul separated from stdin and adds to those.")

    parser.add_argument('do_rename', 
        help="If 1 renames, otherwise dry-run.")

    args = parser.parse_args(sys.argv[1:])

    paths = args.paths

    if not sys.stdin.isatty(): # not connect to terminal teletype (tty): a pipe coming in!
        paths_str = sys.stdin.read()
        if paths_str:
            stdin_paths = paths_str.split("\x00") #splits at null
            stdin_paths = filter(lambda p: p, stdin_paths)
            paths.extend(stdin_paths)

    paths = map(lambda s: s.decode('UTF-8'), paths)

    do_rename = args.do_rename
    if do_rename == '1':
        do_rename = True
    elif do_rename == '0':
        do_rename = False
    else:
        raise ValueError("do_rename can only be 0 or 1")

    files.rename_basenames(paths, rename_func, do_rename, act_basename_only=act_basename_only)
