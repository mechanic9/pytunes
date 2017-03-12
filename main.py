from controller.music_controller import MusicController
from controller.player import Player
from models.library import Library
from views.view import ConsoleView
import sys

def main():

    model = Library.Instance()
    view = ConsoleView()
    player = Player()
    controller = MusicController(model, view, player)
    controller.help(0)

    try:
        controller.control()
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == '__main__':
    main()