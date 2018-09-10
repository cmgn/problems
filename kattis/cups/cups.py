import heapq

n = int(input())
h = []

for i in range(n):
    a, b = input().split()
    if a.isdigit():
        heapq.heappush(h, (float(a) / 2, b))
    else:
        heapq.heappush(h, (float(b), a))

while h:
    print(heapq.heappop(h)[1])
