states = { 
	'Oregon': 'OR',
	'Florida': 'FL', 
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'}
	
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print '-'*10
print "Michigan has: ", cities[states['Michigan']]

print '-'*10
for state, abbrev in states.items():
	print "%s is abbreviated as %s and has %s" %(state, abbrev, cities[abbrev])
	

