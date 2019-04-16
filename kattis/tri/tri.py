ops = {
    "+": int.__add__,
    "-": int.__sub__,
    "*": int.__mul__,
    "/": int.__floordiv__,
}

a, b, c = list(map(int, input().split()))
for op, fn in ops.items():
    if fn(a, b) == c:
        print(f"{a}{op}{b}={c}")
        raise SystemExit
    elif fn(b, c) == a:
        print(f"{a}={b}{op}{c}")
        raise SystemExit
