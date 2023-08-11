from dataclasses import dataclass
import getopt
import sys


@dataclass
class Arguments:
    input_file: str = None
    input_text: str = None
    max_number: int = 1
    max_length: int = 100


def print_help(cmd):
    help_str = f"""Use: {cmd} [options]
Options:
-h        | --help             : Print help
-f file   | --file file        : Select input file
-t text   | --text text        : Select input text (input file is prioritized if specified)
-n number | --maxnumber number : The maximum number of sentences to generate (default=1)
-l length | --maxlength length : The maximum length (in words) of the sentences (default=100)
"""
    print(help_str)


def parse_args() -> Arguments:
    [cmd, *args] = sys.argv
    opts, args = getopt.getopt(args, "hf:t:n:l:", ["help", "file=", "text=", "number=", "maxlength="])

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
            case "-n" | "--maxnumber":
                arguments.max_number = int(arg)
            case "-l" | "--maxlength":
                arguments.max_length = int(arg)

    if not (arguments.input_file or arguments.input_text):
        print("Input Missing.")
        print_help(cmd)
        sys.exit()

    return arguments
