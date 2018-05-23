#!/usr/bin/env python


from sys import argv, stdin


def main():
    if len(argv) > 1:
        with open(argv[1]) as f:
            content = f.read()
    else:
        content = stdin.read()
    print("[")
    for line in content.split("\n"):
        print("[" + ", ".join(map(lambda x: str(int(x)), line.split())) + "],")
    print("]")


if __name__ == '__main__':
    main()
