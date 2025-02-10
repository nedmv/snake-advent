import sys
from collections import deque
from copy import copy

moves = [-1, 0, 1, 0, -1] #NESW

input = sys.argv[1] if len(sys.argv)>=2 else 'input'
data = open(input).read().strip().split('\n')

def solve():
  ans = 0
  start = (0, 0)
  fin = (70, 70)

  obst = []
  for line in data[:1024]:
    obst.append([int(x) for x in line.split(',')])

  seen = [[False for _ in range(fin[0]+1)] for _ in range(fin[1]+1)]
  seen[0][0] = True
  for o in obst:
    seen[o[0]][o[1]] = True

  q = deque([(0, start[0], start[1])])
  while q:
    t, row, col = q.popleft()
    if (row, col) == fin:
      return t
    for i in range(4):
      r = row + moves[i]
      c = col + moves[i+1]
      if 0 <= r <= fin[0] and 0 <= c <= fin[1] and not seen[r][c]:
        seen[r][c] = True
        q.append((t+1, r, c))

  return ans


def solve2():
  ans = 0
  start = (0, 0)
  fin = (70, 70)

  obst = []
  for line in data[:1024]:
    obst.append([int(x) for x in line.split(',')])

  seen = [[False for _ in range(fin[0]+1)] for _ in range(fin[1]+1)]
  seen[0][0] = True
  for o in obst:
    seen[o[0]][o[1]] = True

  for l in range(1024, len(data)):
    line = data[l]
    obst.append([int(x) for x in line.split(',')])
    seen = [[False for _ in range(fin[0]+1)] for _ in range(fin[1]+1)]
    seen[0][0] = True
    for o in obst:
      seen[o[0]][o[1]] = True
    q = deque([(0, start[0], start[1])])
    found = False
    while q:
      t, row, col = q.popleft()
      if (row, col) == fin:
        found = True
        break
      for i in range(4):
        r = row + moves[i]
        c = col + moves[i+1]
        if 0 <= r <= fin[0] and 0 <= c <= fin[1] and not seen[r][c]:
          seen[r][c] = True
          q.append((t+1, r, c))
    if not found:
      return line

  return ans


print(solve())
print(solve2())