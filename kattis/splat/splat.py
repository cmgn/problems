import math


def main():
    n = int(input())
    for _ in range(n):
        splats = []

        m = int(input())
        for _ in range(m):
            x, y, v, w = input().split()
            x, y, v = map(float, (x, y, v)) 
            r = v/math.pi
            splats.append((x, y, r, w))

        splats.reverse()

        m = int(input())
        for _ in range(m):
            z, v = map(float, input().split())
            for x, y, r, w in splats:
                if (x-z)*(x-z) + (y-v)*(y-v) <= r:
                    print(w)
                    break
            else:
                print("white")
                


if __name__ == "__main__":
    main()

