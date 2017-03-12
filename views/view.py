''' Handles command line interface '''
from termcolor import cprint, colored


default_c = 'blue'

class View:
    def input(self):
        raise NotImplementedError

    def output(self):
        raise NotImplementedError

    def help(self):
        raise NotImplementedError

class ConsoleView:

    def __init__(self):
        pass

    def input(self):
        prompt = colored(">>> ", default_c)
        input = raw_input(prompt)
        return input

    def output(self, msg):
        cprint("[*]" + msg, 'green')

    def help(self):
        cprint("======>Welcome to PyTunes<======", 'red')
        cprint("----------CLI Commands----------", 'green')
        print colored("load 'path'", default_c) + " --> Load songs in 'path' to music player library"
        print colored("list", default_c) + " --> List all songs in music player "
        print colored("play id", default_c) + " --> Play song with id"
        print colored("whatisplaying", default_c) + " --> Show name of song playing"
        print colored("pause", default_c) + " --> Pause song"
        print colored("resume", default_c) + " --> Resume paused song"
        print colored("stop", default_c) + " --> stop playing"
        print colored("help", default_c) + " --> This message"

    def error(self, msg):
        cprint("===> " + msg, 'red')
