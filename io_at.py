#!/usr/bin/python3

file = open("file_x", 'a')
file.write("To jest druga linia tekstu/n")
file.close()

file = open("file_x", 'rt')
print(file.read())
file.close()
