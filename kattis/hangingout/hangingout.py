limit, events = map(int, input().split())
balance = limit
rejects = 0
for i in range(events):
    typ, num = input().split()
    num = int(num)
    if typ == "leave":
        balance += num
    elif num <= balance:
        balance -= num
    else:
        rejects += 1
print(rejects)
