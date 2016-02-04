#exercise 13
 

##packages in python are called "MODULES"

first = raw_input("When was your first kiss?")
second = raw_input("Who was your second grade teacher?")
third = raw_input("Have you ever had a threesome?")

#this is how you import packages into python. 
from sys import argv #argv is argument variable -- standard language

script, first, second, third = argv

print "This is your butt", script #so script is just the script path
print "The first kiss is:", first
print "Your second grade teacher is:", second
print "You've had a threesome?", third

#Why am i getting the error message when I don't unpack the argv
	#i'm guessing that it assumes one if i don't put any, and if i put
	#one it will give me how many i need. 

#MODULES MODULES MODULES they give you features. 

##When writing a script with raw_input, is there a way to have those
#raw input become the cmd line argv?

