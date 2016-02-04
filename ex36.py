#ex 36
#if your the else clause of your if statement never executes, then you
##need to use die()

#never nest if statement more than two deep and try and only do one deep
#most times, you should use a for loop, almost never use a while loop

#burls world
from sys import exit

def dead(x):
	print x, "You lose!"
	exit(0)

def win(x):
	print x, "You win! You'll never be worried again!"
	exit(0)

def living_room():
	print "\n\tYou walk into the living room and you see a comfy couch"
	print "\n\tYou also see some shiny equipment that you don't know what it does"
	print "\n\tWhat are you thinking about doing?"

	living_choice = raw_input("> ")

	if "eat" in living_choice:
		print dead("Oh you know you shouldn't have! You can't eat conor and shiela's things!")
	elif "couch" in living_choice:
		treat()
	elif "equipment" in living_choice:
		print dead("Mother fucker! conor is going to send you back to the pen!")
	else:
		print dead("I don't know what you're thinking, but i'm sure it isn't good")



def kitchen():
	print "kitchen"

def treat():
	print "Are you going to sit?"



print """\nConor and Sheila just left the house.
You're all alone and you don't know woof to do. """

print "\nAre you thinking about causing trouble?"

trouble = raw_input("> ")

if trouble == "yes":
	print dead("You know that's a bad idea! Conor is going to git you!")
elif trouble == "no":
	print "that's a good choice! Do you want to go into the kitchen or living room?"
else:
	print dead("What the hell are you talking about!")

room = raw_input("> ")
#go into kitchen or living room
if room == "living room":
	living_room()
elif room == "kitchen":
	kitchen()
else:
	print dead("WTF DAWG!")


#kitchen()
#garbage_can

