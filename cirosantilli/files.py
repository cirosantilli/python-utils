#!/usr/bin/env python
import os
import sys
import stat
import shutil
import ctypes
import logging

import utils

MBYTE = float(2**20)
def size_mb_str(path, decimals=2):
    """Returns the size of the file in path in megabytes as a string, with up to decimals
    decimal places.
    """
    return "{0:."+str(decimals)+"f}".format(os.path.getsize(path)/MBYTE)

KBYTE = float(2**10)
def size_kb_str(path, decimals=2):
    """Returns the size of the file in path in kbytes as a string, with up to decimals
    decimal places.
    """
    return "{0:."+str(decimals)+"f}".format(os.path.getsize(path)/KBYTE)

def act_noext_only(func):
    """decorator
    
    if f(path,*args,**kwargs) would act on the entire given path,
    to find a new name for it for example, it acts only the path without the extension
    """

    def wrapper(path,*args,**kwargs):
        path_noext,ext = os.path.splitext(path)
        new_path_noext = func(path_noext,*args,**kwargs)
        return new_path_noext + ext

    return wrapper

def act_basename_only(func):
    """decorator
    
    if f(path,*args,**kwargs) would act on the entire given path,
    to find a new name for it for example, it acts only on the basename
    """

    def wrapper(path,*args,**kwargs):
        head,bname = os.path.split(path)
        new_bname = func(bname,*args,**kwargs)
        return os.path.join(head,new_bname)

    return wrapper

