import sys

input = sys.argv[1] if len(sys.argv)>=2 else 'input'
data = open(input).read().strip().split('\n')


def check(target, nums, pos, cur):
  if pos == len(nums):
    return cur == target
  return check(target, nums, pos + 1, cur + nums[pos]) or check(target, nums, pos + 1, cur * nums[pos])


def solve():
  ans = 0

  for line in data:
    target = int(line.split(': ')[0])
    nums = [int(x) for x in line.split(': ')[1].split(' ')]
    if check(target, nums, 1, nums[0]):
      ans += target

  return ans


def check2(target, nums, pos, cur):
  if cur > target:
    return False
  if pos == len(nums):
    return cur == target

  t = nums[pos]
  count = 0
  while t > 0:
    t //= 10
    count += 1

  mul = 10 ** count

  return check2(target, nums, pos + 1, cur + nums[pos]) or check2(target, nums, pos + 1, cur * nums[pos]) or check2(target, nums, pos + 1, cur * mul + nums[pos])


def solve2():
  ans = 0

  for line in data:
    target = int(line.split(': ')[0])
    nums = [int(x) for x in line.split(': ')[1].split(' ')]
    if check2(target, nums, 1, nums[0]):
      ans += target

  return ans


print(solve())
print(solve2())