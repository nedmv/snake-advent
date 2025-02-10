import sys
from collections import deque

moves = [-1, 0, 1, 0, -1] #NESW

def get_map(data):
  return [[data[row][col] for col in range(len(data[row]))] for row in range(len(data))]

input = sys.argv[1] if len(sys.argv)>=2 else 'input'
data = open(input).read().strip().split('\n')
m = get_map(data)

def get_start_and_fin(m):
  rows = len(m)
  cols = len(m[0])
  start = (0, 0)
  fin = (0, 0)
  for row in range(rows):
    for col in range(cols):
      if m[row][col] == 'S':
        start = (row, col)
      if m[row][col] == 'E':
        fin = (row, col)
  return start, fin

def fill(m, rows, cols, start):
  d = [[0 for _ in range(cols)] for _ in range(rows)]
  d[start[0]][start[1]] = 1e6

  q = deque([(0, start[0], start[1])])
  while q:
    (cost, row, col) = q.popleft()

    for i in range(4):
      r = row + moves[i]
      c = col + moves[i+1]
      if 0 <= r < rows and 0 <= c < cols and m[r][c] != '#' and d[r][c] == 0:
        d[r][c] = cost + 1
        q.append((cost+1, r, c))
  d[start[0]][start[1]] = 0
  return d


def solve(cheat_limit):
  rows = len(m)
  cols = len(m[0])

  start, fin = get_start_and_fin(m)
  d_from_start = fill(m, rows, cols, start)
  d_from_fin = fill(m, rows, cols, fin)
  no_cheat_cost = d_from_start[fin[0]][fin[1]]

  ans = 0
  for sr in range(1, rows-1):
    for sc in range(1, cols-1):
      if m[sr][sc] == '#':
        continue
      for fr in range(1, rows-1):
        for fc in range(1, cols-1):
          if m[fr][fc] == '#':
            continue
          dist = abs(sr-fr) + abs(sc - fc)
          if dist > cheat_limit:
            continue
          effect = d_from_start[sr][sc] + d_from_fin[fr][fc] + dist
          diff = no_cheat_cost - effect
          if diff >= 100:
            ans += 1
  return ans


print(solve(2))
print(solve(20))