

def jar(x, z):
	i = 0
	numbers = []
	while  x > i:
		print "At the top i is %d" % i
		numbers.append(i)

		i = i + z
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

	print "The numbers: %r " % numbers

print jar(10,2)

print "\n \tThis is Exercise 2"
def case(s,st):
	rng = range(0,s,st) # have to use 0 as the start
	for i in rng:
		print "The number is %d" % i 
		print rng

print case(10, 2)

#ex34
#1 python
#2 peacock
#3 bear
#4 kangaroo
#5 whale
#6 peacock
#7 platypus
#8 whale

