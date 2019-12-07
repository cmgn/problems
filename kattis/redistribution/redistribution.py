input()

xs = [int(x) for x in input().split()]
ys = list(range(len(xs)))
ys.sort(key=lambda i: xs[i], reverse=True)

if xs[ys[0]] > sum(xs[i] for i in ys[1:]):
    print('impossible')
else:
    print(' '.join([str(i + 1) for i in ys]))
