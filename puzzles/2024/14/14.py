import sys

input = sys.argv[1] if len(sys.argv)>=2 else 'input'
data = open(input).read().strip().split('\n')
moves = [1, 0, -1, 0, 1]

def get_robots():
  robots = []
  for line in data:
    pos = [int(x) for x in line.split(" ")[0].split("=")[1].split(",")]
    vel = [int(x) for x in line.split(" ")[1].split("=")[1].split(",")]
    robots.append((pos, vel))
  return robots


def move(robots, rows, cols):
  for i in range(len(robots)):
    robots[i][0][0] += robots[i][1][0]
    if robots[i][0][0] < 0:
      robots[i][0][0] += rows
    robots[i][0][0] %= rows

    robots[i][0][1] += robots[i][1][1]
    if robots[i][0][1] < 0:
      robots[i][0][1] += cols
    robots[i][0][1] %= cols


def count_sf(robots, rows, cols):
  sf = [0, 0, 0, 0]
  for r in robots:
    if r[0][0] > rows // 2 and r[0][1] > cols // 2:
      sf[3] += 1
    elif r[0][0] > rows // 2 and r[0][1] < cols // 2:
      sf[2] += 1
    elif r[0][0] < rows // 2 and r[0][1] < cols // 2:
      sf[0] += 1
    elif r[0][0] < rows // 2 and r[0][1] > cols // 2:
      sf[1] += 1

  ans = 1
  for v in sf:
    ans *= v
  return ans


def solve():
  ans = 0
  robots = get_robots()
  rows = 101
  cols = 103
  if input != 'input':
    rows = 11
    cols = 7

  for _ in range(100):
    move(robots, rows, cols)

  return count_sf(robots, rows, cols)


def solve2():
  ans = 0
  robots = get_robots()
  n = len(robots)
  rows = 103
  cols = 101

  values_x = [0 for _ in range(n)]
  values_y = [0 for _ in range(n)]
  min_variance_x = 1e12
  min_t_x = 0
  min_variance_y = 1e12
  min_t_y = 0

  for t in range(1, cols+1):
    for i in range(n):
      robots[i][0][0] += robots[i][1][0]
      robots[i][0][0] %= cols

      if robots[i][0][0] < 0:
        robots[i][0][0] += cols
      values_x[i] = robots[i][0][0]

    mean_x = sum(values_x) // n
    variance_x = sum((x - mean_x)**2 for x in values_x)
    if variance_x < min_variance_x:
      min_variance_x = variance_x
      min_t_x = t

  for t in range(1, rows+1):
    for i in range(n):
      robots[i][0][1] += robots[i][1][1]
      robots[i][0][1] %= rows

      if robots[i][0][1] < 0:
        robots[i][0][1] += rows
      values_y[i] = robots[i][0][1]

    mean_y = sum(values_y) // n
    variance_y = sum((y - mean_y)**2 for y in values_y)
    if variance_y < min_variance_y:
      min_variance_y = variance_y
      min_t_y = t

  return min_t_x + ((51 * (rows + min_t_y - min_t_x)) % rows) * cols


print(solve())
print(solve2())