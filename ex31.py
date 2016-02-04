#ex 31

hairs = ['brown', 'blond', 'red']
eyes = ['brown', 'blue', 'green']
weights = [1,2,3,4]

the_count = [1,2,3,4,5]
fruits = ['apple', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for-loop goes through a list
for number in the_count:
	print "This count is %d" % number 

#same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit

#also, we can go through mixed lists
#notice we have to use %r since we don't know what's in it

for i in change:
	print "I got %r" % i 

#we can also build lists, start w an empty oranges

elements = []

#then use the range function to do 0 to 5 counts
for i in range(0,6):  #range only adds from the first to last, and not including the last
	print "Adding %d to the list" % i 
	#append is a function that lists understand
	elements.append(i)

#now we can print the elements too
for i in elements:
	print "Element was: %d" % i 

print "fart"

## you can also avoid the for loop entirely by just 
###using append in the case of elements. 
turd = []

p = range(4)

turd.append(p)

print turd

#other things you can do with lists
#list.append() #adds an item to the end of a list
#list.extend() combines two lists?
#list.instert #inserts and item at a given position
#list.remove()
#list.pop()
#list.index()
#list.count()
#list.sort()
#list.reverse()