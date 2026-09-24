# create a musicplayer class and subclass spotify to override play method 

class MusicPlayer():

    def play(self):
        print("Musicplayer playing the song")

class Spotify(MusicPlayer):

    def play(self):
        print("Spotify playing the song")

m1= MusicPlayer()
s1= Spotify()

m1.play()
s1.play()