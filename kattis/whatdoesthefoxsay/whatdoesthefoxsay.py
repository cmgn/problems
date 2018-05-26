#!/usr/bin/env python3


number_of_tests = int(input())

for _ in range(number_of_tests):
    sounds_made = input().split()
    other_animals = set()
    s = input()
    while s != "what does the fox say?":
        other_animals.add(s.split()[-1])
        s = input()
    print(" ".join(sound for sound in sounds_made if sound not in other_animals))
