from controllers.music_controller import MusicController
from controllers.control_commands import HelpCommand, LoadLibraryCommand, ListLibraryCommand, CheckSongCommand, PlayCommand, ResumeCommand, PauseCommand, StopCommand
from models.library import Library
from views.view import ConsoleView
from commands.command import RootCommandParser
import sys


def main():
    model = Library.Instance()
    view = ConsoleView.Instance()
    root_parser = RootCommandParser.Instance()

    default_cmds = []
    # Register default commands
    default_cmds.append(HelpCommand(name='help', help='Displays usage message'))  # Registers command with invocation name 'help'
    default_cmds.append(LoadLibraryCommand(name='load', help="Load songs in 'path' to music player library", arg='path'))
    default_cmds.append(ListLibraryCommand(name='list', help='List all songs in music player'))
    default_cmds.append(CheckSongCommand(name='whatisplaying', help='Show name of song playing'))
    default_cmds.append(PlayCommand(name='play', help='Play song with id', arg='id'))
    default_cmds.append(ResumeCommand(name='resume', help='Resume paused song'))
    default_cmds.append(PauseCommand(name='pause', help='Pause song'))
    default_cmds.append(StopCommand(name='stop', help='Stop playing'))

    root_parser.add_command(default_cmds)  # Registers list of commands

    controller = MusicController(model=model, view=view, root_parser=root_parser)

    root_parser.get_command_by_name('help').run(0)

    try:
        controller.control()
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == '__main__':
    main()