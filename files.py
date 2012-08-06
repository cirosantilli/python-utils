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

def rename(paths, rename_func, **kwargs):
    """
    renames all files in paths according to the renaming function rename_func(str)
    extension is ignored

    kwargs: test. Default: True. if test is True, does not rename, only prints new names and existing names conflicts

    Example call: make function, select files, and rename them all!
    def rename_func(input):

        #mathematics book case
        regex = '^Mathematics - (Book|E-book) - '
        if(re.match(regex,input)):
        return re.sub(regex,'',input)

        #123 - case
        regex = '^\d\d\d - '
        if(re.match(regex,input)):
        return re.sub(regex,'',input)

        #none of the above
        return input

    #path = 'C:/Users/Ciro/Documents/backup/noshare/programs/python/tests/rename/'
    path = 'C:/Users/Ciro/Documents/backup/share/Texts/Mathematics'
    exts = ['pdf','djvu']

    paths = files.list_files_with_extensions_full_tree(path,exts)
    files.rename( paths, rename_func )
    """

    dry_run = kwargs.get('dry_run',True)
    include_extension = kwargs.get('include_extension',False)

    has_error = False

    for path in paths:

        head, bname = os.path.split(path)

        if include_extension:
            new_bname = rename(bname)
        else:
            bname_noext, ext = os.path.splitext(bname)
            new_bname = rename(bname_noext) + ext

        new_path = os.path.join(head, new_bname)

        # act on differences only
        if new_path != path:
            print path
            print new_path
            if not os.path.exists(new_path):
                if not dry_run:
                    os.rename(path, new_path)
            else:
                has_error = True
                print new_path + " already exists.\n"
            print

def rename_unidecode(paths, kwargs):

    from unidecode_wrap import unidecode_wrap

    rename(paths, unicode_wrap,**kwargs)

def change_ext(paths, rename_func):
    """

    Example call:

    def rename(ext):
        return 'xml'

    exists, the_files = files.find(r'C: ampp\htdocs\elearning\articles',exts=['html'],files=1,dirs=0,recurse=0) DO NOT PUT A slash XXXXXX or it does not work the import!!!
    files.change_ext(the_files,rename)
    """
    for path in paths:
        if(os.path.isfile(path)):
            (shortname, ext) = os.path.splitext(os.path.basename(path)) #get name no extension
            new_name = shortname + '.' + rename_func(ext[1:])    #- remove '.' -#
            new_path = os.path.join(os.path.dirname(path),new_name)

        #    print new_path
            if new_path != path:
                if(not os.path.exists(new_path)):
                    os.rename(path, new_path)
                else:
                    print new_path + " already exists.\n"
            else:
                print 'Not a file'

FIND_SORT_NONE = 'n'
FIND_SORT_DIRECT = 'd'
FIND_SORT_REVERSE = 'r'

