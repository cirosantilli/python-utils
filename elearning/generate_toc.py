import os.path
from xml.parsers import expat
from xml.dom.minidom import parseString

input_dir = 'site-dev'
home_dir = os.path.dirname(os.path.dirname(__file__))
xml_path = os.path.join(home_dir,input_dir,'toc.xml')
html_path = os.path.join(home_dir,'nav-tree.html')
class_name = 'nav-tree'

#generates single toc.html file from toc.xml
class Parser:

    def __init__(self):
        self._parser = expat.ParserCreate()
        self._parser.StartElementHandler = self.start
        self._parser.EndElementHandler = self.end
        self._parser.CharacterDataHandler = self.data
	
	self._result = '<ul class="'+class_name+'">'

    def feed(self, data):
        self._parser.Parse(data, 0)

    #use obligatory to finish parsing
    def close(self):
        self._parser.Parse("", 1) # end of data
        del self._parser # get rid of circular references
	self._result += '</ul>'
	self._result = self._result.replace('<ul></ul>','')

    def start(self, tag, attrs):
	if(tag != 'root'):
	    id = attrs['id']
	    #decide title
	    if( 'title' in attrs ):
		title = attrs['title']
	    else:
		title = default_id_to_title(id)
	
	    #decide weather to publish or not
	    if(attrs['publish'] == 'true'):
		inner_li = '<a href="'+id+'">'+title+'</a>'
	    else:
		inner_li = title

	    self._result += '<li id="nav-tree-'+ id +'">'+inner_li+'<ul>'

    def data(self, data):
	    1

    def end(self, tag):
	if(tag != 'root'):
	    self._result += '</ul></li>'

    def result(self):
	return self._result

def default_id_to_title(id):
    id = id.split('/')[-1]
    return id[0].upper() + id[1:].replace('-',' ')

#open input file
file = open(xml_path,'r')
xml_data = file.read()
print 'Input:\n\n' + xml_data
file.close()

#parse and take output
p = Parser()
p.feed(xml_data)
p.close()
result = p.result()

pretty_result = parseString(result).toprettyxml()
print '\n\nOutput:\n\n' + pretty_result

#save output
file = open(html_path,'w')
file.write(result)
file.close()