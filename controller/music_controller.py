''' The main glue between the cli and the data '''
from views import cli, errors
from models.music_data import Library
from player import Player


library = Library.Instance() #Library is a singleton
player = Player()


def parse(input):
    i = input.split(" ")
    return i

def list_songs(*args):
    if library.get_songs():
        for song in library.get_songs():
            print str(song.get_id()) + ".)" + str(song.get_name())
    else:
        errors.output('Your library is empty, load something?')

def play(id=1, *args):
    if id == 0:
        id = 1
    try:
        found = False
        pid = int(id)
        for song in library.get_songs():
            if pid == song.get_id():
                player.play(song)
                found = True
        if not found:
            errors.output("That song isn't in your library")
            controller()

    except ValueError:
        errors.output("The 'play' command expects the song id{int} as arg")
        controller()


def load_library(path="/home/tame/Music", *args):
    if path == 0:
        path = "/home/tame/Music"
    try:
        path = str(path) #Change arg to string
        if library.load(path):
            cli.output("All Songs Loaded")

    except StopIteration:
        errors.output("No songs found")
        controller()

    except OSError:
        errors.output("Path not found")
        controller()



def get_song(*args):
    if player.playing():
        song = player.get_song()
        cli.output(song.get_name())
    else:
        cli.output("Nothing is playing")


def help(*args):
    cli.help()

switcher = {
    "load": load_library,
    "list": list_songs,
    "play": play,
    "pause": player.pause,
    "resume": player.resume,
    "stop": player.stop,
    "whatisplaying": get_song,
    "help": help,
}

def controller():
    while True:
        try:
            input = cli.input()
            cmd, arg, args = 0, 0, 0
            try:
                cmd = parse(input)[0] #Main command
                arg = parse(input)[1] #Main arg, Might raise IndexError
                args = parse(input)[2:] #Extras, Might raise IndexError
            except IndexError:
                pass
            func = switcher[cmd] #Raise KeyError if cmd not in switcher
            func(arg, args)

        # except ExcessInput:
        #     errors.output("Check that command")
        #     continue

        except KeyError:
            errors.output("I don't understand that")
            continue

        except Exception as e:
            print e, '--> COntroller'
            continue

