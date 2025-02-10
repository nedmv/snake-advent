import sys
from collections import deque

def get_map(data):
  return [[data[row][col] for col in range(len(data[row]))] for row in range(len(data))]

input = sys.argv[1] if len(sys.argv)>=2 else 'input'
data = open(input).read().strip().split('\n')
m = get_map(data)
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def solve():
  ans = 0
  for row in range(len(m)):
    for col in range(len(m[row])):
      if m[row][col] == '0':
        start = (row, col)
      else:
        continue

      queue = deque([start])
      seen = set([start])

      while queue:
        x, y = queue.popleft()
        if m[x][y] == '9':
          ans += 1
        for dx, dy in dirs:
          if 0 <= x+dx < len(m) and 0 <= y+dy < len(m[row]) and (x+dx, y+dy) not in seen:
            if ord(m[x+dx][y+dy]) - ord(m[x][y]) == 1:
              queue.append((x+dx, y+dy))
              seen.add((x+dx, y+dy))
  return ans

def solve2():
  ans = 0
  for row in range(len(m)):
    for col in range(len(m[row])):
      if m[row][col] == '0':
        start = (row, col)
      else:
        continue
      start = (start[0], start[1], [])
      queue = deque([start])
      seen = set()

      while queue:
        e = queue.popleft()
        (x, y, path) = e
        if m[x][y] == '9':
          ans += 1
        for dx, dy in dirs:
          new_path = path.copy()
          new_path.append((x+dx, y+dy))
          tup = tuple(new_path)
          if 0 <= x+dx < len(m) and 0 <= y+dy < len(m[row]) and tup not in seen:
            if ord(m[x+dx][y+dy]) - ord(m[x][y]) == 1:
              e = (x+dx, y+dy, new_path)
              queue.append(e)
              seen.add(tup)
  return ans

print(solve())
print(solve2())