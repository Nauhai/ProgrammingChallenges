from dataclasses import dataclass
import getopt
import sys


@dataclass
class Arguments:
    input_file: str = None
    input_text: str = None


def print_help(cmd):
    print(f"Use: {cmd} [-f <input_file> | -t <input_text>]")


def parse_args() -> Arguments:
    [cmd, *args] = sys.argv
    opts, args = getopt.getopt(args, "hf:t:", ["help", "file=", "text="])

    arguments = Arguments()

    for opt, arg in opts:
        match opt:
            case "-h" | "--help":
                print_help(cmd)
                sys.exit()
            case "-f" | "--file":
                arguments.input_file = arg
            case "-t" | "--text":
                arguments.input_text = arg

    if not (arguments.input_file or arguments.input_text):
        print("Input Missing.")
        print_help(cmd)
        sys.exit()

    return arguments
