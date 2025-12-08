import sys


def dist(a, b):
    return sum((a[i] - b[i]) ** 2 for i in range(3))


def solve(D):
    t = 1000 if len(D) == 1000 else 10
    boxes = []
    for line in D:
        boxes.append([int(x) for x in line.split(",")])
    n = len(boxes)

    d = []
    for i in range(n):
        for j in range(i + 1, n):
            d.append((dist(boxes[i], boxes[j]), i, j))
    d.sort()

    size = [1 for _ in range(n)]
    parent = [i for i in range(n)]

    def find(x):
        if x == parent[x]:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def join(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        if size[x] < size[y]:
            x, y = y, x
        parent[y] = x
        size[x] += size[y]

    for i in range(t):
        _, x, y = d[i]
        join(x, y)

    sp = [(size[i], find(i)) for i in range(n)]
    sp.sort(reverse=True)

    seen = set()
    ans = 1
    cnt = 0
    for s, p in sp:
        if p not in seen:
            seen.add(p)
            ans *= s
            cnt += 1
            if cnt == 3:
                break

    return ans


def solve2(D):
    boxes = []
    for line in D:
        boxes.append([int(x) for x in line.split(",")])
    n = len(boxes)

    d = []
    for i in range(n):
        for j in range(i + 1, n):
            d.append((dist(boxes[i], boxes[j]), i, j))
    d.sort()

    size = [1 for _ in range(n)]
    parent = [i for i in range(n)]

    def find(x):
        if x == parent[x]:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def join(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return False
        if size[x] < size[y]:
            x, y = y, x
        parent[y] = x
        size[x] += size[y]
        return size[x] == n

    for _, x, y in d:
        if join(x, y):
            return boxes[x][0] * boxes[y][0]
    return 0


targets = sys.argv[1:] if len(sys.argv) >= 2 else ["test", "input"]
for target in targets:
    data = open(target).read().strip().split("\n")
    print(f"Part 1 for {target}:", solve(data))
    print(f"Part 2 for {target}:", solve2(data))
