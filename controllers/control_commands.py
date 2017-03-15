from commands.command import Command, RootCommandParser
from controllers.player import Player
from controllers.music_controller import MusicController
from views.view import ConsoleView
from models.library import Library


mview = ConsoleView.Instance()
mmodel = Library.Instance()
mcontroller = MusicController(model=mmodel, view=mview)
mplayer = Player.Instance()


root_parser = RootCommandParser.Instance()


class SubCommand(Command):
    def __init__(self, name, help='', parser=None, aliases=[], arg = ''):
        super(SubCommand, self).__init__(name=name, aliases=aliases, help=help, parser=parser)
        self.controller = mcontroller
        self.view = self.controller.get_view()
        self.model = self.controller.get_model()
        self.player = mplayer
        self.arg = arg

    def get_arg(self):
        return self.arg

class HelpCommand(SubCommand):
    def run(self, *args):
        self.view.help()


class LoadLibraryCommand(SubCommand):
    def run(self, path="/home/tame/Music", *args):
        if path == 0:
            path = "/home/tame/Music"
        try:
            path = str(path) #Change arg to string
            if self.model.load(path):
                self.view.output("All Songs Loaded")

        except StopIteration:
            self.view.error("No songs found")
            self.controller.control()

        except OSError:
            self.view.error("Path not found")
            self.controller.control()


class CheckSongCommand(SubCommand):
    def run(self, *args):
        if self.player.playing():
            song = self.player.get_song()
            self.view.output(song.get_name())
        else:
            self.view.output("Nothing is playing")


class ListLibraryCommand(SubCommand):
    def run(self, *args):
        if self.model.check_library():
            for song in self.model.get_songs():
                print str(song.get_id()) + ".)" + str(song.get_name())
        else:
            self.view.error('Your library is empty, load something?')

class PlayCommand(SubCommand):
    def run(self, id=1, *args):
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
                self.controller.control()

        except ValueError:
            self.view.error("The 'play' command expects the song id as arg")
            self.controller.control()


class PauseCommand(SubCommand):
    def run(self, *args):
        self.player.pause()


class ResumeCommand(SubCommand):
    def run(self, *args):
        self.player.resume()


class StopCommand(SubCommand):
    def run(self, *args):
        self.player.stop()