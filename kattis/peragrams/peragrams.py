s = input()
d = {}

for c in s:
    d[c] = d.get(c, 0) + 1

nodd = -1
for v in d.values():
    nodd += v % 2

print(max(0, nodd))

