#!/usr/bin/env python

import re
import os.path

def iterify(iterable):
    if isinstance(iterable, basestring):
        iterable = [iterable]
    try:
        iter(iterable)
    except TypeError:
        iterable = [iterable]
    return iterable

def resub(resubpair,target):
    return resubpair[0].sub(resubpair[1],target)

def resubs(resubpairs,target):
    for resubpair in resubpairs:
        target = resub(resubpair,target)

whitespaces_to_single_space_resub = [re.compile(r"\s+")," "]
def whitespaces_to_single_space(s):
    return resub(whitespaces_to_single_space_resub,s)

remove_heading_whitespace_resub = [re.compile(r"^\s+"),""]
def remove_heading_whitespace(s):
    return resub(whitespaces_to_single_space_resub,s)

remove_trailling_whitespace_resub = [re.compile(r"\s+$"),""]
def remove_trailling_whitespace(s):
    return resub(remove_trailling_whitespace_resub,s)

CONTROL_CHARS_STR = u''.join(map(unichr, range(0,32) + range(127,160)))
CONTROL_CHAR_RE = re.compile('[%s]' % re.escape(CONTROL_CHARS_STR), re.UNICODE)
def strip_control_chars(s):
    return CONTROL_CHAR_RE.sub(ur"", s)

#FORBIDDEN_PRINTABLE_BASENAME_CHARS_STR = '|\\?*<":>+[]/'
FORBIDDEN_PRINTABLE_BASENAME_CHARS_STR = ur"/:\\|*<>\""
FORBIDDEN_BASENAME_CHARS = CONTROL_CHARS_STR + FORBIDDEN_PRINTABLE_BASENAME_CHARS_STR
FORBIDDEN_BASENAME_CHARS_RE = re.compile(ur"[%s]" % re.escape(FORBIDDEN_BASENAME_CHARS), re.UNICODE)
def strip_basename_forbidden_chars(s):
    return FORBIDDEN_BASENAME_CHARS_RE.sub(ur"", s)

remove_heading_hyphen_whitespace = [re.compile(ur"^[-\s]+", re.UNICODE),""]
remove_trailling_dot_whitespace = [re.compile(ur"[\.\s]+$", re.UNICODE),""]
def nice_basename_stripped(bname):
    """
    Creates a nice and portable basename by simply stripping away bad things.

    If stripped things contain important data and you still need the portability,
    consider TODO
    """
    bname = strip_basename_forbidden_chars(bname)

    bname_noext, dotext = os.path.splitext(bname)
    
    bname_noext = resub(remove_heading_hyphen_whitespace,bname_noext)

    #bname_noext = resub(remove_trailling_dot_whitespace,bname_noext)
    bname_noext = remove_trailling_whitespace(bname_noext)

    bname_noext = whitespaces_to_single_space(bname_noext)

    return bname_noext + dotext

if __name__ == '__main__':
    print 'TEST'
