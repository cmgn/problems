n = int(input())
m = n // 2

if n % 2 == 0:
    sum_odds = m * m
else:
    sum_odds = (m + 1) * (m + 1)

print(m * (m + 1) - sum_odds)
