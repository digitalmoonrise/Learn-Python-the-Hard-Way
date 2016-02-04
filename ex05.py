##exercise 5 strings!
my_name = "Conor M OBrien"
my_age = 28
my_height = 72 #inches
my_weight = 155 #lbs
my_eyes = "brown"
my_teeth = "should be whiter"
my_hair = "brown"
my_euro_height = my_height * 2.54

print "Let's talk about %s" % my_name 
print "He's %d inches tall" % my_height
print "He's %d pounds heavy" % my_weight
print "Actually, that's rather light!" 
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth %s but too much coffee" % (my_teeth)
print "If i was in europe i would be %r centimeters tall" % (my_euro_height)

#now i'm adding these vars because that's the assignment

print "If i add up %d, %d, and %d, I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
