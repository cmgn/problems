#!/usr/bin/env python3

from sys import stdin


def main():
    i = 0
    lines = [l.strip() for l in stdin]
    while i < len(lines):
        injective = True
        function = True

        domain = lines[i].split()[1:]
        codomain = lines[i+1].split()[1:]
        number_of_mappings = int(lines[i+2])
        i += 3

        for _ in range(number_of_mappings):
            a, _, b = lines[i].split()
            if a in domain:
                domain.remove(a)
            else:
                function = False
                # result cannot be anything other than not a function now
                break

            if b not in codomain:
                injective = False
            elif b in codomain:
                codomain.remove(b)
            i += 1
    
        if not function:
            print("not a function")
        elif injective and not codomain:
            print("bijective")
        elif injective:
            print("injective")
        elif not codomain:
            print("surjective")
        else:
            print("neither injective nor surjective")


if __name__ == '__main__':
    main()
