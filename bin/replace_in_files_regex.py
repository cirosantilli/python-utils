#!/usr/bin/env python

import sys
import argparse
from argparse import RawTextHelpFormatter
import re
import os.path

from cirosantilli import files

def _chomp(s):
    if s:
        return s[:-1]

if __name__ == '__main__':

    f = os.path.basename(__file__)
    parser = argparse.ArgumentParser(
        prog=f,
        description="Replaces in multiple files linewise with python regexes.",
        epilog=r"""Shows only modified lines and files on stderr.

SUMMARY

   directories are ignored 

EXAMPLES

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


    dotall_longname = '--dotall'
    multiline_longname = '--multiline'

    parser.add_argument('-d', dotall_longname,
        help="dot '.' matches all chars, including newlines. implies %s"%multiline_longname,
        default=False,
        action="store_true",)

    parser.add_argument('-D', '--not-dry-run',
        help="not a dry run",
        default=False,
        action="store_true",)

    parser.add_argument('-i', '--ignorecase',
        help="same as python regex ignorecase",
        default=False,
        action="store_true",)

    parser.add_argument(
        '-m',
        multiline_longname,
        help="acts on entire file instead of linewise."
            "'^' and '$' match the beginning and end of file."
            "this does *not* imply that dot '.' matches newlines."
            "use %s option for that behaviour"%dotall_longname,
        default=False,
        action="store_true",
    )

    parser.add_argument('-l', '--locale',
        help="same as python regex locale",
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

    multiline_mode = False
    regex_params = re.UNICODE
    if args.ignorecase:
        regex_params = regex_params | re.IGNORECASE
    if args.locale:
        regex_params = regex_params | re.LOCALE
    if args.dotall:
        regex_params = regex_params | re.DOTALL | re.MULTILINE
        multiline_mode = True
    elif args.multiline:
        regex_params = regex_params | re.MULTILINE
        multiline_mode = True

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
    sep = ' '*2
    p = re.compile(find, regex_params)
    for path in paths:
        new = ""
        output = ""
        had_change = False
        try:

            with open(path,'r') as f:

                #multiline
                if multiline_mode:
                    old = f.read(path)
                    old = _chomp(old)
                    new = p.sub(replace, old)
                    if old != new:
                        had_change = True
                        output = new + "\n\n"

                #linewise
                else:
                    i = 0
                    for old_line in f.xreadlines():
                        old_line = _chomp(old_line)
                        new_line = p.sub(replace, old_line)
                        if old_line != new_line:
                            output += "%i%s%s\n" % (i,sep,old_line)
                            output += "%i%s%s\n" % (i,sep,new_line)
                            had_change = True
                        new += (new_line) + "\n"
                        i=i+1

        except IOError, e:
            logging.error(e)
            continue

        if had_change:
            output = "\n"+"="*70 + "\n" + path + "\n\n" + output
            sys.stderr.write( output )
            if not_dry_run:
                files.write(path, new)
