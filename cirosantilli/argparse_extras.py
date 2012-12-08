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
import logging

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

def add_single_argument(
            parser,
            shortname,
            longname,
            default_kwargs,
            **custom_kwargs
        ):
    """adds a single argument to an argument parser
    
    custom_kwargs overwride default ones
    """
    add_argument_kwargs = default_kwargs.copy()
    add_argument_kwargs.update(custom_kwargs)
    parser.add_argument(shortname,longname,**add_argument_kwargs)

def add_act_full_path(
        parser,
        shortname='-F',
        longname='--act-full-path',
        **custom_kwargs
    ):

    add_single_argument(
        parser,
        shortname,
        longname,
        default_kwargs =
        {
            'action':'store_true',
            'default':False,
            'help':"if given, rename function acts on entire path. default: act on basename only",
        },
        **custom_kwargs
    )

def add_input_full_path(
        parser,
        shortname='-f',
        longname='--input-full-path',
        **custom_kwargs
    ):

    add_single_argument(
        parser,
        shortname,
        longname,
        default_kwargs =
        {
            'action':'store_true',
            'default':False,
            'help':"if given, rename function takes the full path as input,"
                "and returns only the basename. default: false",
        },
        **custom_kwargs
    )

CHAR_LOG_LEVELS = {
    'd':logging.DEBUG,
    'i':logging.INFO,
    'w':logging.WARNING,
    'e':logging.ERROR,
    'c':logging.CRITICAL,
}

LOG_LEVELS_CHAR = {v:k for (k,v) in CHAR_LOG_LEVELS.items()}

class LogLevelAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, CHAR_LOG_LEVELS[values[0]])

def add_log_level(
        parser,
        shortname='-L',
        longname='--log-level',
        **custom_kwargs
    ):
    """
    :param kwargs: are all passed to the parser.add_argument function.
            they overwride defaults set by this function

    :examples:
    >>> parser = argparse.ArgumentParser()
    >>> add_log_level(parser)
    >>> args = parser.parse_args([''])
    >>> args.log_level == logging.INFO
    True
    >>> args = parser.parse_args('-L w'.split())
    >>> args.log_level == logging.WARNING
    True
    >>> args = parser.parse_args('--log-level w'.split())
    >>> args.log_level == logging.WARNING
    True
    >>> add_log_level(parser,'-l','--new-long-name')
    >>> args = parser.parse_args('-lw'.split)
    >>> args.new_long_name == logging.WARNING
    True
    >>> add_log_level(parser,help='this is the new help, which overwrites the old one')
    """

    add_single_argument(
        parser,
        shortname,
        longname,
        default_kwargs={
            'help':
                "the level of user information to be output\n"+
                "possibilities:\n"+
                " %s: debug\n"%LOG_LEVELS_CHAR[logging.DEBUG]+
                " %s: information\n"%LOG_LEVELS_CHAR[logging.INFO]+
                " %s: warnings\n"%LOG_LEVELS_CHAR[logging.WARNING]+
                " %s: error\n"%LOG_LEVELS_CHAR[logging.ERROR]+
                " %s: critical\n"%LOG_LEVELS_CHAR[logging.CRITICAL],
                'default':logging.INFO,
            'choices':CHAR_LOG_LEVELS.keys(),
            'action':LogLevelAction
        },
        **custom_kwargs
    )

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
                    ('help',"if given, makes modifications, otherwise only"
                        "shows modifications that would have been made"),
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

class StdinArgvPathsAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, CHAR_LOG_LEVELS[values[0]])

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

def add_paths_from_stdin_and_argv(parser,before_paths_arg_adders=[]):
    add_null_separated_input(parser)
    for arg_adder in before_paths_arg_adders:
        arg_adder(parser)
    add_paths(parser)
