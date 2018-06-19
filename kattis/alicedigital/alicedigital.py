#!/usr/bin/env python3


def main():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        xs = [int(x) for x in input().split()]
        best = 0
        current = []
        m_pos = -1
        for x in xs:
            if x < m:
                if m_pos != -1:
                    best = max(best, sum(current))
                current = []
                m_pos = -1
            elif x == m and m_pos != -1:
                best = max(best, sum(current))
                current = current[m_pos+1:]
                current.append(x)
            elif x == m:
                current.append(x)
                m_pos = len(current) - 1
            else:
                current.append(x)
        if m_pos != -1:
            best = max(best, sum(current))
        print(best)


if __name__ == '__main__':
    main()
