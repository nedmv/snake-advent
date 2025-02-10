import sys
from queue import PriorityQueue
from copy import copy

moves = [-1, 0, 1, 0, -1] #NESW

def get_map(data):
  return [[data[row][col] for col in range(len(data[row]))] for row in range(len(data))]

input = sys.argv[1] if len(sys.argv)>=2 else 'input'
data = open(input).read().strip().split('\n')
m = get_map(data)

def get_start_and_fin(m):
  start = (0, 0)
  fin = (0, 0)
  rows = len(m)
  cols = len(m[0])
  for row in range(rows):
    for col in range(cols):
      if m[row][col] == 'S':
        start = (row, col)
      if m[row][col] == 'E':
        fin = (row, col)
  return start, fin


def solve():
  seen = [[[1e9, 1e9, 1e9, 1e9] for _ in range(len(m[0]))] for _ in range(len(m))]
  start, fin = get_start_and_fin(m)
  q = PriorityQueue()
  q.put((0, start[0], start[1], 1))

  while q:
    score, row, col, d = q.get()
    if (row, col) == fin:
      return score

    new_d = d
    r = row + moves[new_d]
    c = col + moves[new_d+1]
    sc = score + 1
    if (
        0 <= r < len(m)
        and 0 <= c < len(m[0])
        and m[r][c] != "#"
        and seen[r][c][new_d] >= sc
    ):
      seen[r][c][new_d] = sc
      q.put((sc, r, c, new_d))
    
    new_d = (d + 1) % 4
    r = row + moves[new_d]
    c = col + moves[new_d+1]
    sc = score + 1000 + 1
    if (
        0 <= r < len(m)
        and 0 <= c < len(m[0])
        and m[r][c] != "#"
        and seen[r][c][new_d] >= sc
    ):
      seen[r][c][new_d] = sc
      q.put((sc, r, c, new_d))

    new_d = (d + 3) % 4
    r = row + moves[new_d]
    c = col + moves[new_d+1]
    sc = score + 1000 + 1
    if (
        0 <= r < len(m)
        and 0 <= c < len(m[0])
        and m[r][c] != "#"
        and seen[r][c][new_d] >= sc
    ):
      seen[r][c][new_d] = sc
      q.put((sc, r, c, new_d))

def solve2():
  seen = [[[1e9, 1e9, 1e9, 1e9] for _ in range(len(m[0]))] for _ in range(len(m))]
  start, fin = get_start_and_fin(m)
  q = PriorityQueue()
  q.put((0, start[0], start[1], 1, [(start[0], start[1])]))
  limit = 1e9
  paths = []

  while q:
    score, row, col, d, path = q.get()
    if score > limit:
      break
    if (row, col) == fin:
      limit = score
      paths.append(path)
      continue

    new_d = d
    r = row + moves[new_d]
    c = col + moves[new_d+1]
    sc = score + 1
    new_p = copy(path)
    if (
        0 <= r < len(m)
        and 0 <= c < len(m[0])
        and m[r][c] != "#"
        and seen[r][c][new_d] + 1000 > sc
    ):
      new_p.append((r, c))
      if seen[r][c][new_d] > sc:
        seen[r][c][new_d] = sc
      q.put((sc, r, c, new_d, new_p))
      
    new_d = (d + 1) % 4
    r = row + moves[new_d]
    c = col + moves[new_d+1]
    sc = score + 1000 + 1
    new_p = copy(path)
    if (
        0 <= r < len(m)
        and 0 <= c < len(m[0])
        and m[r][c] != "#"
        and seen[r][c][new_d] + 1000 > sc
    ):
      new_p.append((r, c))
      if seen[r][c][new_d] > sc:
        seen[r][c][new_d] = sc
      q.put((sc, r, c, new_d, new_p))

    new_d = (d + 3) % 4
    r = row + moves[new_d]
    c = col + moves[new_d+1]
    sc = score + 1000 + 1
    new_p = copy(path)
    if (
        0 <= r < len(m)
        and 0 <= c < len(m[0])
        and m[r][c] != "#"
        and seen[r][c][new_d] + 1000 > sc
    ):
      new_p.append((r, c))
      if seen[r][c][new_d] > sc:
        seen[r][c][new_d] = sc
      q.put((sc, r, c, new_d, new_p))

  uniq = set()
  for p in paths:
    for e in p:
      uniq.add(e)
  return len(uniq)


print(solve())
print(solve2())