import list_files
import os
import shutil

'''
Takes all files in the given directory path dir and puts them into
directories with the same name as the files, located in dir.

If path is not a directory, does nothing.
If directory already exists, puts the file into that directory

Sample call:
        put_all_files_in_dir_into_folders.put_all_files_in_dir_into_folders(dir_path,exts)
'''

def put_all_files_in_dir_into_folders(dir_path,exts):

        isdir, file_paths = list_files.list_files_with_extensions_in_dir(dir_path,exts)

        if isdir:
                for file_path in file_paths:
                        dir_name = os.path.splitext(os.path.split(file_path)[1])[0]
                        dir_path = os.path.join(os.path.split(file_path)[0],dir_name)
                        if not os.path.isdir(dir_path):
                                os.mkdir(dir_path)
                        shutil.move(file_path, dir_path)

        else:
                print "Given path is not a directory."
                 
                        




