ncases = int(input())

for i in range(ncases):
    nstores = int(input())
    spots = [int(x) for x in input().split()]
    average = sum(spots) // len(spots)
    print((average - min(spots)) * 2 + (max(spots) - average) * 2)

