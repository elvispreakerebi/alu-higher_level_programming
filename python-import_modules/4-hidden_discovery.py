#!/usr/bin/python3
import dis
import marshal
import sys

def main():
    with open("hidden_4.pyc", "rb") as f:
        f.read(16)  # Skip the header
        code_obj = marshal.load(f)

    names = code_obj.co_names
    sorted_names = sorted(name for name in names if not name.startswith("__"))

    for name in sorted_names:
        print(name)

if __name__ == "__main__":
    main()
