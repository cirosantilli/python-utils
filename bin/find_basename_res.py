#!/usr/bin/env python

import re
import argparse
import sys
import os

import files
import argparse_extras

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description="find recursivelly paths whose basenames match all given regexes",
        epilog="""Searchs in current dir all paths whose basename match all given case insensitive regexes, and prints them separated to stdout.

This works like python re.search method: matchs anywhere inside basenames are enough.

EXAMPLES

    find_basename_res.py ab cd 
    #finds all files containing both "as" and "df" on their basenames

    find_basename_res.py -0I 'a.*b' '(a|b)+c'
    #finds all files containing both regexes on their basenames
    #I: case is taken into consideration
    #0: output is null terminated
""")

    argparse_extras.add_not_ignorecase(parser)
    argparse_extras.add_null_separated_output(parser)
    parser.add_argument("find", 
        nargs='*',
        help="regexes to use to filter, prints output iff given strings match all regexes")

    args = parser.parse_args(sys.argv[1:])

    #adapter
    re_args = re.UNICODE
    if args.ignorecase:
        re_args = re_args | re.IGNORECASE

    find = args.find

    res = map(lambda r: re.compile( unicode(r, sys.stdin.encoding), re_args), find)

    if args.null_separated_output:
        output_separator = u"\0"
    else:
        output_separator = u"\n"

    #act
    for path in files.find(u"."):
        head, bname = os.path.split(path)
        all_match=True
        for reg in res:
            if not reg.search(bname):
                all_match = False
                break
        if all_match:
            sys.stdout.write( (path + output_separator).encode('utf-8') )
