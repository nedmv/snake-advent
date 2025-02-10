import sys

input = sys.argv[1] if len(sys.argv)>=2 else 'input'
data = open(input).read().strip().split('\n')

def get_map(data):
  return [[data[row][col] for col in range(len(data[row]))] for row in range(len(data))]

def down(m, i, j):
  return i < len(m) - 3 and m[i+1][j] == 'M' and m[i+2][j] == 'A' and m[i+3][j] == 'S'

def right(m, i, j):
  return j < len(m[i]) - 3 and m[i][j+1] == 'M' and m[i][j+2] == 'A' and m[i][j+3] == 'S'

def left(m, i, j):
  return j > 2 and m[i][j-1] == 'M' and m[i][j-2] == 'A' and m[i][j-3] == 'S'

def up(m, i, j):
  return i > 2 and m[i-1][j] == 'M' and m[i-2][j] == 'A' and m[i-3][j] == 'S'

def up_right(m, i, j):
  return i > 2 and j < len(m[i]) - 3 and m[i-1][j+1] == 'M' and m[i-2][j+2] == 'A' and m[i-3][j+3] == 'S'

def up_left(m, i, j):
  return i > 2 and j > 2 and m[i-1][j-1] == 'M' and m[i-2][j-2] == 'A' and m[i-3][j-3] == 'S'

def down_right(m, i, j):
  return i < len(m) - 3 and j < len(m[i]) - 3 and m[i+1][j+1] == 'M' and m[i+2][j+2] == 'A' and m[i+3][j+3] == 'S'

def down_left(m, i, j):
  return i < len(m) - 3 and j > 2 and m[i+1][j-1] == 'M' and m[i+2][j-2] == 'A' and m[i+3][j-3] == 'S'

def search(m, i, j):
  ans = 0
  ans += down(m, i, j)
  ans += right(m, i, j)
  ans += left(m, i, j)
  ans += up(m, i, j)
  ans += up_right(m, i, j)
  ans += up_left(m, i, j)
  ans += down_right(m, i, j)
  ans += down_left(m, i, j)
  return ans

def solve():
  m = get_map(data)
  ans = 0
  for i in range(len(m)):
    for j in range(len(m[i])):
      if m[i][j] == 'X':
        ans += search(m, i, j)

  return ans

def search2(m, i, j):
  return ((m[i-1][j-1] == 'M' and m[i+1][j+1] == 'S') or (m[i-1][j-1] == 'S' and m[i+1][j+1] == 'M')) \
     and ((m[i-1][j+1] == 'M' and m[i+1][j-1] == 'S') or (m[i-1][j+1] == 'S' and m[i+1][j-1] == 'M'))

def solve2():
  m = get_map(data)
  ans = 0
  for i in range(1, len(m)-1):
    for j in range(1, len(m[i])-1):
      if m[i][j] == 'A':
        ans += search2(m, i, j)

  return ans

print(solve())
print(solve2())