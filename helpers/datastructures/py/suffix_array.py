#!/usr/bin/env python3


def construct_suffix_array(s):
    # TODO: store (start, end) pairs instead of the substring
    suffix_a = [(i, s[i:]) for i in range(len(s))]
    suffix_a.sort(key=lambda s: s[1])
    return suffix_a


def longest_common_prefix_array(a):
    # TODO: more efficient construction
    suffixes = [0]
    i = 1
    while i < len(a):
        j = 0
        while j < len(a[i][1]) and j < len(a[i-1][1]) and a[i][1][j] == a[i-1][1][j]:
            j += 1
        suffixes.append(j)
        i += 1
    return [(suffixes[i], a[i]) for i in range(len(suffixes))]


def count_unique_substrings(s):
    a = construct_suffix_array(s)
    a = longest_common_prefix_array(a)
    n = len(s)
    return int(n * (n + 1) / 2) - sum(b[0] for b in a)

