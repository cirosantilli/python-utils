#!/usr/bin/env python

import re
import argparse
import sys
import os

import files

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="""Searchs in current dir all paths whose basename match all given case insensitive regexes, and prints them separated to stdout.

This works like python re.search method: matchs anywhere inside basenames are enough.

SAMPLE CALLS

    find_basename_res.py ab cd 
    #finds all files containing both "as" and "df" on their basenames

    find_basename_res.py -0I 'a.*b' '(a|b)+c'
    #finds all files containing both regexes on their basenames
    #I: case is taken into consideration
    #0: output is null terminated
""")

    parser.add_argument("-I", "--not-ignorecase",
        default=False,
        action='store_true',
        help="if given takes case into consideration")
    parser.add_argument("-0", "--null-separated-output",
        default=False,
        action='store_true',
        help="if given, separates output bu null characters instead of newlines. useful for piping files with newlines on their names")
    parser.add_argument("find", 
        nargs='*',
        help="regexes to use to filter, prints output iff given strings match all regexes.")

    args = parser.parse_args(sys.argv[1:])

    #transforms user input into app input
    re_args = re.UNICODE
    if not args.not_ignorecase:
        re_args = re_args | re.IGNORECASE

    find = args.find

    res = map(lambda r: re.compile( unicode(r, sys.stdin.encoding), re_args), find)

    if args.null_separated_output:
        output_separator = "\0"
    else:
        output_separator = "\n"


    for path in files.find(u"."):
        head, bname = os.path.split(path)
        all_match=True
        for reg in res:
            if not reg.search(bname):
                all_match = False
                break
        if all_match:
            sys.stdout.write(path + output_separator)
