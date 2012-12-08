from cirosantilli import files
import os
import re

def uppercase_to_underline_lowercase_pathnames(path, extensions):
    """
    Transforms all uppercase path basenames in a tree with top at path, into underline lowercase
    name standard.

    Examples:

    AnUppercaseStandardSubfolder -> an_uppercase_standard_subfolder
    AnUppercaseStandardTXTFile.TXT -> an_uppercase_standard_t_x_t_file.TXT

    Notice that the first character is always minuscule, and that extensions are not altered.
    """
    path_exists, file_paths = files.files_with_extensions_full_tree(path,extensions)
    path_exists, dir_paths = files.list_directories_full_tree(path,False)

    if path_exists:
            rename_dictionary = []

            # do the files
            for file_path in file_paths:
                    basename = os.path.basename(file_path)
                    (shortname, ext) = os.path.splitext(basename) 
                    new_shortname = to_underline_lowercase(shortname)
                    new_base_name = new_shortname + ext
                    rename_dictionary.append([shortname,new_shortname])
                    os.rename(file_path, os.path.join(os.path.dirname(file_path),new_base_name))

            # do the directories
            for dir_path in dir_paths:
                    basename = os.path.basename(dir_path)
                    new_base_name = to_underline_lowercase(basename)
                    rename_dictionary.append([basename,new_base_name])
                    os.rename(dir_path, os.path.join(os.path.dirname(dir_path),new_base_name))   
    else:
            print 'The path:\n\n' + path + '\n\ndoes not exist.'
            raw_input("Click to exit.")

#TODO: this is not changing the last Uppercase letter of a name AAA -> a_aA 
def to_underline_lowercase(str):

        offset = 0
        new_str = str
        for i in range(1,len(str)-1):
                if str[i].isupper():
                        new_str = new_str[:(i+offset)] + '_' + str[i].lower() + new_str[(i+1+offset):]
                        offset = offset + 1
                        
        return new_str[0].lower() + new_str[1:]










