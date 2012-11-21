#!/usr/bin/env python

import re

from rename_argparse import rename_argparse
import utils
import files

def add_find(parser):
    """add find arg to given argument parser"""
    parser.add_argument(
            'find',
            nargs=1,
            help="regex to find",
        )

def add_replace(parser):
    """add replace arg to given argument parser"""
    parser.add_argument(
            'replace',
            nargs=1,
            help="regex to replace",
        )

def controller(args):
    return (
            [args.find[0],args.replace[0]],
            {
                'ignorecase':args.ignorecase,
                'act_on_extension':args.act_on_extension,
            }
        )
    
@files.act_basename_only
def rename_func(path,*args,**kwargs):

    find_str = args[0]
    replace_str = args[1]

    ignorecase = kwargs.get('ignorecase',True)

    re_args = re.UNICODE
    if ignorecase:
        re_args = re_args | re.IGNORECASE

    find_re = re.compile(find_str,re_args)

    return utils.resub((find_re,replace_str),path)

if __name__ == '__main__':

    rename_argparse(
            rename_func,
            func_arg_adders=[add_find,add_replace],
            func_arg_controller=controller,
            add_act_noext_only=True,
            description="renames multiple files using a python regex find replace pair",
            epilog="""
EXAMPLES

    %(f)s 'a(.+?)a' '\1' aBBBBa.txt 00a11aa22a.txt
    #dry run
    #renames to:
    #  BBBB.txt
    #  001122.txt

    %(f)s -D 'a(.*?)a' '\1' aBBBBa.txt 00a11ca22c.txt
    #not Dry run: really renames!

    ls | %(f)s a b
    #act current dir

    find . | %(f)s a b
    #act on found items

    find . | %(f)s -I a b
    #don't Ignore case (enabled by default)

    find . | %(f)s -E a b
    #don't act on Extension
""")
