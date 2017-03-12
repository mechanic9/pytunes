''' The main glue between the cli and the data '''
from controller import Controller

class MusicController(Controller):

    def __init__(self, model, view, player):
        super(MusicController, self).__init__(model, view)
        self.player = player
        self.switcher = {
            "load": self.load_library,
            "list": self.list_songs,
            "play": self.play,
            "pause": self.player.pause,
            "resume": self.player.resume,
            "stop": self.player.stop,
            "whatisplaying": self.get_song,
            "help": self.help,
        }

    def control(self):
        while True:
            try:
                input = self.view.input()
                cmd, arg, args = 0, 0, 0
                try:
                    cmd = self.parse(input)[0] #Main command
                    arg = self.parse(input)[1] #Main arg, Might raise IndexError
                    args = self.parse(input)[2:] #Extras, Might raise IndexError
                except IndexError:
                    pass
                func = self.switcher[cmd] #Raise KeyError if cmd not in switcher
                func(arg, args)

            except KeyError:
                self.view.error("I don't understand that")
                continue

    def parse(self, input):
        i = input.split(" ")
        return i

    def list_songs(self, *args):
        if self.model.check_library():
            for song in self.model.get_songs():
                print str(song.get_id()) + ".)" + str(song.get_name())
        else:
            self.view.error('Your library is empty, load something?')

    def play(self, id=1, *args):
        library = self.model
        if id == 0:
            id = 1
        try:
            found = False
            pid = int(id)
            for song in self.model.get_songs():
                if pid == song.get_id():
                    self.player.play(song)
                    found = True
            if not found:
                self.view.error("That song isn't in your library")
                self.control()

        except ValueError:
            self.view.error("The 'play' command expects the song id{int} as arg")
            self.control()

    def load_library(self, path="/home/tame/Music", *args):
        if path == 0:
            path = "/home/tame/Music"
        try:
            path = str(path)  # Change arg to string
            if self.model.load(path):
                self.view.output("All Songs Loaded")

        except StopIteration:
            self.view.error("No songs found")
            self.control()

        except OSError:
            self.view.error("Path not found")
            self.control()

    def get_song(self, *args):
        if self.player.playing():
            song = self.player.get_song()
            self.view.output(song.get_name())
        else:
            self.view.output("Nothing is playing")

    def help(self, *args):
        self.view.help()

