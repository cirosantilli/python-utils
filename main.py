import runpy
import os.path
import files as fileOps
	
run_name = '__main__'

run_paths = [] #stores the paths that will be actually run relative to this file

python = [os.path.dirname(__file__),[

#     'scrap_paper'

#-- from current dir --------------------------------------------------------
#    'rename_files_in_folder',
#    'netbeans_code_templates_export_to_js_code_completion',
#    'text_processing/latex_define_to_mathjax_define'
   'books_management'
#    
    
]]
run_paths += ( fileOps.join_paths(python[0],python[1]) )

#- from elearning ------------------------------------------------------------#
elearning = ['C:/xampp/htdocs/elearning/site-core/',[
#    'generate_tocs',
#    'generate_toc'
#    'generate_plots',
#    'generate_tikz',
#    'xml_to_txt_db',
	# 'wiki_markup_conversion'
	# 'wp_markup_conversion'
#    'test_markup_conversion'
]]
run_paths += ( fileOps.join_paths(elearning[0],elearning[1]) )

#- from root ------------------------------------------------------------#
root = [
#    'C:/xampp/htdocs/elearning/contents-wp/de-macro'
#    'C:/Users/Ciro/Documents/backup/noshare/x/3A/EA Automatique/Code/simulation_real_real'
#    'C:/simulation_real_real'
]
run_paths += root



#run everything
for file_path in run_paths:
    runpy.run_path( file_path +	 '.py', run_name=run_name )