#def find(roots, **kwargs):
    #"""
    #Implements similar functionality to Linux bash find.

    #Finds paths under given directory that satisfy certain criteria.

    #@root a list of strings containing the paths of the roots for find search.

    #If the given path exists, and is a directory, returns True.
    #Else returns false (False,[]).

    #@exts a list of strings. If given, only searches for
    #paths with one of the given extensions (given without the point).
    #If not given, searches for all paths, including those without extenstion.

    #@param d, f, df or fd: if 'd' is present, includes
    #directory in search, if 'f' is present, includes files in search

    #@inodes: a list of integers. If given selects only files
    #with one of the given inodes. Else inodes are ignored.

    #@return: pair (boolean b,string list l). b is true iff the root path exists
    #and is a directory.

    #@dirs: boolean. Selects directories iff True.

    #@files: boolean. Selects files iff True.

    #@recurse: boolean. If true, descends tree.

    #@sort: char. sorting method for output. can take values

        #* FIND_SORT_NONE : no sorting
        #* FIND_SORT_DIRECT : direct order sorting
        #* FIND_SORT_REVERSE : reverse order sorting

    #Other values will raise an exception.

    #Default: 'r', because in reverse orther, deeper paths come first, so that
    #you can rename files and the directories that contain them in one go.

    #l contains the a list of selected paths if any.

    #Sample call:

    #exists, file_paths = files.find(r'./',
        #dirs=True,
        #files=True,
        #exts=['mp3','ogg'],
        #recurse=False,
        #inodes=[411580,411581])

    #"""

    #bname_match_re = kwargs.get('bname_match_re',None)
    #roots = utils.iterify(roots)
    #select_dirs = kwargs.get('dirs',True)
    #select_files = kwargs.get('files',True)
    #recurse = kwargs.get('recurse',True)
    #exts = utils.iterify(kwargs.get('exts',[]))
    #inodes = utils.iterify(kwargs.get('inodes',[]))
    #sort_method = kwargs.get('sort',FIND_SORT_REVERSE) # reverse, so that deeper paths come first and directories can be renamed

    #dotexts = [ '.'+ext for ext in exts ]

    #all_exist = True
    #output_paths = []
    #for root in roots:

        #if(os.path.isfile(root)): #a file
            #dotext = os.path.splitext(root)[1]
            #if exts == [] or os.path.splitext(root)[1] in dotexts:
                #output_paths.append(path)

        #else: #a directory
            #result = []
            #if(recurse): #full tree
                #for walkroot, dirs, files in os.walk(root):
                    #if(select_dirs):
                        #result.extend([os.path.join(walkroot,dir) for dir in dirs])
                    #if(select_files):
                        #result.extend([os.path.join(walkroot,file) for file in files if
                                    #( exts == [] or os.path.splitext(file)[1] in dotexts)
                                    #and ( inodes == [] or inode(path) in inodes )
                                    #and ( bname_match_re == None or bname_match_re.match() )
                                    #])
                #output_paths.extend(result)

            #else: #just the current dir
                #names = os.listdir(root)
                #paths = [ os.path.join(root,name) for name in names ]
                #output_paths.extend([path for path in paths if (
                    #( (select_files and os.path.isfile(path)
                    #and (exts == [] or os.path.splitext(path)[1] in dotexts))
                    #and ( inodes == [] or inoded(path) in inodes ) )
                    #or (select_dirs and os.path.isdir(path))) ])

    ## sort output.
    #if output_paths:
        #if sort_method  == FIND_SORT_REVERSE:
            #output_paths.sort()
        #elif sort_method == FIND_SORT_DIRECT:
            #output_paths.sort(reverse=True)
        #elif sort_method == FIND_SORT_NONE:
            #1
        #else:
            #has_commandline_error = True
            #raise Exception("Invalid sort method value: "+sort_method)

    #return output_paths

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

#def find_rec(root, curdepth, exceptions_str, **kwargs ):
    #"""
    #Recursive depth first finding of files.
    #"""

    #try:
        #os.listdir(root)
    #except Exception, exc:
        #sys.stderr.write(exc)
        #return

    #select_func = kwargs['select_func']
    #descend_func = kwargs['prune_func']

    #output_paths = []
    #for relpath in os.listdir(root):

        #path = os.path.join(root, relpath)

        #if ( ( curdepth >= kwargs['min_depth'] ) ):

            #output_paths.append(path)

        #if ( os.path.isdir(path)
            #and not prune_func(path)
            #and ( curdepth < kwargs['max_depth'] ) ):

            #output_paths.extend(find_rec(path,curdepth+1,**kwargs))

    #return output_paths

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

