#!/usr/bin/env python3

n = int(input())
n_bin_reversed = bin(n)[2:][::-1]
print(int(n_bin_reversed, 2))