def solve(D):
    ans = 0
    ranges = []
    nums = []
    for line in D:
        if "-" in line:
            ranges.append([int(x) for x in line.split("-")])
        elif len(line) > 0:
            nums.append(int(line))

    for num in nums:
        for l, r in ranges:
            if l <= num <= r:
                ans += 1
                break
    return ans


def solve2(D):
    ans = 0
    ranges = []
    for line in D:
        if "-" in line:
            ranges.append([int(x) for x in line.split("-")])
    ranges.sort()

    cur_max = 0
    for l, r in ranges:
        if l > cur_max:
            ans += r - l + 1
            cur_max = r
        elif r > cur_max:
            ans += r - cur_max
            cur_max = r
    return ans


for target in ("test", "input"):
    data = open(target).read().strip().split("\n")
    print(f"Part 1 for {target}:", solve(data))
    print(f"Part 2 for {target}:", solve2(data))
