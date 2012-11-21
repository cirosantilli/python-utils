#!/usr/bin/env python

#============================================================
#
# Ciro D. Santilli 
#
# factor out common argparse calls
#
#============================================================

import os
import sys
import argparse

SECTION_TITLES = {
    'examples':'EXAMPLES',
}

class ArgumentParser(argparse.ArgumentParser):
    """argument parser with better defaults"""

    def __init__(self,*args,**kwargs):
        """
        the following kwargs are modified as follows:
            - epilog = kwargs.get('epilog',"") % {'f':os.path.basename(__file__)},
            - formatter_class=kwargs.get('formatter_class',argparse.RawTextHelpFormatter), #keep newlines
        """
        kwargs['epilog'] = kwargs.get('epilog',"") % {'f':os.path.basename(sys.argv[0])}
        kwargs['formatter_class'] = kwargs.get('formatter_class',argparse.RawTextHelpFormatter)
        super(ArgumentParser,self).__init__(*args,**kwargs)

def add_not_dry_run(
            parser,
            shortname='-D',
            longname='--not-dry-run',
            **kwargs
        ):

    kwargs = dict(
                [
                    ('action','store_true'),
                    ('default',False),
                    ('help',"if given, makes modifications, otherwise only shows modifications that would have been made"),
                ]
                + kwargs.items()
            )
    
    parser.add_argument(
            shortname,
            longname,
            **kwargs
        )

def add_not_act_on_extension(
            parser,
            shortname='-E',
            longname='--not-act-on-extension',
            **kwargs
        ):
    """by default creates a variable called *act_on_extension*, and not not_act_on_extension"""

    kwargs = dict(
                [
                    ('default',True),
                    ('action','store_false'),
                    ('dest','act_on_extension'),
                    ('help',"if given, don't act on the extensin (acts by default)"),
                ]
                + kwargs.items()
            )
    
    parser.add_argument(
            shortname,
            longname,
            **kwargs
        )

def add_not_ignorecase(
            parser,
            shortname='-I',
            longname='--not-ignorecase',
            **kwargs
        ):
    """by default creates a variable called *ignorecase*, and not not_ignorecase"""

    kwargs = dict(
                [
                    ('default',True),
                    ('action','store_false'),
                    ('dest','ignorecase'),
                    ('help',"if given, do not ignore case (enabled by default)"),
                ]
                + kwargs.items()
            )
    
    parser.add_argument(
            shortname,
            longname,
            **kwargs
        )

def add_null_separated_input(
            parser,
            shortname='-0',
            longname='--null-separated-input',
            **kwargs
        ):

    kwargs = dict(
                [
                    ('action','store_true'),
                    ('default',False),
                    ('help',"if given, input is assumed to be null separated, otherwise newline separated"),
                ]
                + kwargs.items()
            )
    
    parser.add_argument(
            shortname,
            longname,
            **kwargs
        )

def add_null_separated_output(
            parser,
            shortname='-0',
            longname='--null-separated-output',
            **kwargs
        ):

    kwargs = dict(
                [
                    ('action','store_true'),
                    ('default',False),
                    ('help',"if given, output is assumed to be null separated, otherwise newline separated"),
                ]
                + kwargs.items()
            )
    
    parser.add_argument(
            shortname,
            longname,
            **kwargs
        )

def add_paths(
            parser,
            name="paths",
            **kwargs
        ):

    kwargs = dict(
                [
                    ('nargs','*'),
                    ('help',"paths to rename. Also takes paths nul separated from stdin and adds to those"),
                ]
                + kwargs.items()
            )
    
    parser.add_argument(
            name,
            **kwargs
        )

def add_silent(

            parser,
            shortname='-s',
            longname='--silent',
            **kwargs
        ):

    kwargs = dict(
                [
                    ('action','store_true'),
                    ('default',False),
                    ('help',"if given, informative output is made to stderr, not even error messages"),
                ]
                + kwargs.items()
            )
    
    parser.add_argument(
            shortname,
            longname,
            **kwargs
        )


def add_paths_from_stdin_and_argv(parser,before_paths_arg_adders=[]):
    add_null_separated_input(parser)
    for arg_adder in before_paths_arg_adders:
        arg_adder(parser)
    add_paths(parser)

def get_stdin_items(sep, encoding):
    if not sys.stdin.isatty():
        items_str = sys.stdin.read()
        if items_str:
            stdin_items = items_str.split(sep)
            stdin_items = filter(lambda p: p, stdin_items) #only get non-empty items. last path is probably empty, since the items="path1\npath2\n" and split gives [path1, path2, ""]
            return stdin_items
    else:
        return []

def get_paths_from_stdin_and_argv(
            args,
            null_separated_input_argname='null_separated_input',
            paths_input_argname='null_separated_input',
            encoding='utf-8',
        ):

    if getattr(args,'null_separated_input'):
        sep = "\0"
    else:
        sep = "\n"

    paths = getattr(args,'paths')
    paths.extend(get_stdin_items(sep,encoding))

    return map(lambda s: s.decode(encoding), paths)
