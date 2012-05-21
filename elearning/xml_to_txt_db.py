import os.path
from xml.parsers import expat

home_dir = os.path.dirname(os.path.dirname(__file__))
xml_path = os.path.join(home_dir,'toc.xml')
output_path = os.path.join(os.path.dirname(__file__),'database.txt')

field_separator = '\t|\t' #separes fields of the database a | b \n c | n \n
entry_separator = '\n' #separes entries of the db
fields = ['id','title','publish','children']

class Parser:

    def __init__(self):
        self._parser = expat.ParserCreate()
        self._parser.StartElementHandler = self.start
        self._parser.EndElementHandler = self.end
        self._parser.CharacterDataHandler = self.data
	self._result = ''

    def feed(self, data):
        self._parser.Parse(data, 0)

    #use obligatory to do end parsing activities
    def close(self):
        self._parser.Parse("", 1) # end of data
        del self._parser # get rid of circular references
	
	#sort output
	sorted_result = sorted(self._result.split(entry_separator))[1:]
	self._result = ''
	for res in sorted_result:
	    self._result += res + entry_separator
	    
	#add field name line
	field_name_line = ''
	for field in fields[0:len(fields)-1]: #-1 because after last no separator
	    field_name_line += field + field_separator
	field_name_line += fields[-1] + entry_separator 
	self._result = field_name_line + self._result
	

    def start(self, tag, attrs):
	id = str(attrs['id'])
	if( 'title' in attrs ):
	    title = attrs['title']
	else:
	    title = default_id_to_title(id)
        self._result += id + field_separator + title + field_separator + attrs['publish'] + entry_separator

    def data(self, data):
	1

    def end(self, tag):
	1

    def result(self):
	return self._result
    
def default_id_to_title(id):
    id = id.split('/')[-1]
    return id[0].upper() + id[1:].replace('_',' ')

#open input file
file = open(xml_path,'r')
xml_data = file.read()
file.close()

#parse and take output
p = Parser()
p.feed(xml_data)
p.close()
result = p.result()

print result

#save output
file = open(output_path,'w')
file.write(result)
file.close()