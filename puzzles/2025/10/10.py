import sys
from copy import deepcopy
from heapq import heappop, heappush

from z3 import Int, Optimize, Sum


def solve(D):
    ans = 0
    for line in D:
        segments = line.split(" ")
        indicators = []
        for i in range(1, len(segments[0]) - 1):
            indicators.append(True if segments[0][i] == "#" else False)

        buttons = []
        for s in segments[1 : len(segments) - 1]:
            buttons.append([int(x) for x in s[1 : len(s) - 1].split(",")])

        state = [False for _ in range(len(indicators))]
        q = [(0, state)]
        seen = set()
        seen.add(tuple(state))
        while q:
            t, state = heappop(q)
            if state == indicators:
                ans += t
                break
            for button in buttons:
                new_state = deepcopy(state)
                for b in button:
                    new_state[b] = not state[b]
                tup = tuple(new_state)
                if tup not in seen:
                    seen.add(tup)
                    heappush(q, (t + 1, new_state))

    return ans


def solve2(D):
    ans = 0
    for line in D:
        segments = line.split(" ")

        buttons = []
        for s in segments[1 : len(segments) - 1]:
            buttons.append([int(x) for x in s[1 : len(s) - 1].split(",")])

        joltage = [int(x) for x in segments[-1][1 : len(segments[-1]) - 1].split(",")]

        variables = []
        s = Optimize()
        for i in range(len(buttons)):
            x = Int(chr(ord("a") + i))
            s.add(x >= 0)
            variables.append(x)
        for i in range(len(joltage)):
            cur = []
            for j, button in enumerate(buttons):
                if i in button:
                    cur.append(j)
            eq = Sum([variables[c] for c in cur]) == joltage[i]
            s.add(eq)
        s.minimize(Sum(variables))
        s.check()
        m = s.model()
        cur = 0
        for var in variables:
            cur += m[var].as_long()
        ans += cur
    return ans


targets = sys.argv[1:] if len(sys.argv) >= 2 else ["test", "input"]
for target in targets:
    data = open(target).read().strip().split("\n")
    print(f"Part 1 for {target}:", solve(data))
    print(f"Part 2 for {target}:", solve2(data))
