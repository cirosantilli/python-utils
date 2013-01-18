#!/usr/bin/env python

from cirosantilli import files
import argparse_extras
import logging

def git_mv(old,new):
    """git mv"""
    import subprocess

    commands = [
        'git',
        'mv',
        old,
        new
    ]
    process = subprocess.Popen(
        commands,
        shell=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return_code = process.wait()

def move_argparse(rename_func, **kwargs):
    """Convenient standard command line interface to rename files.

    will produce a command line of type:

    find . | CALLER_FILE_NAME [OPTIONAL_ARGUMENTS] [POSITOINAL_ARGUMENTS] [PATHS]

    maybe the best way to understand this is to look at the move* funcs on this module.

    Renames using the given rename_func function.
    rename_func is expected to take a path, and return the new desired path

    Takes paths to rename from both stdin and command line arguments, separated either by newline
    or null, depending on the -null-terminated option

    Empty paths are ignored

    Renaming functions acts as specified in files.moves.

    :param encoding:default='utf8'
        encoding in assumed for paths from stdin
        and from command line arguments
        to decode with python string.decode() method
    :type encoding: string

    :param arg_adders:
        [ lambda (argument_parser): ]
        adds arguments that will be passed to rename function
        cannot have variable number of elements since paths are already undefined in number
        arguments are added 
    
    :param contoller:
        lambda (args)

        takes args output by parser.parse_args(),

        and returns a pair ([func_args],{func_kwargs}) that will
        be passed as arguments of the rename function

        called controller because it takes user inputs and puts them on
        an adequate form to pass to the function

    :param add_act_noext_only: default: False
        
        if True, the option for the rename function
        to act on the path without extension is added to the command
        line interface and implemented
        
    :type add_act_noext_only: boolean.

    :param add_act_full_path: default: False
    
        if True, the option for the rename function
        to act on the entire path, not only basename as is default, is added to the command
        line interface and implemented

        

    :type add_act_full_path: boolean. 

    # kwargs

        all kwargs accepted by argpase.ArgumentParser are passed to it
        but some of them are modified as follows specified by argparse_extras.ArgumentParser

    todo
    ====
        - add kwarg that adds both ext only and bname only
    """

    add_act_noext_only = kwargs.pop("add_act_noext_only", None)
    add_act_full_path = kwargs.pop("add_act_full_path", None)
    add_input_full_path = kwargs.pop("add_input_full_path", None)

    encoding = kwargs.pop("encoding", 'UTF-8')
    func_arg_adders = kwargs.pop("func_arg_adders", [])
    func_arg_controller = kwargs.pop("func_arg_controller", lambda a: ([],{}) )

    parser = argparse_extras.ArgumentParser(**kwargs)

    argparse_extras.add_log_level(parser)
    argparse_extras.add_not_dry_run(parser)
    argparse_extras.add_not_ignorecase(parser)

    if add_act_noext_only:
        argparse_extras.add_not_act_on_extension(parser)
    if add_act_full_path:
        argparse_extras.add_act_full_path(parser)
    if add_input_full_path:
        argparse_extras.add_act_full_path(parser)

    argparse_extras.add_paths_from_stdin_and_argv(
        parser,
        before_paths_arg_adders=func_arg_adders
    )

    parser.add_argument(
        '-g',
        '--git-mv',
        action='store_true',
        default=False,
        help='if given does a git mv rename instead of normal rename',
    )

    args = parser.parse_args()

    paths = argparse_extras.get_paths_from_stdin_and_argv(args)

    if add_act_noext_only and not args.act_on_extension:
        rename_func = files.act_noext_only(rename_func)
    if add_act_full_path and not args.act_full_path:
        rename_func = files.act_basename_only(rename_func)

    logging.basicConfig(
        format='%(message)s',
        level=args.log_level,
    )

    move_kwargs = {}
    move_kwargs['do_move'] = args.not_dry_run
    move_kwargs['func_args'], move_kwargs['func_kwargs'] = func_arg_controller(args)
    if args.git_mv:
        move_kwargs['mv_func'] = git_mv

    files.move(
        paths,
        rename_func,
        **move_kwargs
    )
