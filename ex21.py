#ex 21

def add(a,b):
	print "adding %d and %d" % (a, b)
	return a + b

def subtract(a,b):
	print "subtracting %d and %d" % (a, b)
	return a - b

def multiply(a,b):
	print "multiplying %d and %d" % (a, b)
	return a * b

def divide(a,b):
	print "dividing %d and %d" % (a, b)
	return a / b 



age = add(22,6)
height = subtract(80,8)
weight = multiply(75,2)
iq = divide(200,2)

print "Age: %d\n Height:%d\n Weight:%d\n IQ:%d" % (age, height, weight, iq)

print "here is a puzzle!"

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print "That becomes:", what, "Can you do it by hand?"