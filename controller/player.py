''' Handles Music Player '''
import vlc
from views import cli, errors


class Player:
    def __init__(self):
        self.vlc = vlc.MediaPlayer #Vlc player
        self.isPlaying = False
        self.player = None

    def play(self, song):
        self.song = song

        if self.isPlaying:
            self.player.stop() #Stops previously playing song

        try:
            self.player = self.vlc(self.song.get_path()) #Init player for new song
            self.player.play() #Play song

            self.isPlaying = True #Set playing flag
            cli.output("Playing "+ self.song.get_name())

        except Exception as e:
            errors.output(e)

    def pause(self, *args):
        if self.isPlaying:
            self.player.pause() #Pause song
            self.isPlaying = False #Not playing
            cli.output(self.song.get_name() +" is paused")

        else:
            errors.output("No song was playing")


    def resume(self, *args):
        try:
            self.player.play() #Resume song
            self.isPlaying = True #Not playing
            cli.output(self.song.get_name() +" has been resumed")

        except AttributeError:
            errors.output("No song was playing")  #Catch exception if no song was previously playing

        except Exception as e:
            errors.output(e)


    def stop(self, *args):
        try:
            self.player.stop()  # Stop song

            self.isPlaying = False  # Not playing
            cli.output(self.song.get_name() +" has stopped playing")

        except AttributeError:
            errors.output("No song was playing")  #Catch exception if no song was previously playing

        except Exception as e:
            errors.output(e)

    def playing(self, *args):
        return self.isPlaying

    def get_song(self, *args):
        if self.isPlaying:
            return self.song


