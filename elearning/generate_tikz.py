'''
by Ciro D. Santilli 29/01/2012
'''

import os
import os.path
import subprocess
import files

#- file path parameters ------------------------------------------------------------#
root = os.path.dirname(os.path.dirname(__file__))
input_dir = "site-dev/tikz_code"
pdf_path = "intermediate_outputs"
output_dir = "uploads"
inkscape = 'C:/Program Files (x86)/Inkscape/inkscape.exe'
extension = '.tex'
output_format = 'svg'

#- file names without extension -#
file_names = [
"2-sat-to-graph-example-2"
];

#- what goes before the tex file -#
pre_tex = r"""
\documentclass{article}
\usepackage{amsthm}

\usepackage[pdftex,active,tightpage]{preview}

% for Tikz
\usepackage[version=0.96]{pgf}
\usepackage{tikz}
\usetikzlibrary{arrows,shapes,automata}
\usepackage[latin1]{inputenc}

%------------------------------------------------------------------------------%
\begin{document}
\begin{preview}
"""

#- what goes after the tex file -#
post_tex = r"""
\end{preview}
\end{document}
"""

for file_name in file_names:
    input_path = os.path.join( root, input_dir, file_name + extension)
    pdf_dir = os.path.join( root, input_dir, pdf_path)
    full_tex_path = os.path.join( pdf_dir, file_name+'.tex')
    pdf_path = os.path.join( pdf_dir, file_name+'.pdf' )
    output_path = os.path.join( root, output_dir, file_name+'.svg')
    
    #- open original file -#
    file = open(input_path,'r')
    input = file.read()
    file.close()
    
    #- append and save full tex file -#
    file = open(full_tex_path,'w')
    file.write(pre_tex + input + post_tex)
    file.close()
    
    subprocess.call(['pdflatex',full_tex_path,'--output-directory='+pdf_dir])	#- make pdf -#
    subprocess.call([inkscape,pdf_path,'--export-plain-svg='+output_path])	#- use Inkscape to transform pdf->svg -#
    
exists, paths = files.list(pdf_dir,exts=[],files=1,dirs=0,fulltree=0)
for path in paths:
#    print path
    os.remove(path)
