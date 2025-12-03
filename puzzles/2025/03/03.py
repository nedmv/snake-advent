def solve(D, limit=2):
    ans = 0
    n = len(D[0])
    for line in D:
        chars = ["0" for _ in range(limit)]
        for i in range(n):
            for pos in range(limit):
                if chars[pos] < line[i] and i + limit - pos - 1 < n:
                    chars[pos] = line[i]
                    for j in range(pos + 1, limit):
                        chars[j] = "0"
                    break
        ans += int("".join(x for x in chars))
    return ans


def solve2(D):
    return solve(D, limit=12)


for target in ("test", "input"):
    data = open(target).read().strip().split("\n")
    print(f"Part 1 for {target}:", solve(data))
    print(f"Part 2 for {target}:", solve2(data))