def move(paths, rename_func, do_rename=False, **kwargs):
    """convenient interface for moving multiple paths

    rename func can takes the entire path, not only the basename,
    but it can only alter the basename only, and not the containing directory.

    files cannot change contaning directories after the rename.

    :param paths: paths to act on

        not an iterator, so that sorting can be done.

        relative paths are converted to full paths before rename_func acts on them

        rationale: absolute paths are taken even if only basebame can be renamed
        so that functions that use data inside the file can work. if you want
        to do a function that uses only basename information, use the act_basename_only
        decorator

    :type paths: list of strigs
    :param rename_func: rename function of  that returns the *basename* from the given *full path*
    :type rename_func: function with signature (string,*args,**kwargs)
    :param do_rename: if True, really renames, else, only outputs changes that would be done
    :type do_rename: boolean
    :param mv_func: if given, uses this function to rename files from old to new name. default: os.rename

        this function can suppose that:

        - the target parent directory exists
        - the target file does not exist

        it should throw any exception if the rename fails.

    :type mv_func: func(stringn,string). side effect: move old_path to new_path

    :param can_change_dirs: default: False
    
        if True, new path can be in a new dir from old one.
    
        else, if this is tried a warning is logged, and move is skipped

        example:

            old path:

                /usr/file.py

            new path:

                /home/file.py

            if True, the move works

    :type can_change_dirs: boolean
    :param make_missing_dirs: default: False
    
        if True, automatically makes any non existant directories that
        would be necessary for the new path.
        
        else, loggs a warning and skips current move

        this option implies can_change_dirs

        if a file is going to be moved to a different parent dir,
        and the parent dir is an existing file, only moves if overwrite == True
        and make_missing_dirs == True

        example:

            existing dirs:

                /usr/

            old path:

                /usr/file.py

            new path:

                /usr/non/existant/dirs/file.py

            if True, creates:

                /usr/non/
                /usr/non/existant/
                /usr/non/existant/dir/

            and then moves the old path there:

                /usr/non/existant/dir/file.py
                
    :type make_missing_dirs: boolean
    :param overwrite: default: False
    
        if True overwrites existing files without asking.

        else, logs a warning, and skips move

        if a file is going to be moved to a different parent dir,
        and the parent dir is an existing file, only moves if overwrite == True
        and make_missing_dirs == True

    :type overwrite: boolean.

    :param sort_func: default: sorted(reverse=True)

        function used to sort paths, and therefore decide order in which paths are renamed

        clearly, this function can have an impact on the rename results.

        example:

            existing files:

                /a
                /b

            rename func: lambda p: 'c'

            in this case, either a or b will be renamed,
            depending on which goes first.

            if overwrite is True, loss of data would occur

        rationale hehind default:

            with sorted(reverse=True), when renameing basenames, which is the major use case,
            one always renames parent dirs before files inside them.

    :type sort_func: function([string, ...])

    TODO
    ====

        - THE MOVE DIRS IS BUGGED DON'T USE IT!!!!!!

        - rename do_rename to do_mv

        - add act on abspath/act on relpath option

    """

    sort_func = kwargs.pop("sort_func", sorted)
    func_args = kwargs.pop("func_args", [])
    func_kwargs = kwargs.pop("func_kwargs", {})
    make_missing_dirs = kwargs.pop("make_missing_dirs", True)
    can_change_dirs = kwargs.pop("can_change_dirs", True) or make_missing_dirs
    mv_func = kwargs.pop("mv_func", os.rename)
    overwrite = kwargs.pop("overwrite", True)

    paths = map(os.path.abspath,paths)
    paths = sort_func(paths,reverse=True)
    warnings = []
    errors = []
    for path in paths:

        head, bname = os.path.split(path)
        new_bname = rename_func(path, *func_args, **func_kwargs)
        new_path = os.path.join(head, new_bname)

        if new_path != path:

            logging.info( "%s\n%s\n" % (path,new_path) )

            #make sure new path is clear
            if os.path.exists(new_path):
                if overwrite and do_rename:
                    if not os.path.isdir(new_dir): #its a file
                        if new_dir != old_path:
                            if overwrite:
                                shutil.rmtree(new_path)
                                os.mkdir(new_path)
                            else:
                                print overwrite_error
                        elif overwrite: #must move old path to temp path!
                            try:
                                os.move(path,tmppath)
                            except Exception,e:
                                errors.append( "TODO" % (path,new_path,e) )
                                continue
                            path = temppath
                    try:
                        shutil.rmtree(new_path)
                    except Exception,e:
                        errors.append(
                            "os error: could not remove existing path"
                            "\n%s\n%s\n\n%s" % (path,new_path,e) 
                        )
                        continue
                else:
                    warnings.append(
                            "new path already exists."
                            "rename skipped\nold path:"
                            "%s\nnew path:  %s" % (path, new_path) 
                    )
                    continue

            #make sure new dir exists
            old_dir = os.path.split(path)[0]
            new_dir = os.path.split(new_path)[0]
            if old_dir != new_dir:
                makedirs = False
                continue #TODO this is for security before I get the tests done!!!!!!
                if can_change_dirs:
                    if os.path.exists(new_dir):
                        if not os.path.isdir(new_dir): #its a file
                            if make_missing_dirs:
                                makedirs = True
                                if new_dir != old_path:
                                    if overwrite:
                                        try:
                                            shutil.rmtree(new_path)
                                        except Exception,e:
                                            print e, "TODO"
                                            continue
                                    else:
                                        print overwrite_error #TODO
                                elif overwrite: #new_dir == old_path: must move old path to temp path!
                                    #TODO get temppath
                                    try:
                                        os.move(path,tmppath)
                                    except Exception,e:
                                        errors.append( "TODO" % (path,new_path,e) )
                                        continue
                                    path = temppath
                            else:
                                print 'missing dirs warn TODO'
                    elif make_missing_dirs:
                        makedirs = True
                    else:
                        print 'missing dirs warn TODO'

                    #now that the are is clear, make the missing dirs if needed
                    if makedirs and do_rename:
                        try:
                            os.makedirs(new_dir) #ensure dir exists
                        except Exception,e:
                            errors.append( "os error: could not create non-existant dirs for new path. \n%s\n%s\n\n%s" % (path,new_path,e) )
                            continue
                    else:
                        warnings.append("new dir does not exist\n%s\n%s\n" % (path, new_path) )
                        continue
                else:
                    warnings.append("new path is in a different directory from old one. rename skipped\nold path:  %s\nnew path:  %s" % (path, new_path) )
                    continue

            if do_rename:
                try:
                    mv_func(path, new_path)
                except Exception,e:
                    errors.append( "os error: could not rename \n%s\n%s\n\n%s" % (path,new_path,e) )

    if warnings:
        logging.warning("WARNINGS")
        logging.warning("\n".join(warnings))
        logging.warning("END WARNINGS\n")
    if errors:
        logging.error("ERRORS")
        logging.error("\n".join(errors))
        logging.error("END ERRORS\n")

