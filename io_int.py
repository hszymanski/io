#!/usr/bin/python3

import os.path

file = input("Podaj nazwe pliku: ")
if os.path.isfile(file):
    open_file = open(file, 'rt')
    print(open_file.read())
    open_file.close()
else:
    print("Nie ma takiego pliku")


