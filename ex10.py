#ex 10

# \n brakes lines. 
# \ (backslash is essentially the same as regex where it escapes sequence)

print "I am 6'2\" tall."
print 'I am 6\'2" tall.'

tabby_cat = "\tI'm tabbed in."  #\t tabs
persian_cat = "I'm split\non a line" #error, forgot the n, but \n splits line
backslash_cat = "I'm \\ a \\ cat." #just exiting the backslash

#using the \t is tabbing in all the list items
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass 
"""
#interesting, now commenting with hash inside """, but you can use exits. 

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


#makes spinny little i, also crashes powershell
#while True:
	#for i in ["/","-","|","\\", "|"]:
	#	print "%s\r" % i, 