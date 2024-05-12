#!/usr/bin/env python

def mysum(L):
    return L[0] if len(L)==1 else L[0]+ mysum(L[1:])

mysum([1, 3, 4, 5])


