import sys
from functools import cache


def get_out(D):
    out = {}
    for line in D:
        name = line.split(":")[0]
        out[name] = [x for x in line.split(":")[1].split(" ") if x]
    return out


def solve(D):
    out = get_out(D)

    @cache
    def rec(a):
        if a == "out":
            return 1

        ans = 0
        for o in out[a]:
            ans += rec(o)
        return ans

    return rec("you")


def solve2(D):
    out = get_out(D)

    @cache
    def rec(a, vis):
        if a == "out":
            return 1 if vis == 3 else 0
        elif a == "dac":
            vis += 1
        elif a == "fft":
            vis += 2

        ans = 0
        for o in out[a]:
            ans += rec(o, vis)
        return ans

    return rec("svr", 0)


p1_only_targets = ["test1"]
p2_only_targets = ["test2"]
targets = sys.argv[1:] if len(sys.argv) >= 2 else ["test1", "test2", "input"]
for target in targets:
    try:
        with open(target) as f:
            data = open(target).read().strip().split("\n")
            if target not in p2_only_targets:
                print(f"Part 1 for {target}:", solve(data))
            if target not in p1_only_targets:
                print(f"Part 2 for {target}:", solve2(data))
    except (FileNotFoundError, IOError) as e:
        print(f"Error: {e}")
