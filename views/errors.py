''' Handles errors in command line interface '''
from termcolor import cprint

def output(msg):
    cprint("===> " + msg, 'red')