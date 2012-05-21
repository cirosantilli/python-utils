    #Manipulate files in my film folder
parent = 'F:/Videos 16-04-2011/Films'
output = os.path.join(os.path.dirname(parent),'films db.txt')
sep = [" - ","/t"]
r = re.compile('^(.*) - (.*) - (.*)$')
namere = re.compile('(.*\s|)(.+)')

exists, paths = files.list_dirs_in_dir(parent)
result = ["",""]
for path in paths:
    basename = os.path.basename(path)
    m = r.match(basename)
    if(m):
	director = m.group(1)
	year = m.group(2)
	title = m.group(3)
	result[1] += director + sep[1] + title + sep[1] + year + '\n'

print result[1]

file = open(output,'w')
file.write(result[1])
file.close()