import list_files

'''
Replaces all the ocorrunces of replace_dictionary[0] for replace_dictionary[1]
in all the subfiles of path with one of the extensions extensions.
'''

def replace_in_files_full_tree(path,replace_dictionary,extensions):

        path_exists, file_paths = list_files.list_files_with_extensions_full_tree(path,extensions)

        if path_exists:
                for file_path in file_paths:
                        s = open(file_path).read()
                        for entry in replace_dictionary:
                                s = s.replace(entry[0],entry[1])
                        f = open ( file_path, 'w' )
                        f.write(s)
                        f.close

        else:
                print 'The path:\n\n' + path + '\n\ndoes not exist.'
                raw_input("Click to exit.")
