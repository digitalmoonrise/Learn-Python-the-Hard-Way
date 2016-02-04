# ex 11

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input() #make sure that i put my brackets in MIStAKE

print "So, you're %r old, %r tall, and %r heavy." % (age, height, weight)

print "What is your favorite game?"
game = raw_input()
print "How often do you play video games"
time = raw_input()*3  #it's not actually going to multiply the number because 
						#raw_input turns anything into a string. so we could 
						#probably use %s in our outputs? 

						#Yes, you can use %s insstead of %r

						#you can convert raw_input() into an integer by using
						# x = int(raw_input()) 

print "Don't lie to me! I know you play %s at least %s hours each week!" % (game, time)