smallest = int(input())
arrangement = [int(x) for x in input().split()]
last_occurrence = {}
for pos, language in enumerate(arrangement):
    if language in last_occurrence:
        diff = pos - last_occurrence[language]
        if diff < smallest:
            smallest = diff
    last_occurrence[language] = pos
print(smallest)
