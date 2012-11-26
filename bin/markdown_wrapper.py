#!/usr/bin/env python

#------------------------------------------------------------
#
# Ciro D. Santilli 
#
# A wrapper to markdown that tweaks the its interface to suit
# my preferred defaults better and add some more simple interface
# fonctionnality.
#
# DEPENDENCIES:
#
#   - markdown
#   
#   sudo apt-get install markdown
#
# TODO:
#
#   -o --output-path output path. Hard because of conflict with multiple input files.
#   -s --silent. Do not print error messages.
#   
#   factor this out as a module
#------------------------------------------------------------

if __name__ == '__main__':
    """
    Test:
    
        mkdir markdown
        cd markdown
        
        echo -e "#With extension\n\nPar 1\n\nPar 2" > test.md
        
        markdown_wrapper.py -E test # not found
        
        #1 auto extension adding
        echo -e "#Without extension\n\nPar 1\n\nPar 2" > test
        markdown_wrapper.py test
        firefox test.html # should show with ext file
        
        markdown_wrapper.py test
        firefox test.html # should show no ext file.
        #1 interactive overwrite
        markdown_wrapper.py -i test.md
        firefox test.html # should show ext file
        
        #1 multiple files conversion
        echo -e "#Without extension 2\n\nPar 1\n\nPar 2" > test2
        markdown_wrapper.py -i test test.md test2
        
    """
  
    import os
    import sys
    import subprocess
    import argparse
    import shutil
    
    from cirosantilli import files
    import ui
    
    parser = argparse.ArgumentParser(description="Wrapper for markdown that improves its command-line interface",)
        
    parser.add_argument('-i', '--interactive', 
        dest='interactive', 
        action='store_true', 
        default=False,
        help="If specified, user is prompted before overwriting existing output .html file. If False, overwrites the output path, weather it is a directory of a file without notification. False by default.")
    
    parser.add_argument('-E', '--opt-ext-off', 
        dest='opt_ext_off',
        action="store_true",
        default=False,
        help='Stops trying to convert input_paths_opt_ext.md if input_paths_opt_ext does not exist.')
    
    parser.add_argument('input_paths_opt_ext', 
        nargs='+',
        help='Input paths to markdown files to be converted.'
            +'If a path does not exist, also tries to convert input_paths_opt_ext.md file.'
            +'To turn off this behaviour see the -G option.')

    args = parser.parse_args()
    interactive = args.interactive
    opt_ext_on = not args.opt_ext_off
    input_paths_opt_ext = args.input_paths_opt_ext
    
    # do the convertions and save the results
    has_error = False
    for input_path_opt_ext in input_paths_opt_ext:
        
        # check that the input path exists
        input_path = files.opt_ext(input_path_opt_ext, 'md', 
            opt_ext_on=opt_ext_on,
            print_error=True)
        if not input_path:
            sys.stderr.write("%s\nwas not converted." % (input_path) )
            has_error = True
            break
        
        # get the input out of the input path
        input = files.read(input_path, print_error=True, raise_exception=False)
        if input == None: # could not read.
            sys.stderr.write(input_path+"\nwas not converted.")
            has_error = True
            break
        
        # first make sure the conversion can be performed
        # before doing any other possible costly or dangerous
        # (removing paths) operations
        try:
            output = subprocess.check_output(['markdown', input_path])
        except Exception, err:
            sys.stderr.write(input_path+"\n could not be converted. Markdown retuned:\n"+str(err))
            has_error = True
            break
        
        output_path = files.path_no_ext(input_path) + '.html'
        
        # ensure that the output path is clear and clear it if not.
        # prompts the user if in interactive mode
        if os.path.exists(output_path):
            if interactive:
                prompt = ("%s\nalready exists and must be removed to save the output of \n%s\nRemove\n%s\nand continue?") % (output_path, input_path, output_path)
                if not ui.prompt_yes_no(prompt): # user did not want to remove
                    sys.stderr.write("Conversion of \n"+input_path+"\n cancelled by user because the output path already exists.")
                    break
            files.remove(output_path)

        # write the output to the output_path
        if not files.write(output_path, output, print_error=True, raise_exception=False): # could not write
            sys.stderr.write("Conversion of \n%s\n was aborted, and if the output path \n%s\n existed it was removed." % (input_path, output_path))
            has_error = True
            break
    
    # return error code if at least one error happened
    if has_error:
        sys.exit(1)
    else:
        sys.exit(0)




