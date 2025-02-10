import sys

def get_map(data):
  return [[data[row][col] for col in range(len(data[row]))] for row in range(len(data))]

input = sys.argv[1] if len(sys.argv)>=2 else 'input'
data = open(input).read().strip().split('\n')


def parse_key(m):
  v = []
  for col in range(5):
    for row in reversed(range(6)):
      if m[row][col] == '.':
        v.append(5-row)
        break
  return v


def parse_lock(m):
  v = []
  for col in range(5):
    for row in range(1, 7):
      if m[row][col] == '.':
        v.append(row-1)
        break
  return v


def solve():
  ans = 0
  a = []
  locks = []
  keys = []
  for i in range(0, len(data), 8):
    if data[i][0] == '#':
      locks.append(get_map([data[i:i+7]]))
    else:
      keys.append(get_map([data[i:i+7]]))

  locks = [parse_lock(m[0]) for m in locks]
  keys = [parse_key(m[0]) for m in keys]

  for l in locks:
    for k in keys:
      for i in range(5):
        if l[i] + k[i] > 5:
          break
      else:
        ans += 1

  return ans


print(solve())