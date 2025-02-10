import sys
from functools import cache
from copy import copy

moves = [-1, 0, 1, 0, -1] #NESW

input = sys.argv[1] if len(sys.argv)>=2 else 'input'
data = open(input).read().strip().split('\n')


@cache
def rec(d, pos, patterns):
  if pos == len(d):
    return 1
  ans = 0
  for p in patterns:
    if d[pos:].startswith(p):
      ans += rec(d, pos + len(p), patterns)
  return ans


def solve(part2 = False):
  ans = 0
  patterns = data[0].split(", ")
  patterns = tuple(patterns)
  designs = []
  for line in data[2:]:
    designs.append(line)

  for d in designs:
    cur = rec(d, 0, patterns)
    if part2:
      ans += cur
    elif cur > 0:
      ans += 1

  return ans


print(solve())
print(solve(part2=True))