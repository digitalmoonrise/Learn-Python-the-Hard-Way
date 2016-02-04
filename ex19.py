#ex19 

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % (cheese_count)
	print "You have %d boxes of crackers!" % (boxes_of_crackers)
	print "Man that's enough for a party"
	print "Go and get some blankets homie \n"

print "We can give the function numbers directly \n "

cheese_and_crackers(33, 7)

print "Or we can use variables from our script \n"
amount_of_cheese = 33
amount_of_crackers = 7

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print "WE can even do match inside too! \n"
cheese_and_crackers(10+7, 19-12)

print "And we can combine var and math! \n"

cheese_and_crackers(amount_of_cheese + 15, amount_of_crackers - 6)

#exercised

print "How many days of vacation have you taken?"
time_taken = input(">")
print "How many days per year do you have on vacation?"
time_available = input(">")

def vacation_days(x, y):
	print "if you have taken %r days" % (time_taken)
	print "and you have %r days avaialble..." % (time_available)


vacay = (time_available - time_taken)
print "Then you have %r days avaialble" % (vacay)