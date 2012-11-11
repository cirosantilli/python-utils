#!/usr/bin/env python

import os
import sys
import argparse

import files
import argparse_extras

def rename_argparse(rename_func, **kwargs):
    """Convenient standard command line interface to rename files.

    Renames using the given rename_func function.
    rename_func is expected to take a path, and return the new desired path

    Takes paths to rename from both stdin only, separated either by newline
    or null, depending on the null_terminated

    Empty paths are ignored

    Renaming functions acts as specified in files.rename_basenames.

    # kwargs

    all kwargs are passed to argpase.ArgumentParser constructor
    some of them are changed as follows:

    - epilog = kwargs.get('epilog',"") % {'f':os.path.basename(__file__)},
    - formatter_class=kwargs.get('formatter_class',argparse.RawTextHelpFormatter), #keep newlines

    - argparse_kwargs
        dict
        default={}
        kwargs for ArgumentParser constructor

    - encoding
        string
        default='UTF-8'
        encoding in assumed for paths from stdin
        and from command line arguments
        to decode with python string.decode() method

    #- func_extra_args
        #list
        #default=[]
        #args to be passed to rename_func in addition to the input path
        #mandatory argument
    """

    encoding = kwargs.get("encoding", 'UTF-8')
    kwargs['epilog'] = kwargs.get('epilog',"") % {'f':os.path.basename(sys.argv[0])}
    kwargs['formatter_class'] = kwargs.get('formatter_class',argparse.RawTextHelpFormatter)

    parser = argparse.ArgumentParser(**kwargs)

    argparse_extras.add_silent(parser)
    argparse_extras.add_not_dry_run(parser)
    argparse_extras.add_paths_from_stdin_and_argv(parser)

    args = parser.parse_args()

    not_dry_run = args.not_dry_run
    paths = argparse_extras.get_paths_from_stdin_and_argv(args)
    silent = args.silent

    files.rename_basenames(
                paths,
                rename_func,
                do_rename=not_dry_run,
                silent=silent
            )
