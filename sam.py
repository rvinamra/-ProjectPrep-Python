ten_things = "Apples Oranges Crows Telephone Clouds Sugar"

print "Wait those are not 10 things, let's fix that"

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop(1)
	print "Adding: ", next_one 
	stuff.append(next_one)
	
print "There we go: ", stuff

print "Let's do somethings with stuff."

print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:6])