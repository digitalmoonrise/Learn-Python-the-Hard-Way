#exercise 14
from sys import argv

script, user_name = argv  #adding the second. essentially with this we are creating a username and password
								#field. the username shows up, but the password never does, unless we added it
								#to the % ().

prompt = '>' #prompt is a variable that we can re use with all of our other variables 
				#we don't have to keep typing it out. if you put in a string, that's what it will paste
				# before every answer. 
				
script = 'fart' #if you leave script blank it will give you the script, but you can also assign it as a var

print "Hi %s, I'm the %s script" % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me, %s" % (user_name)
likes = raw_input(prompt)

print "Where do you live, %s?" % (user_name)
lives = raw_input(prompt)

print "What kind of computer do you have, %s?" %(user_name)
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. I'm not sure where that is. 
And you have %r computer. Nice.
""" % (likes, lives, computer)





