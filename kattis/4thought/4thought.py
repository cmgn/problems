#!/usr/bin/env python3

import sys

operators = ["+", "-", "*", "//"]
operator_combinations = [(a, b, c) for a in operators for b in operators for c in operators]

def evaluate_num(n):
    for a, b ,c in operator_combinations:
        if eval("4 {0} 4 {1} 4 {2} 4 == {3}".format(a, b, c, n)):
            return "4 {0} 4 {1} 4 {2} 4 = {3}".format(a, b, c, n).replace("//", "/")
    return "no solution"

nums = sys.stdin.readlines()

for num in nums[1:]:
    print(evaluate_num(int(num)))
