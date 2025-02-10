import sys
from collections import deque

def get_map(data):
  return [[data[row][col] for col in range(len(data[row]))] for row in range(len(data))]

input = sys.argv[1] if len(sys.argv)>=2 else 'input'
data = open(input).read().strip().split('\n')
m = get_map(data)
moves = [1, 0, -1, 0, 1]


def solve():
  ans = 0
  seen = [[False for _ in range(len(m[0]))] for _ in range(len(m))]
  for row in range(len(m)):
    for col in range(len(m[row])):
      if not seen[row][col]:
        seen[row][col] = True
        target = m[row][col]
        q = deque([(row, col)])
        region = [(row, col)]
        while q:
          r, c = q.popleft()
          for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
            if 0<=nr<len(m) and 0<=nc<len(m[nr]) and m[nr][nc] == target and not seen[nr][nc]:
              seen[nr][nc] = True
              region.append((nr, nc))
              q.append((nr, nc))
        sq = len(region)
        perim = 0
        for r, c in region:
          perim += 4
          for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
            if 0<=nr<len(m) and 0<=nc<len(m[nr]) and m[nr][nc] == target:
              perim -= 1
        ans += sq * perim

  return ans

def solve2():
  ans = 0
  seen = [[False for _ in range(len(m[0]))] for _ in range(len(m))]
  has_border = [[[False, False, False, False] for _ in range(len(m[0]))] for _ in range(len(m))]
  for row in range(len(m)):
    for col in range(len(m[row])):
      for i in range(4):
        nr = row + moves[i]
        nc = col + moves[i+1]
        if nr < 0 or nr >= len(m) or nc < 0 or nc >= len(m[nr]) or m[nr][nc] != m[row][col]:
          has_border[row][col][i] = True
  for row in range(len(m)):
    for col in range(len(m[row])):
      if not seen[row][col]:
        seen[row][col] = True
        target = m[row][col]
        q = deque([(row, col)])
        region = [(row, col)]
        while q:
          r, c = q.popleft()
          for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
            if 0<=nr<len(m) and 0<=nc<len(m[nr]) and m[nr][nc] == target and not seen[nr][nc]:
              seen[nr][nc] = True
              region.append((nr, nc))
              q.append((nr, nc))
        sq = len(region)
        borders = 0

        min_r = min(region, key=lambda x: x[0])[0]
        min_c = min(region, key=lambda x: x[1])[1]
        max_r = max(region, key=lambda x: x[0])[0]
        max_c = max(region, key=lambda x: x[1])[1]

        for r in range(min_r, max_r+1):
          for c in range(min_c, max_c+1):
            if (r, c) in region:
              for i in range(4):
                if has_border[r][c][i]:
                  borders += 1
                  nr = r + moves[(i+3)%4]
                  nc = c + moves[i]
                  # ignore this border if previous element in this direction had it
                  if 0 <= nr < len(m) and 0 <= nc < len(m[nr]) and m[nr][nc] == target and has_border[nr][nc][i]:
                    borders -= 1

        ans += sq * borders

  return ans

print(solve())
print(solve2())