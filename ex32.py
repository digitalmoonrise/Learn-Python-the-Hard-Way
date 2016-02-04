#31 actual

print 'You enter a dark room with two doors. do you go though door one or door 2?'

door = raw_input("> ")

if door == "1":
	print "theres a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the BEAST!"

	bear = raw_input("> ")

	if bear == "1":
		print "The bear eats you're fucking face!"
	elif bear == "2":
		print "the bear eats your fucking legs!!!"
	else:
		print "Well doing %s is probably better." % bear

elif door == "2":
	print "You stare into the endless abyss at Cthulu's anus."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins"
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input("> ")

	if insanity == "1" or insanity == "2":
		print "Your body survives but your mind is jello."
	else: 
		print "the insanity is too much, your eyes melt."

else:
	print "you stumble around and fall on a fucking knife and die."