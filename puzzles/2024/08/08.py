import sys
from collections import defaultdict

def get_map(data):
  return [[data[row][col] for col in range(len(data[row]))] for row in range(len(data))]

input = sys.argv[1] if len(sys.argv)>=2 else 'input'
data = open(input).read().strip().split('\n')
m = get_map(data)

def solve():
  ans = 0
  antennas = defaultdict(list)

  for row in range(len(m)):
    for col in range(len(m[row])):
      if m[row][col] != '.':
        antennas[m[row][col]].append((row, col))

  antinodes = [[False for _ in range(len(m[0]))] for _ in range(len(m))]

  for ant in antennas:
    for a in antennas[ant]:
      for b in antennas[ant]:
        if a == b:
          continue
        dx = a[0] - b[0]
        dy = a[1] - b[1]

        x = a[0] + dx
        y = a[1] + dy

        if 0 <= x < len(m) and 0 <= y < len(m[0]):
          antinodes[x][y] = True

  for row in range(len(m)):
    for col in range(len(m[0])):
      if antinodes[row][col]:
        ans += 1

  return ans

def solve2():
  ans = 0
  antennas = defaultdict(list)

  for row in range(len(m)):
    for col in range(len(m[row])):
      if m[row][col] != '.':
        antennas[m[row][col]].append((row, col))

  antinodes = [[False for _ in range(len(m[0]))] for _ in range(len(m))]

  for ant in antennas:
    for a in antennas[ant]:
      for b in antennas[ant]:
        if a == b:
          continue

        dx = a[0] - b[0]
        dy = a[1] - b[1]

        x = a[0]
        y = a[1]

        while 0 <= x < len(m) and 0 <= y < len(m[0]):
          antinodes[x][y] = True
          x += dx
          y += dy



  for row in range(len(m)):
    for col in range(len(m[0])):
      if antinodes[row][col]:
        ans += 1

  return ans

print(solve())
print(solve2())