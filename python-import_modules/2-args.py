#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    arg_count = len(argv)

    if arg_count == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(arg_count, "" if arg_count == 1 else "s"))
        for i, arg in enumerate(argv, 1):
            print("{}: {}".format(i, arg))
