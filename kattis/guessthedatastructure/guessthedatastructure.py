#!/usr/bin/env python3


from sys import stdin
import heapq


class Stack(object):
    name = "stack"

    def __init__(self):
        self.items = []
    
    def add(self, item):
        self.items.append(item)
    
    def remove(self):
        return self.items.pop()


class Queue(object):
    name = "queue"

    def __init__(self):
        self.items = []
    
    def add(self, item):
        self.items.append(item)
    
    def remove(self):
        return self.items.pop(0)


class PQ(object):
    name = "priority queue"

    def __init__(self):
        self.items = []
    
    def add(self, item):
        self.items.append(-item)
        heapq.heapify(self.items)
    
    def remove(self):
        return -heapq.heappop(self.items)


def guess(commands):
    attempts = [PQ(), Queue(), Stack()]
    for k, v in enumerate(attempts):
        for command in commands:
            if command[0] == 1:
                v.add(command[1])
                continue
            item = v.remove()
            if item != command[1]:
                attempts[k] = None
                break
    attempts = [attempt for attempt in attempts if attempt]
    if len(attempts) > 1:
        print("not sure")
    elif not attempts:
        print("impossible")
    else:
        print(attempts[0].name)


def main():
    i = 0
    lines = [line.strip() for line in stdin]
    while i < len(lines):
        count = int(lines[i])
        i += 1
        commands = [[int(x) for x in lines[i+y].split()] for y in range(count)]
        try:
            guess(commands)
        except IndexError:
            print("impossible")
        i += count
    return


if __name__ == '__main__':
    main()
