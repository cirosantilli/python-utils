# this file contains short calls or pieces of them that I used and which might me useful in the future, specially when I did not implement them into functions.

#- if name main
if __name__ == '__main__':
    print "TEST"

#- mathematics file listing ------------------------------------------------------------#
root = r'C:\Users\Ciro\Documents\backup\share\Texts\Mathematics - Copie'
exists, dirs = fileOps.list(root,exts=[],files=0,dirs=1,fulltree=0)
for dir in dirs:
	exists, files = fileOps.list(dir,exts=['pdf','djvu'],files=1,dirs=0,fulltree=0)
	result = ""
	for file in files:
		result += os.path.basename(file) + "\n"
	fileOps.write(os.path.join(root,dir + '.txt'),result)
	
#- split first names (if any)from last name ------------------------------------------------------------#
namere = re.compile('(.*\s|)(.+)')

#- transform all , beefore first - into ; ------------------------------------------------------------#
r = re.compile(r'^.*?-')
def replace_func_r( match ):
    result = match.group()
    result = result.replace(',',';')
    return result

#- regex rename. remove trailing zeroes ------------------------------------------------------------#
import re
import files as fileOps

p = re.compile(r'\d+$')
def rfunc( match ):
	result = match.group()
	return result[1:]

def rename_func(input):
	return p.sub(rfunc,input)
	
root = r'C:\Users\Ciro\Documents\backup\noshare\x\3A\Constraint Programming\Project\instances'
exists, dirs = fileOps.list(root,exts=[],files=0,dirs=1,fulltree=0)
for dir in dirs:
	exists, files = fileOps.list(dir,exts=['cnf'],files=1,dirs=0,fulltree=0)
	fileOps.rename(files,rename_func,test=False)
	
import re

#- regex rename. remove trailing zeroes ------------------------------------------------------------#
#- REMEMBER: match mateches only at the begening!!! search looks for the first match, searchall and finditer find all. -#
def rename_func(input):
	return p.search(input).group()
	
root = r'C:\Users\Ciro\Documents\backup\noshare\x\3A\Constraint Programming\Project\instances'
exists, dirs = fileOps.list(root,exts=[],files=0,dirs=1,fulltree=0)
for dir in dirs:
	exists, files = fileOps.list(dir,exts=['cnf'],files=1,dirs=0,fulltree=0)
	fileOps.rename(files,rename_func,test=False)
	
#-  ------------------------------------------------------------#
import re
	
p = re.compile(r'\([^)]*\)')
def rfunc( match ):
	return match.group().replace('-',',')

def rename_func(input):
	return p.sub(rfunc,input)
	
exists, dirs = fileOps.list(root,exts=[],files=0,dirs=1,fulltree=1)
root = r'C:\Users\Ciro\Documents\backup\share\Texts\Physics'
for dir in dirs:
	exists, files = fileOps.list(dir,exts=[],files=1,dirs=0,fulltree=0)
	fileOps.rename(files,rename_func,test=False)
#- mathematics books management ------------------------------------------------------------#
# Takes file name listings in different files, makes a subdirectory for each filename listing with the same name as the txt file, then puts all files listed in the directory.

import shutil

mathematics = r'C:\Users\Ciro\Documents\backup\share\Texts\Mathematics'
categories = os.path.join(mathematics,'Categories')

exists, paths = fileOps.list(categories,exts=['txt'],files=1,dirs=0,fulltree=1)
for path in paths:

	topicDir = os.path.join(fileOps.parent_dir(path),fileOps.name_noext(path))
	# print os.path.join(fileOps.parent_dir(path),fileOps.name_noext(path))
	# os.makedirs(topic_dir)
	
	txt = fileOps.read(path)
	names = txt.split('\n')
	for name in names:
		if not name == '':
			src = os.path.join(mathematics,name)
			if not os.path.exists(src):
				dst = os.path.join(topicDir,name)
				shutil.move(src, dst)