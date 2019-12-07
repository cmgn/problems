import itertools


def main():
    n = input()
    runners = []
    for i in range(int(n)):
        a, b, c = input().split()
        runners.append((a, float(b), float(c)))

    # Pick the 4 best stage 1 runners
    # Pick the 4 best stage 2,3,4 runners
    # It's one of the combinations of 1 + 2,3,4
    runners.sort(key=lambda x: x[1])
    first_leg = runners[:4]
    runners.sort(key=lambda x: x[2])
    other_legs = runners[:4]

    best_score = float('+inf')
    best_team = ()

    for first in first_leg:
        fname = first[0]
        for group in itertools.combinations(other_legs, 3):
            if fname in {x[0] for x in group}:
                continue
            score = first[1] + sum(x[2] for x in group)
            if score < best_score:
                best_score = score
                best_team = (first, *group)
    
    print('{:.10f}'.format(best_score))
    print('\n'.join(x[0] for x in best_team))


if __name__ == "__main__":
    main()