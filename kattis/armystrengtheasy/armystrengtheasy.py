#!/usr/bin/env python3


from operator import itemgetter

get_last = itemgetter(-1)

for case in range(int(input())):
    input() # blank line
    num_a, num_b = map(int, input().split())
    
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    a.sort(reverse=True)
    b.sort(reverse=True)

    while a and b:
        min(b, a, key=get_last).pop()

    if len(a) > len(b):
        print ("Godzilla")
    elif len(a) < len(b):
        print ("MechaGodzilla")
    else:
        print ("uncertain")
