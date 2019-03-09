n = int(input())
f = 1
t = 0
for i in range(1, n + 2):
    t += 1/f
    f *= i
print("{:.16f}".format(t))