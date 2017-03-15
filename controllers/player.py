''' Handles Music Player '''
import vlc
from views.view import ConsoleView
from lonely import Singleton

cli = ConsoleView.Instance()

@Singleton
class Player:
    def __init__(self):
        self.vlc = vlc.MediaPlayer #Vlc player
        self.isPlaying = False
        self.player = None

    def play(self, song):
        self.song = song

        if self.isPlaying:
            self.player.stop() #Stops previously playing song

        self.player = self.vlc(self.song.get_path()) #Init player for new song
        self.player.play() #Play song

        self.isPlaying = True #Set playing flag
        cli.output("Playing " + self.song.get_name())

    def pause(self):
        if self.isPlaying:
            self.player.pause() #Pause song
            self.isPlaying = False #Not playing
            cli.output(self.song.get_name() + " is paused")

        else:
            cli.error("No song was playing")


    def resume(self):
        try:
            self.player.play() #Resume song
            self.isPlaying = True #Not playing

        except AttributeError:
            cli.error("No song was playing")  #Catch exception if no song was previously playing

        else:
            cli.output(self.song.get_name() + " has been resumed")



    def stop(self):
        try:
            self.player.stop()  # Stop song

            self.isPlaying = False  # Not playing

        except AttributeError:
            cli.error("No song was playing")  #Catch exception if no song was previously playing

        else: #No exception
            cli.output(self.song.get_name() + " has stopped playing")

    def playing(self, *args):
        return self.isPlaying

    def get_song(self, *args):
        if self.isPlaying:
            return self.song


