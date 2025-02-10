import sys
from collections import defaultdict
from copy import copy

input = sys.argv[1] if len(sys.argv)>=2 else 'input'
data = open(input).read().strip().split('\n')


def parse():
  s = []
  for line in data:
    fi = line[0:2]
    se = line[3:]
    if fi not in s:
      s.append(fi)
    if se not in s:
      s.append(se)
    pass

  adj = [[0 for _ in range(len(s))] for _ in range(len(s))]
  for line in data:
    fi = line[0:2]
    se = line[3:]
    adj[s.index(fi)][s.index(se)] = 1
    adj[s.index(se)][s.index(fi)] = 1
  return s, adj

def solve():
  s, adj = parse()
  ans = 0
  seen = set()
  for i in range(len(s)):
    if s[i][0] != 't':
      continue
    for j in range(len(s)):
      if adj[i][j] != 1:
        continue
      for k in range(len(s)):
        li = [i, j, k]
        li.sort()
        li = tuple(li)
        if li in seen:
          continue
        if adj[i][k] == 1 and adj[j][k] == 1:
          ans += 1
          seen.add(li)
  return ans


def rec(adj, start, stack, seen):
  seen.append(start)
  l = list(stack)
  for e in stack:
    if e != start and e not in adj[start]:
      return copy(l[:-1])
  ans = copy(l)
  for i in adj[start]:
    if i not in seen:
      l.append(i)
      cur = rec(adj, i, tuple(l), seen)
      l.pop()
      if len(cur) > len(ans):
        ans = copy(list(cur))
  return ans


def solve2():
  s, adj = parse()

  next = defaultdict(list)
  for i in range(len(adj)):
    for j in range(len(adj)):
      if adj[i][j] == 1:
        next[s[i]].append(s[j])

  best = []
  for i in range(len(adj)):
    cur = rec(next, s[i], tuple([s[i]]), [s[i]])
    if len(best) < len(cur):
      best = cur
  
  best.sort()
  return ",".join(best)


print(solve())
print(solve2())