def score(a, b):
    if a == 1 and b == 2 or a == 2 and b == 1:
        return (3, 100)
    if a == b:
        return (2, a * 10 + b)
    return (1, max(b * 10 + a, a * 10 + b))

while True:
    s0, s1, r0, r1 = map(int, input().split())
    if s0 == s1 == r0 == r1 == 0:
        break
    a = score(s0, s1)
    b = score(r0, r1)
    if a > b:
        print('Player 1 wins.')
    elif a < b:
        print('Player 2 wins.')
    else:
        print('Tie.')

