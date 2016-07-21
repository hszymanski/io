#!/usr/bin/python

a = {"a":1, "d":4, "c":3, "e":5, "b":2, "j":10, "g":7, "f":6, "h":8, "i":9} 

for x in sorted(a):
    print x, "-", a[x]
