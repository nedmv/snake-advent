import sys
from functools import cache

input = sys.argv[1] if len(sys.argv)>=2 else 'input'
data = open(input).read().strip().split('\n')

def get_digits(s):
  if str(s).len() % 2 == 0:
    return (int(str(s)[:len(str(s))//2]), int(str(s)[len(str(s))//2:]))
  else:
    return None

@cache
def get_total_stones(stone, turns):
  if turns == 0:
    return 1
  elif stone == 0:
    return get_total_stones(1, turns - 1)
  elif len(str(stone)) % 2 == 0:
    l, r = (int(str(stone)[:len(str(stone))//2]), int(str(stone)[len(str(stone))//2:]))
    return get_total_stones(l, turns - 1) + get_total_stones(r, turns - 1)
  else:
    return get_total_stones(stone * 2024, turns - 1)

def calc_stones(turns):
  ans = 0
  stones = [int(x) for x in data[0].split(' ')]
  for s in stones:
    ans += get_total_stones(s, turns)
  return ans

def solve():
  return calc_stones(25)

def solve2():
  return calc_stones(75)


print(solve())
print(solve2())

# Part 3 :)
sys.setrecursionlimit(2050)
s = calc_stones(2024)
print(s, len(str(s)))