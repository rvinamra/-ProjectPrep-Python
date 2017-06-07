def break_words(stuff):
	"""This function will break words"""
	words = stuff.split(' ')
	return words
	
def sort_words(words):
	"""Sorts the words"""
	return sorted(words)
	
def print_first_word(words):
	"""Prints first word"""
	word = words.pop(0)
	print word
	
def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(- 1)
	print word

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
	
def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first"""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
	
stuff = "I find your lack of pounce disturbing"
	
