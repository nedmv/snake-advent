import sys
from collections import defaultdict
from copy import copy

input = sys.argv[1] if len(sys.argv)>=2 else 'input'
data = open(input).read().strip().split('\n')

def calc(num):
  r1 = num * 64
  num ^= r1
  num %= 16777216
  r2 = num // 32
  num ^= r2
  num %= 16777216
  r3 = num * 2048
  num ^= r3
  num %= 16777216
  return num


def solve():
  secrets = []
  for line in data:
    secrets.append(int(line))

  ans = 0
  for num in secrets:
    for _ in range(2000):
      num = calc(num)
    ans += num
  return ans


def solve2():
  secrets = []
  for line in data:
    secrets.append(int(line))

  patterns = [[] for _ in range(len(secrets))]
  changes = [[-1000] for _ in range(len(secrets))]
  for i in range(len(secrets)):
    num = secrets[i]
    patterns[i].append(num % 10)
    for _ in range(2000):
      num = calc(num)
      patterns[i].append(num % 10)
      changes[i].append(patterns[i][-1] - patterns[i][-2])

  maps = [defaultdict(lambda:-1) for _ in range(len(secrets))]
  pset = set()
  for i in range(len(secrets)):
    for end in range(4, 2001):
      p = (changes[i][end-3], changes[i][end-2], changes[i][end-1], changes[i][end])
      pset.add(p)
      if maps[i][p] == -1:
        maps[i][p] = patterns[i][end]

  ans = 0
  for p in pset:
    cur = 0
    for i in range(len(secrets)):
      if maps[i][p] > 0:
        cur += maps[i][p]
    if cur > ans:
      ans = cur
  return ans


print(solve())
print(solve2())