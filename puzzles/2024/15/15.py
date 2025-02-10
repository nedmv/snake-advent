import sys
from collections import deque

moves = [-1, 0, 1, 0, -1] #NESW

def get_map(data):
  return [[data[row][col] for col in range(len(data[row]))] for row in range(len(data))]

input = sys.argv[1] if len(sys.argv)>=2 else 'input'
data = open(input).read().strip().split('\n')

def get_dir(ch):
  d = (0, 0)
  match ch:
    case '^':
      d = (-1, 0)
    case '>':
      d = (0, 1)
    case 'v':
      d = (1, 0)
    case '<':
      d = (0, -1)
  return d

def solve():
  ans = 0
  split = 50 if input == "input" else 10
  m = get_map(data[:split])
  act = data[split+1:]

  s = ''
  for line in act:
    s += line
  start = (0, 0)
  for row in range(len(m)):
    for col in range(len(m[0])):
      if m[row][col] == '@':
        start = (row, col)
        break

  for ch in s:
    row, col = start
    r, c = row, col
    d = get_dir(ch)
    
    if 0 <= r < len(m) and 0 <= c < len(m[0]):
      can_move = True
      r = row + d[0]
      c = col + d[1]
      while m[r][c] == 'O':
        r += d[0]
        c += d[1]
      if m[r][c] == '#':
        can_move = False

      if can_move:
        m[row][col] = '.'
        next_r = row + d[0]
        next_c = col + d[1]
        start = (next_r, next_c)
        m[row + d[0]][col + d[1]] = '@'
        while next_r != r or next_c != c:
          next_r += d[0]
          next_c += d[1]
          m[next_r][next_c] = 'O'

  for row in range(len(m)):
    for col in range(len(m[0])):
      if m[row][col] == 'O':
        ans += row * 100 + col

  return ans


def scale(m):
  ans = [['.' for _ in range(2 * len(m[0]))] for _ in range(len(m))]
  for r in range(len(m)):
    for c in range(len(m[0])):
      match m[r][c]:
        case '#':
          ans[r][2*c] = '#'
          ans[r][2*c+1] = '#'
        case '.':
          ans[r][2*c] = '.'
          ans[r][2*c+1] = '.'
        case '@':
          ans[r][2*c] = '@'
          ans[r][2*c+1] = '.'
        case 'O':
          ans[r][2*c] = '['
          ans[r][2*c+1] = ']'
  return ans


def solve2():
  ans = 0
  split = 50 if input == "input" else 10
  m = get_map(data[:split])
  act = data[split+1:]

  m = scale(m)
  s = ''
  for line in act:
    s += line
  start = (0, 0)
  for row in range(len(m)):
    for col in range(len(m[0])):
      if m[row][col] == '@':
        start = (row, col)
        break

  for ch in s:
    row, col = start
    r, c = row, col
    d = get_dir(ch)

    if 0 <= r < len(m) and 0 <= c < len(m[0]):
      can_move = True
      q = deque([(row, col)])
      seen = set([(row, col)])
      moved = []
      changes = []
      while q:
        r, c = q.popleft()
        if m[r][c] == '@':
          q.append((r+d[0], c+d[1]))
        elif m[r][c] == '[':
          next_r = r+d[0]
          next_c = c+d[1]
          if (next_r, next_c) not in seen:
            q.append((next_r, next_c))
            seen.add((next_r, next_c))
          next_r = r
          next_c = c+1
          if (next_r, next_c) not in seen:
            q.append((next_r, next_c))
            seen.add((next_r, next_c))
        elif m[r][c] == ']':
          next_r = r+d[0]
          next_c = c+d[1]
          if (next_r, next_c) not in seen:
            q.append((next_r, next_c))
            seen.add((next_r, next_c))
          next_r = r
          next_c = c-1
          if (next_r, next_c) not in seen:
            q.append((next_r, next_c))
            seen.add((next_r, next_c)) 
        elif m[r][c] == '#':
          can_move = False
          break
        if m[r][c] in '@[]':
          moved.append((r, c))
          changes.append((r+d[0], c+d[1], m[r][c]))
      if not can_move:
        continue

      for (r, c) in moved:
        m[r][c] = '.'
      for (r, c, ch) in changes:
        m[r][c] = ch
      start = (row+d[0], col + d[1])

  for row in range(len(m)):
    for col in range(len(m[0])):
      if m[row][col] == '[':
        ans += row * 100 + col

  return ans


print(solve())
print(solve2())