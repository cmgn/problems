class FenwickTree:
    def __init__(self, n):
        self.nums = [0] * (n + 1)

    def add(self, i, n):
        while i < len(self.nums):
            self.nums[i] += n
            i += i & -i

    def count(self, i):
        result = 0
        while i:
            result += self.nums[i]
            i -= i & -i
        return result

    def countrange(self, i, j):
        return self.count(j) - self.count(i - 1)


def main():
    n, q = [int(x) for x in input().split()]
    tree = FenwickTree(n)
    isset = [False] * (n + 1)
    for i in range(q):
        a, *b = input().split()
        if a == "F":
            b = int(b[0])
            tree.add(b, -1 if isset[b] else 1)
            isset[b] = not isset[b]
        else:
            print(tree.countrange(int(b[0]), int(b[1])))


if __name__ == "__main__":
    main()