def find_wrap(roots, **kwargs):
    """
    Convenient interface for find, with many common find criteria implemented.

    All the given criteria are 'anded'. If you want a 'or', then you must implement
    this functionnality in with func.

    This function has a constant overhead with respect to find, since the
    select function and descend functions are compiled at runtime in order
    to minimize the number of useless comparisons per file.

    @root a list of strings containing the paths of the roots for find search.

    If the given path exists, and is a directory, returns True.
    Else returns false (False,[]).

    @exts a list of strings. If given, only searches for
    paths with one of the given extensions (given without the point).
    If not given, searches for all paths, including those without extenstion.

    @param d, f, df or fd: if 'd' is present, includes
    directory in search, if 'f' is present, includes files in search

    @inodes: a list of integers. If given selects only files
    with one of the given inodes. Else inodes are ignored.

    @return: pair (boolean b,string list l). b is true iff the root path exists
    and is a directory.

    @dirs: boolean. Selects directories iff True.

    @files: boolean. Selects files iff True.

    @recurse: boolean. If true, descends tree.

    @sort: char. sorting method for output. can take values

        * FIND_SORT_NONE : no sorting
        * FIND_SORT_DIRECT : direct order sorting
        * FIND_SORT_REVERSE : reverse order sorting

    Other values will raise an exception.

    Default: 'r', because in reverse orther, deeper paths come first, so that
    you can rename files and the directories that contain them in one go.

    l contains the a list of selected paths if any.

    Sample call:

    exists, file_paths = files.find(r'./',
        dirs=True,
        files=True,
        exts=['mp3','ogg'],
        inodes=[411580,411581])

    """
    roots = utils.iterify(roots)

    #default values for the kwargs
    kwargs_key_defs = [['bname_match_re',None],
            ['dirs',True],
            ['files',True],
            ['exts',None],
            ['not_exts',None],
            ['sort',FIND_SORT_REVERSE],
            ['inodes',None],
            ['not_inodes',None],
            ['sha1s',None],
            ['not_sha1s',None],
            ['min_depth',0],
            ['max_depth',float("inf")],
            ['hidden',True],
            ['not_hidden',True],
            ['bname_contain',None],
            ['not_bname_contain',None],
            ['not_bname_match_res',None],
            ['bname_noext_match_res',None],
            ['not_bname_noext_match_res',None],
            ['select_func',lambda p: True],
            ['prune_hidden',False],
            ['prune_not_hidden',False],
            ['prune_bname_contains',None],
            ['prune_bname_not_contains',None],
            ['prune_bname_match_res',None],
            ['prune_not_bname_match_res',None],
            ['prune_func',lambda p: True],
            ]

    for kwargs_key_def in kwargs_key_defs:
        key = kwargs_key_def[0]
        default = kwargs_key_def[1]
        kwargs[key] = kwargs.get(key, default)

    #make sure you havel lists
    exts = utils.iterify(kwargs['exts'])
    kwargs['dotexts'] = [ '.'+ext for ext in exts ]
    kwargs['inodes'] = utils.iterify(kwargs['inodes'])

    #build and compile the final function to avoid a huge number of useless comparisons
    #for each path. this is useful if the number of paths is large, otherwise the
    #compilation overhead is not worth it.
    func_def = "def func(p,**kwargs):\n if "
    if not kwargs['dirs']:
        func_def += "not os.path.isdir(p) and "
    if not kwargs['files']:
        func_def += "not os.path.isfile(p) and "
    if kwargs['exts']:
        func_def += "os.path.splitext(p)[1][1:] in kwargs['exts'] and "
    if kwargs['not_exts']:
        func_def += "not os.path.splitext(p)[1][1:] in kwargs['not_exts'] and "
    if kwargs['inodes']:
        func_def += "files.inode(p) in kwargs['inodes'] and "
    if kwargs['not_inodes']:
        func_def += "not files.inode(p) in kwargs['inodes'] and "
    func_def = func_def[:-4]
    func_def += ":\n  return True\n return False"
    print func_def
    exec func_def in globals() # defines the function
    kwargs['func'] = func

    # main loop
    output_paths = []
    for root in roots:
        output_paths.extend(find_rec(root,1,**kwargs))
        
    # sort output.
    sort_method = kwargs['sort']
    if output_paths:
        if sort_method == FIND_SORT_DIRECT:
            output_paths.sort()
        elif sort_method == FIND_SORT_REVERSE:
            output_paths.sort(reverse=True)
        elif sort_method == FIND_SORT_NONE:
            1
        else:
            has_commandline_error = True
            raise Exception("Invalid sort method value: "+sort_method)

    return output_paths

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

def path_no_ext(path):
    """ Returns path without file extension (no dot '.' either) """
    return os.path.join(parent_dir(path), basename_no_ext(path))

def extension(path):
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

    @print_error: boolean. If True, prints errors to stderr in case of exception. Exception itself is only printed if raise_exception is False. If it is True, it is left to the caller to print it if the wants.

    @raise_exception: boolean. If True, this function may raise an
    """

    print_error = kwargs.get('print_error', False)
    raise_exception = kwargs.get('raise_exception', True)

    had_exception = False
    try:
        f = open(path,'w')
        f.write(input)
        f.close()
    except Exception, exc:
        had_exception = True
        if print_error:
            sys.stderr.write( "Could not write the output to path \n%s" % (output_path) )
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

    print_error = kwargs.get('print_error', False)
    raise_exception = kwargs.get('raise_exception', True)

    had_exception = False
    try:
        f = open(path,'r')
        output = f.read()
        f.close()
    except Exception, exc:
        had_exception = True
        if print_error:
            sys.stderr.write("Error occurred when writting to\n%s\n" % (output_path) )
            if not raise_exception:
                sys.stderr.write(str(err))
        if raise_exception:
            raise exc

    if had_exception:
        return None
    else:
        return output

def remove(path):
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

def  generate_test_output(curPath,suffix):
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
