#exercise 15
#This is going to import from the computer what we tell it
#importing a module sys is a package
from sys import argv

#we are definiting the argument, the strings we need to run the prgm
script, filename = argv

#defining the text var and actually giving it an action w the open() cmd
txt = open(filename)

#user input
print "Here's your file: %r!" % filename

#using the read() to print the file onto the screen
print txt.read()

#doing the same thing as above
print "type the filename again, punk:"
file_again = raw_input(">") 

txt_again = open(file_again)

print txt_again.read() 

txt.close()

print "That's all folks"

