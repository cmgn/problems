#!/usr/bin/env python

prices = [int(input()) for _ in range(int(input()))]
prices.sort(reverse=True)
cost = sum(sum(prices[i:i+2]) for i in range(0, len(prices), 3))

print(cost)
