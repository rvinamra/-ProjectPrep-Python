the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears']
change = [1, 'pennies', 2, 'dimes']

for number in the_count:
	print "The count is %d" %number
	
for fruit in fruits:
	print "A fruit of type %s" %fruit
	
for i in change:
	print "I got %r" %i
	
elements = []

for i in range(0, 6):
	print "Adding %d to the list." %i
	elements.append(i)
	
lis = [[1, 2, 3],[4, 5, 6], [6, 7, 8, 9]]
for j in lis:
	print "Now up is %r" %j