def find(root, **kwargs):
    """
    Recurses under the given root, and returns paths that match desired criteria.

    Examples:

    1)  def descend_func(p):
            # do not recurse into linux hidden dot files 
            return os.path.split(p)[1][0] != '.'

        for path in files.find('.',
            min_depth=2,
            max_depth=3,
            descend_func=descend_func ):

            if os.path.isfile(path) and os.path.splitext(path)[1] in ['.txt','.md']:
                print path

    2)  paths_list = [ p for p in find('.') ] 

    This basically adds a more convenient interface to find_rec by setting default values
    for kwargs, and the initial depth.

    @root: root under which recurstion will be done.

    # kwargs

    @max_depth. integer.
        default: float("inf")
        maximum depth to recurse.
        max_depth=1 searches current dir only.

    @min_depth. integer.
        default: 1
        minimum depth to recurse.
        min_depth=2 searches all dirs deeper than current one.

    @descend_func: function : str --> boolean.
        takes a directory path, and returns True iff the search
        should recurse under that directory.

    """

    #standard values for the kwargs
    kwargs = dict(
                [
                    ['min_depth',0],
                    ['max_depth',float("inf")],
                    ['descend_func',lambda p: True],
                ]
                + kwargs.items()
            )

    for path in find_rec(root,1,**kwargs):
        yield path

def find_rec(root, curdepth, **kwargs ):
    """
    Recursive depth first finding of files.

    For a convenient minimalist interface for this function, use find()

    The main design goal of this function is efficiency rather
    than interface convenience. As such:

    * only operations which may increase efficiency were implemented,
        notably by pruning parts of a tree (descend_function, avoids lots
        of useless compairisions),
        or by using values which are easily avalilable in the function
        but would be more expensive to calculate outside it (current depth
        which would require counting '/' or '\' in the path otherwise )
        
    * a generator expression is used to return values instead of a list.

        this means that vere little memory is used to loop over the search
        results, which should be the most common operation, since no complete
        search result list is stored.
    """

    try:
        os.listdir(root)
    except Exception, exc:
        sys.stderr.write(exc)
        yield

    descend_func = kwargs['descend_func']

    for relpath in os.listdir(root):

        path = os.path.join(root, relpath)

        if ( ( curdepth >= kwargs['min_depth'] ) ):
            yield path

        if ( os.path.isdir(path)
            and descend_func(path)
            and ( curdepth < kwargs['max_depth'] ) ):

            for path in find_rec(path,curdepth+1,**kwargs):
                yield path

def find_books(roots, **kwargs):

    for kwargs_key_def in kwargs_key_defs:
        key = kwargs_key_def[0]
        default = kwargs_key_def[1]
        kwargs[key] = kwargs.get(key, default)
    """
    Helper method to find books.
    """
    exts = ['pdf','djvu','djv','chm']
    for root in roots:
        for path in find(root, **kwargs):
            if ( os.path.isfile(path)
                    and extension(path) in exts ):
                yield path

def find_music(roots, **kwargs):
    """Helper method to find books."""
    exts = ['mp3','ogg','wma','flac']
    for root in roots:
        for path in find(root, **kwargs):
            if ( os.path.isfile(path)
                    and extension(path) in exts ):
                yield path
def split3(path):
    """ Returns a triplet parent_dir, basename wihout extension and extension with dot """
    parent_dir, bname = os.path.split(path)
    bname_noext, dotext = os.path.splitext(bname)
    return parent_dir, bname_noext, dotext

def inode(path):
    """ Returns inode of a given path. """
    return os.stat(path)[stat.ST_INO]

def write(path,input,**kwargs):
    """
    Saves input string to a given path.
    If the path already exists, it is overwritten.

    Examples:

    write("~/.asdf", "written to file")
    write("~/.asdf", "written to file", print_error=True)
    write("~/.asdf", "written to file", raise_exception=False, print_error=True)

    @print_error: boolean. If True, prints errors to stderr in case of exception.
        Exception itself is only printed if raise_exception is False.
        If it is True, it is left to the caller to print it if the wants.

    @raise_exception: boolean. If True, this function may raise an
    """

    print_error = kwargs.get('print_error', True)
    raise_exception = kwargs.get('raise_exception', True)

    had_exception = False
    try:
        f = open(path,'w')
        f.write(input)
        f.close()
    except Exception, exc:
        had_exception = True
        if print_error:
            sys.stderr.write( "could not write to path \n%s" % (output_path) )
            if not raise_exception:
                sys.stderr.write(str(err))
        if raise_exception:
            raise exc

    if had_exception:
        return False
    else:
        return True

