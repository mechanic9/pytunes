from controller.music_controller import controller, help
import sys

def main():
    help()
    try:
        controller()
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == '__main__':
    main()