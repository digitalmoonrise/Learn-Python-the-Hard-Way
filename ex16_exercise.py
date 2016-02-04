#ex 16 exercise

from sys import argv

script, filename = argv

newfile = open(filename, 'r')

print newfile.read()

newfile.close()