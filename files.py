import os.path
import stat
import shutil

import utils

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

    exists, paths = files.list_files_with_extensions_full_tree(path,exts)
    files.rename( paths, rename_func )
    """

    extension is ignored

    if('test' in kwargs):
        test = kwargs['test']
    else:
        test = True        # default to true for safety

    if('test_output_to_file' in kwargs):
        test_output_to_file = kwargs['test_output_to_file']
    else:
        test_output_to_file = ""

    for path in paths:
        if(os.path.isfile(path)):
            (shortname, ext) = os.path.splitext(os.path.basename(path)) #get name no extension
            new_base_name = rename_func(shortname) + ext
        else:
            new_base_name = rename_func(os.path.basename(path))
        new_path = os.path.join(os.path.dirname(path),new_base_name)

    #    print new_path
        if new_path != path:
            if(not os.path.exists(new_path)):
                if(test):
                    print new_path
                else:
                    if os.path.exists(path):
                        os.rename(path, new_path)
                    else:
                        print path + "does not exist.\n"
            else:
                print new_path + " already exists.\n"

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

def find(roots, **kwargs):
    """
    Implements similar functionality to Linux bash find.

    Finds paths under given directory that satisfy certain criteria.

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
        recurse=False,
        inodes=[411580,411581])

    """

    roots = utils.iterify(roots)
    select_dirs = kwargs.get('dirs',True)
    select_files = kwargs.get('files',True)
    recurse = kwargs.get('recurse',True)
    exts = utils.iterify(kwargs.get('exts',[]))
    inodes = utils.iterify(kwargs.get('inodes',[]))
    sort_method = kwargs.get('sort',FIND_SORT_REVERSE) # reverse, so that deeper paths come first and directories can be renamed

    dotexts = [ '.'+ext for ext in exts ]

    all_exist = True
    output_paths = []
    for root in roots:

        if(os.path.isfile(root)): #a file
            dotext = os.path.splitext(root)[1]
            if exts == [] or os.path.splitext(root)[1] in dotexts:
                output_paths.append(path)

        else: #a directory
            result = []
            if(recurse): #full tree
                for walkroot, dirs, files in os.walk(root):
                    if(select_dirs):
                        result.extend([os.path.join(walkroot,dir) for dir in dirs])
                    if(select_files):
                        result.extend([os.path.join(walkroot,file) for file in files if
                                    ( exts == [] or os.path.splitext(file)[1] in dotexts)
                                    and ( inodes == [] or inode(path) in inodes )
                                    ])
                output_paths.extend(result)

            else: #just the current dir
                names = os.listdir(root)
                paths = [ os.path.join(root,name) for name in names ]
                output_paths.extend([path for path in paths if (
                    ( (select_files and os.path.isfile(path)
                    and (exts == [] or os.path.splitext(path)[1] in dotexts))
                    and ( inodes == [] or inoded(path) in inodes ) )
                    or (select_dirs and os.path.isdir(path))) ])

    # sort output.
    if output_paths:
        if sort_method  == FIND_SORT_REVERSE:
            output_paths.sort()
        elif sort_method == FIND_SORT_DIRECT:
            output_paths.sort(reverse=True)
        elif sort_method == FIND_SORT_NONE:
            1
        else:
            has_commandline_error = True
            raise Exception("Invalid sort method value: "+sort_method)

    return output_paths

def find_books(roots, **kwargs):
    """
    Convenience method to find books fulltree.
    """
    return find(roots,exts=['pdf','djvu','djv','chm'],files=1,dirs=0)

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
    """ Returns file extension with dot of a given path. """
    (shortname, ext) = os.path.splitext(os.path.basename(path))
    return ext;

def inode(path):
    """ Returns inode of a given path. """
    return os.stat(path)[stat.ST_INO]

def write(path,input,**kwargs):
    """
    Saves input string to a given path.
    If the path already exists, it is overwritten.

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
    Reads path and returns content of file.

    Useful for one hit read of files that wont clutter the RAM memory.
    If its too big use a buffered reader instead.

    **kwargs:

    @print_error: boolean. If true, will print de

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
            sys.stderr.write("Could not write the output to path \n%s" % (output_path) )
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

def assert_file_exists_report(path):
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
