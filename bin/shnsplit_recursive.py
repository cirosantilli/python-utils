#!/usr/bin/env python

#!dependencies=['sudo apt-get install shntool']

import sys    
import os
import os.path
import subprocess
import argparse
from argparse import RawTextHelpFormatter

import files

AUDIO_EXTS = ['ape', 'flac']

if __name__ == '__main__':

    f = os.path.basename(__file__)
    parser = argparse.ArgumentParser(description=r"""Wrapper for shnsplit, that allows for recursive operation.

Always overwrites existing files.

INSTALLATION

INSTALL_PATH=~/bin/ #or somewhere else in your PATH

sudo apt-get install shntool

mkdir -p "$INSTALL_PATH"
cd "$INSTALL_PATH"
wget -nc https://raw.github.com/cirosantilli/python/master/shnsplit_recursive.py 
chmod +x shnsplit_recursive.py
wget -nc https://raw.github.com/cirosantilli/python/master/files.py 

SAMPLE CALLS

shnsplit_recursive.py -o flac -t '%n - %p - %t' -R

  Finds all cue files under current directory.
  If in the same directory as them there is a single file
  with a splittable audio extension and with the same basename as the cue,
  tries to split it with shnsplit
    -o: converting output to flac
    -t: using the filename format '%n - %p - %t' (as described in shntool)
    -R: remove cue and audio file after successful conversion
""",
    formatter_class=RawTextHelpFormatter,
    prog=f,
    )

    parser.add_argument('-o', '--output_format',
        help="Ouptut format. Same as shnsplit -o",
        default="flac")

    parser.add_argument('-R', '--remove_original_files',
        action="store_true", 
        default=False, 
        help="Remove original files after successful split. Default False.")

    parser.add_argument('-t', '--output_filename_format',
        help="Ouptut filename format. Same as shnsplit -t. Default '%%n - %%p - %%t'",
        default="%n - %p - %t")

    args = parser.parse_args(sys.argv[1:])
    output_format = args.output_format
    remove_original_files = args.remove_original_files
    output_filename_format = args.output_filename_format

    errors = []

    for cue_path in files.find(u'.'):

        if cue_path.endswith('.cue'):

            parent_dir, cue_bname_noext, dotext = files.split3(cue_path)

            def accept(path):
                parent_dir, bname_noext, dotext = files.split3(path)
                return bname_noext == cue_bname_noext and dotext[1:] in AUDIO_EXTS

            audio_file_candidates = filter(accept, os.listdir(parent_dir))

            ncandidates = len(audio_file_candidates)

            if ncandidates == 0: #only one candidate, so take him!
                error = "No audio candidates for:\n%s" % cue_path
                print error
                errors.append(error)

            elif ncandidates > 1:
                error = "More than a single candidate for:\n%s\nCandidates are:\n%s" % cue_path, "\n".join(audio_file_candidates)
                print error
                errors.append(error)

            else: #only one candidate, so take him!
                audio_file = os.path.join(parent_dir, audio_file_candidates[0])
                print "Splitting pair"
                print cue_path
                print audio_file

                #commands=['shntool', 'split', '-O', 'never', '-f', cue_path, '-d', parent_dir, '-o', output_format, audio_file, '-t', output_filename_format]
                commands=['shntool', 'split', '-O', 'always', '-f', cue_path, '-d', parent_dir, '-o', output_format, audio_file, '-t', output_filename_format]
                process = subprocess.Popen(commands, shell=False)
                return_code = process.wait() # waits for process to end

                if return_code == 1: #a problem happened!
                    error = "Could not split:\n%s" % cue_path
                    print error
                    errors.append(error)
                else:
                    print "Split successful"
                    if remove_original_files:
                        print "Removing cue and original audio file."
                        os.remove(cue_path)
                        os.remove(audio_file)

            print

    if errors:
        print "#------------------------------------------------------------#"
        print "ERRORS OCCURRED:"
        print
        print "\n\n".join(errors)
