PATH_TO_YOUR_AUTOKEY_LIB = "/usr/share/pyshared/autokey"

import sys
sys.path.append(PATH_TO_YOUR_AUTOKEY_LIB)

from configmanager import CONFIG_DEFAULT_FOLDER

import os

def _add_extension_to_json():
    """Updates .json files to contain the extension of corresponding .py of .txt files.
    Ex:

    1.json => 1.txt.json, if there is a 1.txt file in the same folder
	  => 1.py.json,    ""          1.py        ""

    This is used to avoid name conflicts if a script and a file with same name are created
    in the same folder.
    """
    for walkroot, dirs, files in os.walk(CONFIG_DEFAULT_FOLDER):
    	for json_name in files:
    	    (json_shortname, ext) = os.path.splitext(json_name) # .json
    	    if ext == '.json' and json_name != '.folder.json':
                json_path = os.path.join(walkroot,json_name)
                json_dir = os.path.dirname(json_path)
                data_path_noext = os.path.join(json_dir,json_shortname[1:]) # data file missing .txt or .py
                print json_path
                print data_path_noext
                if os.path.exists(data_path_noext + '.txt'):
                    data_ext = '.txt'
                elif os.path.exists(data_path_noext + '.py'):
                    data_ext = '.py'
                else:
                    raise Exception("Corrupted data, .json file: " + json_path + " has no corresponding .txt or .py file.")
                new_json_path = '.' + data_path_noext + '.py' + '.json'
                print json_path
                os.rename(json_path,new_json_path)

if __name__ == '__main__':
  _add_extension_to_json()