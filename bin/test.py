#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def f(i):
    class C:
        class D:
            j=i
        D.k=i
    C.D.l=i
    return C()

c1 = f(1)
print c1.D.j
print c1.D.k
print c1.D.l
print f(2).D.j
print f(2).D.k
print f(2).D.l
print c1.D.j
print c1.D.k
print c1.D.l


#if __name__ == "__main__":

