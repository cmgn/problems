def flipcase(c):
    if c.isupper():
        return c.lower()
    return c.upper()

s = input()
c = sum(int(c.isupper()) for c in s)
if c == len(s) or c == len(s) - 1 and s[0].islower():
    print("".join(flipcase(c) for c in s))
else:
    print(s)
