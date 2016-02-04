#ex18

#this one is like your scripts with argv
def print_2(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

#ok, that args was actually pointless. instead, we can do this
def print_2_again (arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

#this just takes one argument
def print_one_argument(arg1):
		print "arg1: %r" % (arg1)

def print_none():
	print "I \n got \n nothin" 

print_2("conor", "obrien")
print_2_again("conor", "obrien")
print_one_argument("conor")
print_none()