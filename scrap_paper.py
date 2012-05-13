n: '\\mathbb{N}',
z: '\\mathbb{Z}',
q: '\\mathbb{Q}',
r: '\\mathbb{R}',
c: '\\mathbb{C}',

inf: '\\infty', //infty is too long. appears too often. no conflicts I can see for the shortcut. I have to change the standard here... Come on Latex...

//-- logic operators --//,  
or: '\\text{ or }',
and: '\\text{ and }',
iff: '\\leftrightarrow',
implies: '\\rightarrow',

//-- limits --//,
fromto: '\\rightarrow',
tendsto: '\\longrightarrow',
nottendto: '\\nrightarrow',

//-- functions --//,
funcdom: ['#1 \\colon #2 \\to #3', 3],
funcdef: ['\\begin{align} #1 \\colon #2 & \\rightarrow #3 \\nonumber \\\\ #4 & \\mapsto #5 \\end{align}', 5], //name, domain, image, element of domain, what happens to it

der: ['\\frac{d#1}{d#2}', 2], //-- derivative --//
parder: ['\\frac{\\partial #1}{\\partial #2 }', 2],

proj: ['proj_{#1}', 1],
measure: ['meas(#1)', 1],

vnorm: ['\\left|\\left| #1\\right|\\right|', 1], //-- vector norm --//
vnormone: ['{\\left|\\left| #1\\right|\\right|}_1', 1],
vnormtwo: ['{\\left|\\left| #1\\right|\\right|}_2', 1],
vnormsup: ['{\\left|\\left| #1\\right|\\right|}_\\infty', 1],
opnorm: ['{\\left|\\left| #1\\right|\\right|_{op}}', 1], 

indqx: '\\mathbf{1}_{\\Q}(x)',
indq: ['\\mathbf{1}_{\\Q}(#1)', 1],

//-- physics --//,
vbar: '\\overline{v}',

//-- misc --//,
xb: '\\mathbf{x}',
dxb: '\\mathbf{dx}',
fb: '\\mathbf{f}'