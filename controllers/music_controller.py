''' The main glue between the cli and the data '''
from commands.command import RootCommandParser

#Segregate controllers from cli commands with command pattern
#Different implementation of the singleton pattern
class MusicController(object):

    class __MusicController(object):

        def __init__(self, model, view, root_parser=None):
            self.model = model
            self.view = view
            self.root_parser = root_parser or RootCommandParser.Instance() #Default parser
            self.switcher = {}

        def control(self):
            while True:
                input = self.view.input()
                cmd, arg, args = 0, 0, 0
                try:
                    cmd = self.parse(input)[0] #Main command
                    arg = self.parse(input)[1] #Main arg, Might raise IndexError
                    args = self.parse(input)[2:] #Extras, Might raise IndexError

                except IndexError:
                    pass

                try:
                    func = self.root_parser.get_command_by_name(cmd).run #Return none if cmd not in switcher
                    func(arg, args)

                except AttributeError:
                    self.view.error("I don't understand that")
                    continue

        def parse(self, input):
            i = input.split(" ")
            return i

        def get_view(self):
            return self.view

        def get_model(self):
            return self.model

    instance = None

    def __init__(self, model, view, root_parser=None):

        if not MusicController.instance:
            MusicController.instance = MusicController.__MusicController(model, view, root_parser)

        else:
            MusicController.instance.model = model
            MusicController.instance.view = view
            MusicController.instance.root_parser = root_parser


    def __getattr__(self, name):
        return getattr(self.instance, name)

    def get_instance(self):
        return self.instance
