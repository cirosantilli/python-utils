#!/usr/bin/env python

import re
import sys
import os
import itertools

import termcolor

import files
import argparse_extras

if __name__ == '__main__':

    parser = argparse_extras.ArgumentParser(
        description="find recursivelly paths whose basenames match all given regexes",
        epilog="""matches don't need to begin at start of basename.

EXAMPLES

    %(f)s ab cd 

        finds all files containing both "as" and "df" on their basenames

        sample finds:
          0aB1cD.txt

    %(f)s -0I ab cd

        I: case is taken into consideration
        
        0: output is null terminated

        sample *not* finds:
          0aB1cD.txt

    %(f)s -n ab cd

        -n: negates ab, but not cd

        sample finds:
            0cD1.txt
        
        sample *not* finds:
            0aB1cD.txt
            > this contains ab

    (%(f)s -n ab;%(f)s cd)
        
        this is how you can do a OR operation at bash command line!

        using and, not and or, you can get any expression.

        sample finds:
            0ab1cd.txt
            01.txt
            0cd1.txt

        sample *not* finds:
            0ab1.txt

TODO
    
    add option to output full path
""")

    #optional

    argparse_extras.add_not_ignorecase(parser)

    parser.add_argument('-m','--min-depth' ,
            default=0,
            action='store',
            type=int,
            help="min search depth. 1 makes search start from current dir"
        )

    parser.add_argument('-M','--max-depth' ,
            default=float('inf'),
            action='store',
            type=int,
            help="max search depth. 1 limits search to current dir"
        )

    parser.add_argument('-n','--negated' ,
        default=[],
        action='append',
        help="if the following regex matches, exclude from output")

    argparse_extras.add_null_separated_output(parser)

    #positional

    parser.add_argument('find', 
        nargs='*',
        help="regexes to use to filter, prints output iff given strings match all regexes")


    args = parser.parse_args()

    #adapter
    re_args = re.UNICODE
    if args.ignorecase:
        re_args = re_args | re.IGNORECASE

    negated = args.negated

    min_depth = args.min_depth
    max_depth = args.max_depth
    res = map(lambda r: re.compile( unicode(r, sys.stdin.encoding), re_args), args.find)
    negated_res = map(lambda r: re.compile( unicode(r, sys.stdin.encoding), re_args), args.negated)

    if args.null_separated_output:
        output_separator = u"\0"
    else:
        output_separator = u"\n"

    #act
    for path in files.find(
                u".",
                min_depth=min_depth,
                max_depth=max_depth,
            ):
        head, bname = os.path.split(path)
        accept=True
        color_spans = [] #start end pairs span pairs to color in between
        for reg in res:
            matches = list(reg.finditer(bname))
            if matches:
                color_spans.extend(m.span() for m in matches)
            else:
                accept = False
                break
        if accept:
            for reg in negated_res:
                if reg.search(bname):
                    accept = False
                    break
        if accept:
            sys.stdout.write( head + os.path.sep )
            for i,c in itertools.izip(itertools.count(),bname): 
                printed = False
                for color_span in color_spans:
                    if i >= color_span[0] and i < color_span[1]:
                        termcolor.cprint(c,'red',attrs=['bold'],end='')
                        printed = True
                        break;
                if not printed:
                    sys.stdout.write( c )
            sys.stdout.write( output_separator)
