#exercise 16
#commands to remember
#close() closes a file
#read() reads a file, you can assign results to a var
#readline() reads just one line of a file
#truncate() empties a file, be careful
#write('stuff') writes stuff to a file 

# it is called a 'parameter' when you fill the '()' after a commands

from sys import argv

script, filename = argv

print "We're going to erase %r" % filename
print "If you don't want that hit ctrl + C "
print "If you're ok with that, hit enter!!!!" 

raw_input("?")

print "Opening the file %r" % filename
target = open(filename, 'w')

print "Truncating the file: %r" % filename
target.truncate() 

print "Now I'm going to ask you for three lines:"
line1 = raw_input("line one: ")
line2 = raw_input("line two: ")
line3 = raw_input("line three: ")

print "Now let's write these mother fuckers to a file!"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3) 
target.write("\n")


print "And now we close that shit down"

target.close() 

