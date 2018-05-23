#!/usr/bin/env python3

vowels = "aeiouy"

n = int(input())
while n:
    words = [input() for _ in range(n)]
    best_word = max(words, key=lambda w: sum(w.count(v*2) for v in vowels))
    print(best_word)
    n = int(input())
