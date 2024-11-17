from screen_manager import Screens
from monitor_manager import Monitor
from command_line import cli

from pprint import pp
import argparse
import yaml
import os

def main():
    parser = argparse.ArgumentParser(description="A tool for managing multi-display & app presets")

    subparser = parser.add_subparsers(dest="command", help="Commands")
    save_parser = subparser.add_parser('save', help='Use screens or apps as a modifier to choose what to save')
    save_parser.add_argument('--preset', '-p', help='Title for your preset to save monitor configs')

    apply_screens_parser = subparser.add_parser('apply', help='Use displayplacer to apply stored screen settings')
    apply_screens_parser.add_argument('--param', help='Optional add info for applying screen data')

    display_parser = subparser.add_parser('display', help='Display currently saved displays, more functionality coming')
    display_parser.add_argument('--details', '-d', action='store_true', help='Display more details about each display')


    args = parser.parse_args()

    if args.command == 'save':
        cli.handle_save_command(args)

    elif args.command == 'apply':
        
        Screens.apply_specs()
        print('Screen Settings Applied')
    
    elif args.command == 'display':
        cli.handle_display_command(args)


if __name__ == '__main__':
    main()