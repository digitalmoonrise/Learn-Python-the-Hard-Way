formatter = "%r %r %r %r" #four different vars to print

print formatter % (1,2,3,4)
print formatter % ("One","two","three", "four")
print formatter % (True, False, False, True)
print formatter % (
	"I hat this thing",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said Goodnight!")

## essentially we just have the %r because we are using both
## strings and integers. We'd use %s for strings and %d for 
## integers. All of these have 4  

## exercise 9

days = "Mon Tue Wed Thu Fri Sat Sun" 

# \n is newline -- cannot use /n, has to be \n
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "here are the days", days
print "Here are the months", months

print """
There's something going on here. 
With the three double quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5 or 6.
"""
#"""work as text box. also it breaks lines. not just wall of text


