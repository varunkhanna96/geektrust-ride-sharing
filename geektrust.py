from sys import argv

from command_executor import CommandExecutor

MIN_ARG_LENGTH = 2


def main():
    if len(argv) != MIN_ARG_LENGTH:
        raise Exception("File path not entered")
    executor = CommandExecutor()
    file_path = argv[1]
    executor.read_file(file_path=file_path)


if __name__ == "__main__":
    main()
