#ex35

from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"

	choice = raw_input("> ")
	if choice != int:
		dead("That's wrong")
	else:
		how_much = int(choice)

	if how_much < 50:
		print "Nice, you're not greedy. WIN"
		exit(0)

	else:
		dead("You greedy bastard!")

def bear_room():
	print "theres a bear in here!"
	print "The bear has a bunch of honey"
	print "The fat bear is in front of another door"
	print "how are you going to move the bear?"
	bear_moved = False 

	while True:
		choice = raw_input("> ")

		if choice == "take honey":
			dead("the bear looks at you then slaps your deadick off!")
		elif choice == "taunt bear" and not bear_moved:
			#essentially saying not false
			print "The bear has moved from the door. you may open the door"

			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			dead("bear eats yer leg")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means!"

def cthulhu_room():
	print "here you see the evil cthulhu"
	print "He, it, whatever stares at you and you go insane!"
	print "Do you flee for your life or eat your head?"

	choice = raw_input("> ")

	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("I guess you won't be getting 'A head'")
	else:
		cthulhu_room()

def dead(why):
	print why, "Good job, deadman!"
	exit(0)

def start():
	print "You are in a dark room."
	print "There is a door on your right and left"
	print "which one do you take?"

	choice = raw_input("> ")

	if "right" in choice:
		cthulhu_room()
	elif "left" in choice:
		bear_room()
	else:
		dead("you indecisive fool!")

start()
