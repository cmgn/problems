#!/usr/bin/env python3


class FenwickTree(object):
    def __init__(self, nums):
        self.nums = [0] * (len(nums) + 1)
        for i in range(1, len(self.nums)):
            self.add(i, nums[i-1])

    def add(self, i, n):
        while i < len(self.nums):
            self.nums[i] += n
            i += (i & -i)
    
    def sum(self, i):
        result = 0
        while i:
            result += self.nums[i]
            i -= (i & -i)
        return result
