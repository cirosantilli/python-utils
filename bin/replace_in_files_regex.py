#!/usr/bin/env python

import sys
import argparse
from argparse import RawTextHelpFormatter
import re
import os.path

from cirosantilli import files

if __name__ == '__main__':

    f = os.path.basename(__file__)
    parser = argparse.ArgumentParser(
        prog=f,
        description="Replaces in multiple files linewise with python regexes.",
        epilog=r"""Shows only modified lines and files on stderr.

SAMPLE CALLS

  find . -type f | %s -i 'find(\d)' 'replace\1'
  #finds and replaces using python re.sub(), case insensitive
  #see: http://docs.python.org/dev/library/re.html#re.sub
  #prints modified lines to stderr
  #this is a dry-run: files are not modified, only changes are shown

  find . -type f | %s -iD 'find(\d)' 'replace\1'
  #D means *not* dry run. files are modified
""" % (f, f),
        formatter_class=RawTextHelpFormatter,
        )
    #parser.add_argument('-d', '--dotall',
        #help="same as python regex dotall",
        #default=False,
        #action="store_true",)

    parser.add_argument('-D', '--not-dry-run',
        help="not a dry run",
        default=False,
        action="store_true",)

    parser.add_argument('-i', '--ignorecase',
        help="same as python regex ignorecase",
        default=False,
        action="store_true",)

    parser.add_argument('-l', '--locale',
        help="same as python regex locale",
        default=False,
        action="store_true",)

    #parser.add_argument('-m', '--multiline',
        #help="same as python regex multiline",
        #default=False,
        #action="store_true",)

    parser.add_argument('-u', '--unicode',
        help="same as python regex unicode",
        default=False,
        action="store_true",)

    parser.add_argument('-0','--null-terminated',
        help="if given, split paths at null char. else split at newline",
        default=False,
        action="store_true",)

    parser.add_argument('find', 
        help="regex to find")

    parser.add_argument('replace', 
        help="python replace regex string")

    parser.add_argument("paths", 
        nargs='*',
        help="paths to rename. Also takes paths null separated from stdin and adds to those.")

    args = parser.parse_args(sys.argv[1:])

    #get the real params out of the args
    regex_params = 0
    #if args.dotall:
        #regex_params.append(re.DOTALL)
    if args.ignorecase:
        regex_params = regex_params | re.IGNORECASE
    if args.locale:
        regex_params = regex_params | re.LOCALE
    #if args.multiline:
        #regex_params.append(re.MULTILINE)
    if args.unicode:
        regex_params = regex_params | re.UNICODE

    not_dry_run = args.not_dry_run

    if args.null_terminated:
        path_separator = "\x00"
    else:
        path_separator = "\n"
    paths = args.paths
    if not sys.stdin.isatty(): #not connect to terminal teletype (tty): a pipe coming in!
        paths_str = sys.stdin.read()
        if paths_str:
            stdin_paths = paths_str.split(path_separator) #splits at null
            stdin_paths = filter(lambda p: p, stdin_paths) #removes empty paths (after last \n of \0)
            paths.extend(stdin_paths)
    paths.sort()

    find = args.find
    replace = args.replace

    #work!
    p = re.compile(find, regex_params)
    for path in paths:
        old = files.read(path)
        new = ""
        output = ""
        had_match = False
        i = 0
        for line in old.split("\n"):
            old_line = line
            new_line = p.sub(replace, line)
            if old_line != new_line:
                output += "%i    %s\n" % (i,old_line)
                output += "%i    %s\n\n" % (i,new_line)
                had_match = True
            new += (new_line) + "\n"
            i=i+1
        if had_match:
            output = "%s\n%s\n\n%s" % ("="*70,path, output)
            sys.stderr.write( output )
        if not_dry_run:
            files.write(path, new)




