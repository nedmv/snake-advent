import sys


def get_points(data):
    return [[int(x) for x in line.split(",")] for line in data]


def min_max(a, b):
    return (a, b) if a < b else (b, a)


def square(a, b):
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)


def solve(D):
    points = get_points(D)
    n = len(points)
    ans = 0
    for i in range(n):
        a = points[i]
        for j in range(i + 1, n):
            b = points[j]
            ans = max(ans, square(a, b))
    return ans


def solve2(D):
    ans = 0
    points = get_points(D)
    n = len(points)

    v_lines = []
    h_lines = []
    for i in range(n):
        j = (i + 1) % n
        a, b = points[i], points[j]
        x_min, x_max = min_max(a[0], b[0])
        y_min, y_max = min_max(a[1], b[1])
        y_max = max(a[1], b[1])

        if y_min == y_max:
            v_lines.append(((x_min, x_max), y_min))
        elif x_min == x_max:
            h_lines.append((x_min, (y_min, y_max)))
        else:
            assert False, "Unordered points in input"

    def v_intersect(x, y1, y2, is_upper):
        for (x_min, x_max), y in v_lines:
            if (y1 < y < y2) and (
                (x_min < x < x_max)
                or (is_upper and x == x_min)
                or (not is_upper and x == x_max)
            ):
                return True
        return False

    def h_intersect(x1, x2, y, is_left):
        for x, (y_min, y_max) in h_lines:
            if (x1 < x < x2) and (
                (y_min < y < y_max)
                or (is_left and y == y_min)
                or (not is_left and y == y_max)
            ):
                return True
        return False

    for i in range(n):
        a = points[i]
        for j in range(i + 1, n):
            b = points[j]
            x_min, x_max = min_max(a[0], b[0])
            y_min, y_max = min_max(a[1], b[1])
            if (
                h_intersect(x_min, x_max, y_min, True)
                or h_intersect(x_min, x_max, y_max, False)
                or v_intersect(x_min, y_min, y_max, True)
                or v_intersect(x_max, y_min, y_max, False)
            ):
                continue
            ans = max(ans, square(a, b))

    return ans


targets = sys.argv[1:] if len(sys.argv) >= 2 else ["test", "input"]
for target in targets:
    data = open(target).read().strip().split("\n")
    print(f"Part 1 for {target}:", solve(data))
    print(f"Part 2 for {target}:", solve2(data))
