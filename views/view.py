''' Handles command line interface '''
from termcolor import cprint, colored
from lonely import Singleton
from commands.command import RootCommandParser


default_c = 'blue'
root_parser = RootCommandParser.Instance()

#Abstract Class
class View:
    def input(self):
        raise NotImplementedError

    def output(self):
        raise NotImplementedError

    def help(self):
        raise NotImplementedError

@Singleton
class ConsoleView(View):

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
        for msg in root_parser.get_help():
            print colored(msg['name'] + ' ' + msg['arg'], default_c) + ' ' + msg['bind'] + ' ' + msg['help']

    def error(self, msg):
        cprint("===> " + msg, 'red')
