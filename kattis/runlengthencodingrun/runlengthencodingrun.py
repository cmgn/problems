cmd, s = input().split()

if cmd == "E":
    i = 0
    while i < len(s):
        j = i
        i += 1
        while i < len(s) and s[i] == s[i - 1]:
            i += 1
        print(s[j] + str(i - j), end="")
else:
    i = 0
    while i < len(s):
        print(s[i] * int(s[i + 1]), end="")
        i += 2

print()

