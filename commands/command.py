'''Implementation of Command Pattern'''
from lonely import Singleton

#Class for all subcommands
class Command(object):
    def __init__(self, name, aliases=[], parser=None, help=''):
        self.name = name
        self.parser = parser or RootCommandParser.Instance()
        self.aliases = aliases
        self.help = help
        self.root_parser = None

    def run(self):
        raise NotImplementedError

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_aliases(self, *aliases):
        self.aliases.append(aliases)

    def get_aliases(self):
        return self.aliases

    def set_parser(self, parser):
        self.parser = parser

    def get_parser(self):
        return self.parser

    def set_help(self, help):
        self.help = help

    def get_help(self):
        return self.help

    def get_root_parser(self):
        return self.root_parser

    def set_root_parser(self, parser):
        return self.root_parser


#Abstract class for all command parsers
@Singleton
class RootCommandParser(object):
    def __init__(self):
        self.subcommands = []

    #Merge helps of all subcommands
    def get_help(self, bind='-->'):
        helper = []
        for cmd in self.get_commands():
            helper.append({'name': cmd.get_name(), 'arg': cmd.get_arg(), 'bind': bind, 'help': cmd.get_help()})
        return helper

    #Add a new command
    def add_command(self, cmds):
        for cmd in cmds:
            cmd.set_root_parser(self)
            self.subcommands.append(cmd)

    #Get a command by the registered name
    def get_command_by_name(self, name):
        for cmd in self.subcommands:
            if name == cmd.get_name() or name == cmd.get_aliases():
                return cmd
        else:
            return None

    #Get generator for all commands
    def get_commands(self):
        for cmd in self.subcommands:
            yield cmd

    #Get generator for all commands
    def is_empty(self):
        if self.subcommands:
            return True
        else:
            return False


# class SubCommandParser(RootCommandParser):
#     def __init__(self):
#         super(SubCommandParser, self).__init__()

