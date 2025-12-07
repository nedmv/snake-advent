import sys


def get_map(data):
    return [[ch for ch in data[i]] for i in range(len(data))]


def solve(D):
    ans = 0
    m = get_map(D)
    rows = len(m)
    cols = len(m[0])
    start_col = 0
    for c in range(cols):
        if m[0][c] == "S":
            start_col = c
            break

    q = [(0, start_col)]
    seen = set()
    while q:
        row, col = q.pop()
        next = []
        if m[row][col] == "^":
            next = [(row, col - 1), (row, col + 1)]
            ans += 1
        elif row < rows - 1:
            next = [(row + 1, col)]
        for ne in next:
            if ne not in seen:
                q.append(ne)
                seen.add(ne)

    return ans


def solve2(D):
    m = get_map(D)
    rows = len(m)
    cols = len(m[0])
    start_col = 0
    for c in range(cols):
        if m[0][c] == "S":
            start_col = c
            break

    dp = [0 for _ in range(cols)]
    dp[start_col] = 1
    cur = [0 for _ in range(cols)]

    for row in range(1, rows):
        for col in range(0, cols):
            if m[row][col] == "^":
                cur[col - 1] += dp[col]
                cur[col + 1] += dp[col]
            else:
                cur[col] += dp[col]
        for i in range(cols):
            dp[i] = cur[i]
            cur[i] = 0

    return sum(dp)


targets = sys.argv[1:] if len(sys.argv) >= 2 else ["test", "input"]
for target in targets:
    data = open(target).read().strip().split("\n")
    print(f"Part 1 for {target}:", solve(data))
    print(f"Part 2 for {target}:", solve2(data))
