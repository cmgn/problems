from sys import stdin

def should_escape(c):
    return any([
        c >= "!" and c <= "*",
        c >= "[" and c <= "]"
    ])

lines = stdin.readlines()

i = 0
while i < len(lines):
    level = int(lines[i])
    string = lines[i + 1]
    i += 2
    for j in range(level):
        output = ""
        for c in string:
            if should_escape(c):
                output += "\\" + c
            else:
                output += c
        string = output
    print(string)

