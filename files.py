import os.path
import stat
import shutil
import ctypes

import utils

MBYTE = float(2**20)
def size_mb_str(path, decimals=2):
    """
    Returns the size of the file in path in megabytes as a string, with up to decimals
    decimal places.
    """
    return "{0:."+str(decimals)+"f}".format(os.path.getsize(path)/MBYTE)

KBYTE = float(2**10)
def size_kb_str(path, decimals=2):
    """
    Returns the size of the file in path in kbytes as a string, with up to decimals
    decimal places.
    """
    return "{0:."+str(decimals)+"f}".format(os.path.getsize(path)/KBYTE)

def join_paths(parent_path, children_paths):
    """
    given a parent_path and children_paths returns
    the array result of os.path.join parent_path to all children_paths
    """
    result = []
    for child_path in children_paths:
        result.append(os.path.join(parent_path,child_path))
    return result

def rename_basenames(paths, rename_func, do_rename=False, **kwargs):
    """
    Convenient interface for renaming multiple paths.

    Rename func can takes the entire path, not only the basename,
    but it can only alter the basename only, and not the containing directory.

    kwargs

    * act_on_basename_only
    Boolean
    If true, rename_func takes the basename only, ommiting the parent path.

    * act_on_extension
    Boolean
    If true, rename_func takes the extension.
    """

    act_basename_only = kwargs.get("act_basename_only", False)
    act_on_extension = kwargs.get("act_on_extension", True)

    paths.sort(reverse=True) # so that dirs get renamed after the paths they contain

    has_error = False
    for path in paths:

        # decide where to act on
        if act_basename_only:
            head, bname = os.path.split(path)
            if act_on_extension:
                new_bname = rename_func(bname)
                new_path = os.path.join(head, new_bname)
            else:
                bname_noext, dotext = os.path.splitext(bname)
                new_bname_noext = rename_func(bname_noext)
                new_path = os.path.join(head, new_bname_noext + dotext)
        else: # act on entire path
            if act_on_extension:
                new_path = rename_func(path)
            else:
                path_noext, dotext = os.path.splitext(bname)
                new_path_noext = rename_func(path_noext)
                new_path = new_path_noext + dotext

        if new_path != path:
            print path
            print new_path
            if os.path.exists(new_path):
                has_error = True
                print "New path already exists. Rename skipped.\n"
            elif os.path.split(path)[0] != os.path.split(new_path)[0]:
                has_error = True
                print "New path is in a different dir. Rename skipped.\n"
            else:
                if do_rename:
                    os.rename(path, new_path)
            print

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

    **kwargs

    @max_depth. integer.
        maximum depth to recurse.
        max_depth=1 searches current dir only.

    @min_depth. integer.
        minimum depth to recurse.
        min_depth=2 searches all dirs deeper than current one.

    @descend_func: function : str --> boolean.
        takes a directory path, and returns True iff the search
        should recurse under that directory.

    """

    #standard values for the kwargs
    kwargs_key_defs = [['min_depth',0],
            ['max_depth',float("inf")],
            ['descend_func',lambda p: True],
            ]

    for kwargs_key_def in kwargs_key_defs:
        key = kwargs_key_def[0]
        default = kwargs_key_def[1]
        kwargs[key] = kwargs.get(key, default)

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
    """
    Helper method to find books.
    """
    exts = ['mp3','ogg','wma','flac']
    for root in roots:
        for path in find(root, **kwargs):
            if ( os.path.isfile(path)
                    and extension(path) in exts ):
                yield path

def parent_dir(path):
    """ Returns full path of parent directory. """
    return os.path.dirname(path)

def basename(path):
    """ Returns basename. """
    return os.path.splitext(path)[1]

def basename_no_ext(path):
    """ Returns basename wihout extension (no dot '.' either) """
    (shortname, ext) = os.path.splitext(os.path.basename(path))
    return shortname;

def split3(path):
    """ Returns a triplet parent_dir, basename wihout extension and extension with dot """
    parent_dir, bname = os.path.split(path)
    bname_noext, dotext = os.path.splitext(bname)
    return parent_dir, bname_noext, dotext

def path_no_ext(path):
    """ Returns path without file extension (no dot '.' either) """
    return os.path.join(parent_dir(path), basename_no_ext(path))

def extension_no_dot(path):
    """ Returns file extension without dot of a given path. """
    return os.path.splitext(path)[1][1:]

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
            sys.stderr.write("could not read from\n%s\n" % (output_path) )
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
