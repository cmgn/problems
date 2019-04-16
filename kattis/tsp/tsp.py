from random import shuffle

n = int(input())
xs = list(range(n))
shuffle(xs)
print("\n".join(map(str, xs)))
