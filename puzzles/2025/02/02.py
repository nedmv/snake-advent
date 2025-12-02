import sys

input = sys.argv[1] if len(sys.argv) >= 2 else "input"
D = open(input).read().strip().split("\n")


def get_pairs(line):
    return [[int(x) for x in y.split("-")] for y in line.split(",")]


def solve():
    pairs = get_pairs(D[0])
    ans = 0
    for left, right in pairs:
        for num in range(left, right + 1):
            s = str(num)
            n = len(s)
            if n % 2 == 0 and s[: n // 2] == s[n // 2 :]:
                ans += num
    return ans


def solve2():
    pairs = get_pairs(D[0])
    ans = 0
    for left, right in pairs:
        for num in range(left, right + 1):
            s = str(num)
            n = len(s)
            num_valid = True
            for lim in range(1, n // 2 + 1):
                if n % lim != 0:
                    continue
                pattern = s[0:lim]
                pattern_repeats = True
                for end in range(2 * lim, n + 1, lim):
                    if s[end - lim : end] != pattern:
                        pattern_repeats = False
                        break
                if pattern_repeats:
                    num_valid = False
                    break
            if not num_valid:
                ans += num
    return ans


print(solve())
print(solve2())
