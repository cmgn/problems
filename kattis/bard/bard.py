#!/usr/bin/env python3


def main():
    number_of_villagers = int(input())
    villagers = [set() for _ in range(number_of_villagers + 1)]
    number_of_nights = int(input())
    number_of_songs = 0
    
    for _ in range(number_of_nights):
        villagers_present = set(map(int, input().split()[1:]))
        if 1 in villagers_present:
            number_of_songs += 1
            for villager in villagers_present:
                villagers[villager].add(number_of_songs)
        else:
            songs_so_far = set()
            for villager in villagers_present:
                songs_so_far |= villagers[villager]
            for villager in villagers_present:
                villagers[villager] |= songs_so_far
    
    for k, v in enumerate(villagers):
        if len(v) == number_of_songs:
            print(k)


if __name__ == '__main__':
    main()
    