import sys


def get_map(data):
    return [[ch for ch in data[i]] for i in range(len(data))]


def solve(D):
    ans = 0
    nums = []
    for line in D:
        nums.append([x.lstrip() for x in line.split(" ") if x.lstrip()])

    for col in range(len(nums[0])):
        op = nums[-1][col]
        cur = 1 if op == "*" else 0
        for row in range(len(nums) - 1):
            num = int(nums[row][col])
            if op == "*":
                cur *= num
            else:
                cur += num
        ans += cur
    return ans


def solve2(D):
    ans = 0
    nums = []
    m = get_map(D)
    rows = len(m)
    cols = max((len(m[i]) for i in range(rows)))

    nums = []
    for col in reversed(range(cols)):
        op = " " if col >= len(m[-1]) else m[-1][col]
        num = ""
        for row in range(rows - 1):
            if col >= len(m[row]):
                continue
            num += m[row][col]
        num = num.strip()
        if num:
            nums.append(int(num))

        if op != " ":
            cur = 1 if op == "*" else 0
            for num in nums:
                if op == "*":
                    cur *= num
                else:
                    cur += num
            ans += cur
            nums = []

    return ans


targets = sys.argv[1:] if len(sys.argv) >= 2 else ["test", "input"]
for target in targets:
    data = open(target).read().strip().split("\n")
    print(f"Part 1 for {target}:", solve(data))
    print(f"Part 2 for {target}:", solve2(data))
