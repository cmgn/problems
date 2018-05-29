#!/usr/bin/env python3


def main():
    for _ in range(int(input())):
        people = []
        for _ in range(int(input())):
            name, classes, _ = input().split()
            classes = [ord(c[0]) for c in classes.split("-")]
            people.append((name[:-1], classes[::-1] + [109 for _ in range(10 - len(classes))]))
        people.sort(key=lambda p: p[0])
        people.sort(key=lambda p: p[1], reverse=True)
        print("\n".join(map(lambda x: x[0], people)))
        print("==============================")


if __name__ == '__main__':
    main()
