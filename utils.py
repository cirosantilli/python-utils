#!/usr/bin/env python

def iterify(iterable):
    if isinstance(iterable, basestring):
        iterable = [iterable]
    try:
        iter(iterable)
    except TypeError:
        iterable = [iterable]
    return iterable

if __name__ == '__main__':
    print 'TEST'
