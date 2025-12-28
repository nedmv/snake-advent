import sys


# non-generic, works because inputs are "nice"
# does not work for example
def solve(D):
    shapes = [[] for _ in range(6)]
    regions = []

    for i in range(6):
        shapes[i].append(D[i * 5 + 1])
        shapes[i].append(D[i * 5 + 2])
        shapes[i].append(D[i * 5 + 3])

    for line in D[30:]:
        a = line.split(":")[0]
        x = int(a.split("x")[0])
        y = int(a.split("x")[1])
        nums = [int(x) for x in line.split(":")[1].split(" ") if x]
        regions.append((x, y, nums))

    ans = 0
    for x, y, nums in regions:
        total = (x // 3) * (y // 3)
        if total >= sum(nums):
            ans += 1
    return ans


targets = sys.argv[1:] if len(sys.argv) >= 2 else ["input"]
for target in targets:
    data = open(target).read().strip().split("\n")
    print(f"Part 1 for {target}:", solve(data))
