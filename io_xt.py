#!/usr/bin/python3

file = open("file_x", 'xt')
file.write("To jest pierwsza linia tekstu\n")
file.close()
try:
    file = open("file_x", 'rt')
    print(file.read())
    file.close()
except:
    print("Brak pliku file_x")
    
