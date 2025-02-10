import sys

def get_map(data):
  return [[data[row][col] for col in range(len(data[row]))] for row in range(len(data))]

input = sys.argv[1] if len(sys.argv)>=2 else 'input'
data = open(input).read().strip().split('\n')
moves = [-1, 0, 1, 0, -1] #NESW

def solve():
  ans = 0
  m = get_map(data)
  seen = set()

  start = (0, 0)
  for row in range(len(m)):
    for col in range(len(m[row])):
      if m[row][col] == '^':
        start = (row, col, 0)
        break 
  
  while True:
    seen.add((start[0], start[1]))
    can_move = False
    d = start[2]

    while not can_move:
      next = (start[0]+moves[d], start[1]+moves[d+1], d)
      if next[0] < 0 or next[0] >= len(m) or next[1] < 0 or next[1] >= len(m[0]):
        return len(seen)

      if m[next[0]][next[1]] == '#':
        d = (d + 1) % 4
      else:
        can_move = True
        start = next

  return ans

def solve2():
  ans = 0
  m = get_map(data)
  s = (0, 0)
  for row in range(len(m)):
    for col in range(len(m[row])):
      if m[row][col] == '^':
        s = (row, col, 0)
        break 

  for i in range(len(m)):
    for j in range(len(m[i])):
      if m[i][j] == '#' or m[i][j] == '^':
        continue
      start = s
      seen = set()
      looped = True

      while (start not in seen) and looped:
        seen.add(start)
        can_move = False
        d = start[2]

        while not can_move:
          next = (start[0]+moves[d], start[1]+moves[d+1], d)
          if next[0] < 0 or next[0] >= len(m) or next[1] < 0 or next[1] >= len(m[0]):
            looped = False
            break

          if m[next[0]][next[1]] == '#' or (next[0] == i and next[1] == j):
            d = (d + 1) % 4
          else:
            can_move = True
            start = next
      if looped:
        ans += 1

  return ans

print(solve())
print(solve2())