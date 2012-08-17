#!/usr/bin/env python

import re
import os.path
import subprocess

import utils
from rename_argparse import rename_argparse

def extract_field_from_id3tool_out(id3tool_out, field_id):
    """
    Extracts a field from the id3tool output.
    """
    m = re.search(r'^'+field_id+r':\s*(.*)$', id3tool_out, re.MULTILINE)
    if m:
        return m.group(1)
    else:
        return None

def id3_to_basename(path):

    process = subprocess.Popen(['id3tool', path], shell=False,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    id3tool_out, stderr = process.communicate()

    track = extract_field_from_id3tool_out(id3tool_out,"Track")
    artist = extract_field_from_id3tool_out(id3tool_out,"Artist")
    title = extract_field_from_id3tool_out(id3tool_out,"Song Title")
    year = extract_field_from_id3tool_out(id3tool_out,"Year")

    head, bname = os.path.split(path)
    bname_noext, dotext = os.path.splitext(bname)

    #bname_noext = " - ".join(filter(lambda p: p, [track, artist, title])) # if something is missing, remove it, and join with " - "
    if track:
        bname_noext = track + " - " + bname_noext

    bname_noext = utils.whitespaces_to_single_space(bname_noext)
    bname_noext = utils.remove_trailling_whitespace(bname_noext)
    bname_noext = utils.remove_heading_whitespace(bname_noext)

    return os.path.join(head, bname_noext + dotext)

if __name__ == '__main__':

    rename_argparse(id3_to_basename, description="""Command line interface for renaming using id3 tags.

Open up this file and modify id3_to_basename function if you want a custom rename.
Someday this will be implemented as parsing of a simple format string.

DEPENDENCIES

    id3tool

EXAMPLE

    find subdir -iname '*.mp3' -print0 | rename_basename_id3tags.py path1 path2 0
    #will rename basename of mp3s inside subdir tree and of path1 and path2 (but not of their subtrees)
    
    find-music . | rename_basename_id3tags.py 1
    #finds all music nul separated, and renames with id3 tags
""")
