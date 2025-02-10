import sys

input = sys.argv[1] if len(sys.argv)>=2 else 'input'
data = open(input).read().strip().split('\n')

def calc_prize(b1, b2, prize, loc, depth):
  discr = b1[0] * b2[1] - b1[1] * b2[0]
  if discr == 0:
    return None
  p = prize
  x = b1[0] * p[1] - b1[1] * p[0]
  y = b2[1] * p[0] - b2[0] * p[1]
  if x % discr != 0 or y % discr != 0:
    return None
  x = x // discr
  y = y // discr
  if x < 0 or y < 0:
    return None
  return 3 * y + x


def solve(bonus):
  ans = 0
  d = []
  b1 = (0, 0)
  b2 = (0, 0)
  prize = (0, 0)
  for line in data:
    if line.startswith('Button A'):
      x = int(line.split("+")[1].split(",")[0])
      y = int(line.split("+")[2])
      b1 = (x, y)
    elif line.startswith('Button B'):
      x = int(line.split("+")[1].split(",")[0])
      y = int(line.split("+")[2])
      b2 = (x, y)
    elif line.startswith('Prize'):
      x = int(line.split("=")[1].split(",")[0]) + bonus
      y = int(line.split("=")[2]) + bonus
      prize = (x, y)
      c = calc_prize(b1, b2, prize, (0, 0), 0)
      if c is not None:
        ans += c
  return ans

print(solve(0))
print(solve(10000000000000))