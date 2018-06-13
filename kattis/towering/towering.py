import itertools

def main():
    xs = [int(x) for x in input().split()]
    blocks = set(xs[:6])
    height = xs[-2]
    successful_combination = None
    for combination in itertools.combinations(blocks, 3):
        if sum(combination) == height:
            print(" ".join(map(str, sorted(combination, reverse=True))), end=" ")
            print(" ".join(map(str, sorted(set(combination) ^ blocks, reverse=True))))
            return


if __name__ == "__main__":
    main()
