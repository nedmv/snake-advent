def get_map(data):
    return [[ch for ch in data[i]] for i in range(len(data))]


def check(m, row, col):
    cnt = 0
    if m[row][col] == ".":
        return False
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == dc == 0:
                continue
            r = row + dr
            c = col + dc
            if 0 <= r < len(m) and 0 <= c < len(m[0]) and m[r][c] == "@":
                cnt += 1
    return cnt < 4


def solve(D):
    ans = 0
    m = get_map(D)

    for row in range(len(m)):
        for col in range(len(m[0])):
            if check(m, row, col):
                ans += 1
    return ans


def solve2(D):
    ans = 0
    m = get_map(D)

    removed = True
    while removed:
        removed = False
        for row in range(len(m)):
            for col in range(len(m[0])):
                if check(m, row, col):
                    m[row][col] = "."
                    removed = True
                    ans += 1
    return ans


for target in ("test", "input"):
    data = open(target).read().strip().split("\n")
    print(f"Part 1 for {target}:", solve(data))
    print(f"Part 2 for {target}:", solve2(data))
