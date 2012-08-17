#!/usr/bin/env python

import re
import argparse
import sys
import os

import files

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="""Searchs in current dir all paths whose basename match all given case insensitive regexes, and prints them newline separated to stdout.

This works like python re.search method: matchs anywhere inside basenames are enough.

Just a convenient 90% use case of find.

SAMPLE CALLS

find_basename_res.py first second

find_basename_res.py 'a.*b' '(a|b)+c'
""")

    parser.add_argument("re_strs", 
        nargs='*',
        help="regexes to use to filter, prints output iff given strings match all regexes.")

    args = parser.parse_args(sys.argv[1:])

    re_strs = args.re_strs

    res = map(lambda r: re.compile( unicode(r, sys.stdin.encoding),re.IGNORECASE | re.UNICODE), re_strs)

    for path in files.find(u"."):
        head, bname = os.path.split(path)
        all_match=True
        for reg in res:
            if not reg.search(bname):
                all_match = False
                break
        if all_match:
            print path

        

    


