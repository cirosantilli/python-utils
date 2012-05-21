import os.path
from xml.dom.minidom import parse

home_dir = os.path.dirname(os.path.dirname(__file__)) #elearning/
html_path = os.path.join(home_dir,'toc.html') #elearning/toc.html
tocs_root_rel_path = 'sidebars'
tocs_path = os.path.join(home_dir,tocs_root_rel_path) #elearning/tocs partial tocs home
class_name = 'nav_tree'

#takes full tree html and generates partial tocs with breadcrumbs in #elearning/tocs dir
def generate_partial_tocs(html_path,tocs_path):
    root = parse(html_path)
    remove_whilespace_nodes(root,True) #simpler without beautification blank
    lis = root.getElementsByTagName('li')
    for li in lis:
	anc = li.childNodes[0]
	if(anc.nodeType == anc.ELEMENT_NODE and anc.localName == "a"):
	    id = anc.attributes["href"].value[1:]
	    print '<ul class="'+class_name+'">' + li_ascendants(root,li) + li.toxml() + '</ul>'

#lists ascendants list link up to root.
def li_ascendants(root,li):
    result = ''
    print 'NODE:\n\n' + li.toxml() + '\n\n'
    li.childNodes[0]
    ul = li.parentNode
    while(not ul is root):
	li = ul.parentNode
	result += li.childNodes[0].toxml() # should add the hole
	ul = li.parentNode
    return result

#to simplify tasks
def remove_whilespace_nodes(node, unlink=False):
    """Removes all of the whitespace-only text decendants of a DOM node.
    
    When creating a DOM from an XML source, XML parsers are required to
    consider several conditions when deciding whether to include
    whitespace-only text nodes. This function ignores all of those
    conditions and removes all whitespace-only text decendants of the
    specified node. If the unlink flag is specified, the removed text
    nodes are unlinked so that their storage can be reclaimed. If the
    specified node is a whitespace-only text node then it is left
    unmodified."""
    
    remove_list = []
    for child in node.childNodes:
        if child.nodeType == child.TEXT_NODE and \
           not child.data.strip():
            remove_list.append(child)
        elif child.hasChildNodes():
            remove_whilespace_nodes(child, unlink)
    for node in remove_list:
        node.parentNode.removeChild(node)
        if unlink:
            node.unlink()
    
if __name__ == '__main__':
    generate_partial_tocs(html_path,tocs_path)