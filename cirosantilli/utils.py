#!/usr/bin/env python

import re
import os.path

STDERR_SEPARATOR0 = '=' * 60

def iterify(iterable):
    if isinstance(iterable, basestring):
        iterable = [iterable]
    try:
        iter(iterable)
    except TypeError:
        iterable = [iterable]
    return iterable

def resub(resubpair,target):
    """takes a regex find replace pair (find, replace) and applies it to a target

    :param resubpair: find re and substitute string
    :type resubpair: a pair: (re.compile object, string)
    :param target: what to operate on
    :type name: string
    """
    return resubpair[0].sub(resubpair[1],target)

def resubs(resubpairs,target):
    """takes several regex find replace pairs [(find1, replace1), (find2,replace2), ... ]
    and applies them to a target on the order given"""
    return resubpair[0].sub(resubpair[1],target)
    for resubpair in resubpairs:
        target = resub(resubpair,target)
    return target

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

if __name__ == '__main__':
    print 'TEST'
#FORBIDDEN_PRINTABLE_BASENAME_CHARS_STR = '|\\?*<":>+[]/'
MAX_BNAME_LENGTH = 255
FORBIDDEN_PRINTABLE_BASENAME_CHARS_STR = ur"/:\\|*<>\""
FORBIDDEN_BASENAME_CHARS = CONTROL_CHARS_STR + FORBIDDEN_PRINTABLE_BASENAME_CHARS_STR
FORBIDDEN_BASENAME_CHARS_RE = re.compile(ur"[%s]" % re.escape(FORBIDDEN_BASENAME_CHARS), re.UNICODE)