def read(path,**kwargs):
    """
    Convenient wrapper that reads content from a path and returns it.

    Speed of the operation may be slightly compromised by a constant factor.
    It is the price to pay for the convenience, and ease of refactoring of using this method.

    Useful for one hit read of files that wont clutter the RAM memory.
    If its too big and you can do operations part by part, use a buffered reader instead.
    If it is too big, and you can't do operations part by part, ... there exists no solution for you!

    **kwargs:

    @print_error
    boolean
    true
    If true, will print a standardized error message on stderr in case of exception.

    @: boolean. If true, will print de

    """

    print_error = kwargs.get('print_error', True)
    raise_exception = kwargs.get('raise_exception', True)

    had_exception = False
    try:
        f = open(path,'r')
        output = f.read()
        f.close()
    except Exception, exc:
        had_exception = True
        if print_error:
            sys.stderr.write("could not read from\n%s\n" % (path) )
            if not raise_exception:
                sys.stderr.write(str(err))
        if raise_exception:
            raise exc

    if had_exception:
        return None
    else:
        return output

def remove_recursive(path):
    """
    If the path is a file, removes it
    If it is a directory, removes it recursivelly
    """
    if os.path.isfile(path):
        os.remove(path)
    else:
        shutil.rmtree(path)

def assert_file_exists(path, **kwargs):
    """
    Returns true iff path exists and is a file.

    If not, prints the appropriate error message to stderr (thus the report).
    """

    if not os.path.exists(path):
        sys.stderr.write("The path '" + input_path + "' does not exist.")
        return False
    if not os.path.isfile(path):
        sys.stderr.write("The path '" + input_path + "' is not a file.")
        return False
    return True

def write_basenames(paths,output_dir,**kwargs):
    """
    Quick write a find of basenames to a file. default separator: \n.
    """

    sep = kwargs.get('separator','\n')

    result = ""
    for path in paths:
        result += paths + sep
    write(output_dir,result)

def opt_ext(path_no_ext, ext, **kwargs):
    """
    If the path exists, returns it.
    If not, and if path + dotext exists, returns it.
    Else, returns None.

    kwargs:

    @print_error: boolean.
    If True, prints not found message to stderr in none is found.
    Default: False

    @opt_ext_on: boolean.
    If False, skips check .
    Default: False

    Sample call:

        prompt_user: opt_ext_on?
        input_path = files.opt_ext(input_path_opt_ext,'md', opt_ext_on=opt_ext_on, stderr=True)
        if not input_path:
            sys.stderr.write(input_path+"\nwas not converted.")
            has_error = True
    """

    print_error = kwargs.get('print_error',False)
    opt_ext_on = kwargs.get('opt_ext_on',True)

    # no extension
    if os.path.exists(path_no_ext):
        return path_no_ext

    # with extension
    path_ext = path_no_ext + '.' + ext
    if opt_ext_on and os.path.exists(path_ext):
        return path_ext

    # none found
    if print_error:
        sys.stderr.write("Neither path was found:\n"+path_no_ext+"\n"+path_ext)
    return None

def make_hardlinks(source_paths, destination_dir ):
    """ Makes hardlinks of all the source_paths in destination_dir with same name as the original source_path."""
    for source_path in source_paths:
        os.link(source_path, os.path.join(destination_dir, os.path.basename(source_path) ) )

def generate_test_output(curPath,suffix):
    """ Generates test output file in the same directory as the file curPath, using the same name as it + a given suffix """
    test_output_dir = os.path.dirname(curPath)
    test_output_name = os.path.splitext(os.path.basename(curPath))[0]+suffix+'.txt'
    test_output_path = os.path.join(test_output_dir,test_output_name)
    test_output = open(test_output_path ,'w')
    test_output.close()
    return open(test_output_path ,'a')

def is_hidden(filepath):
    """
    Returns if path is hidden or not.
    Works on linux, windows and mac.
    """
    name = os.path.basename(os.path.abspath(filepath))
    return name.startswith('.') or has_hidden_attribute(filepath)

def has_hidden_attribute(filepath):
    try:
        attrs = ctypes.windll.kernel32.GetFileAttributesW(unicode(filepath))
        assert attrs != -1
        result = bool(attrs & 2)
    except (AttributeError, AssertionError):
        result = False
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()

