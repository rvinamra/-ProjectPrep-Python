class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_song(self):
		for line in self.lyrics	:
			print line
			
happy_bday = Song(["Happy Birthday to you",
					"thats it",
					"Now I stop"])
					
bulls_parade = Song(["they rally around the family",
					"I don't want to get into that"])
					
happy_bday.sing_me_song()

bulls_parade.sing_me_song()