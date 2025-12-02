import sys

input = sys.argv[1] if len(sys.argv) >= 2 else "input"
D = open(input).read().strip().split("\n")


def solve():
    pos = 50
    n = 100
    ans = 0
    for line in D:
        dir = -1 if line[0] == "L" else 1
        num = int(line[1:])
        pos = (pos + num * dir) % n
        if pos == 0:
            ans += 1
    return ans


def solve2():
    pos = 50
    n = 100
    ans = 0
    for line in D:
        dir = -1 if line[0] == "L" else 1
        num = int(line[1:])
        next = pos + num * dir
        ans += abs(next) // n
        if next <= 0 and pos != 0:
            ans += 1
        pos = next % n
    return ans


print(solve())
print(solve2())
