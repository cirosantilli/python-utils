#!/usr/bin/env python

import files
import argparse_extras

def rename_argparse(rename_func, **kwargs):
    """Convenient standard command line interface to rename files.

    will produce a command line of type:

    find . | CALLER_FILE_NAME [OPTIONAL_ARGUMENTS] [POSITOINAL_ARGUMENTS] [PATHS]

    maybe the best way to understand this is to look at the rename_basename* funcs on this module.

    Renames using the given rename_func function.
    rename_func is expected to take a path, and return the new desired path

    Takes paths to rename from both stdin and command line arguments, separated either by newline
    or null, depending on the -null-terminated option

    Empty paths are ignored

    Renaming functions acts as specified in files.rename_basenames.

    # kwargs

    - all kwargs accepted by argpase.ArgumentParser are passed to it
        but some of them are modified as follows specified by argparse_extras.ArgumentParser

    - encoding
        string
        default='utf8'
        encoding in assumed for paths from stdin
        and from command line arguments
        to decode with python string.decode() method

    - arg_adders
        [ lambda (argument_parser): ]
        adds arguments that will be passed to rename function
        cannot have variable number of elements since paths are already undefined in number
        arguments are added 
    
    - contoller
        lambda (args)

        takes args output by parser.parse_args(),

        and returns a pair ([func_args],{func_kwargs}) that will
        be passed as arguments of the rename function

        called controller because it takes user inputs and puts them on
        an adequate form to pass to the function

    #TODO
        - add kwarg that adds both ext only and bname only
    """

    add_act_noext_only = kwargs.pop("add_act_noext_only", False)
    add_act_basename_only = kwargs.pop("add_act_basename_only", True)
    encoding = kwargs.pop("encoding", 'UTF-8')
    func_arg_adders = kwargs.pop("func_arg_adders", [])
    func_arg_controller = kwargs.pop("func_arg_controller", lambda a: ([],{}) )

    parser = argparse_extras.ArgumentParser(**kwargs)

    argparse_extras.add_silent(parser)
    argparse_extras.add_not_dry_run(parser)
    argparse_extras.add_not_ignorecase(parser)
    if add_act_noext_only:
        argparse_extras.add_not_act_on_extension(parser)
    #TODO
    #if add_act_noext_only:
        #argparse_extras.add_act_on_basename_only(parser)
    argparse_extras.add_paths_from_stdin_and_argv(parser,before_paths_arg_adders=func_arg_adders)

    args = parser.parse_args()

    not_dry_run = args.not_dry_run
    paths = argparse_extras.get_paths_from_stdin_and_argv(args)
    silent = args.silent

    if add_act_noext_only and not args.act_on_extension:
        rename_func = files.act_noext_only(rename_func)

    func_args, func_kwargs = func_arg_controller(args)

    files.rename_basenames(
                paths,
                rename_func,
                func_args=func_args,
                func_kwargs=func_kwargs,
                do_rename=not_dry_run,
                silent=silent
            )
