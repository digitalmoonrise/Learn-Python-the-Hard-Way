x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s."  % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'. " % y

hilarious = False

#so the sapce is the confusing thing here. when becaue it's reading and then puting the hilarious var. 
joke_evaluation = "Isn't that joke so funny!? %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e 


### ex. 7 more of the same

print "Mary had a little lamb"
print "It's fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 10 #put 10 periods? yes

end1 = "c"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "b"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print end1 + end2 + end3 + end4 + end5 + end6, #adding the coma makes two print statements stay on the same line. no comma moves to next line down. 
print end7 + end8 + end9 + end10 + end11 + end12
