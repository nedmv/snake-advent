import sys
import re

input = sys.argv[1] if len(sys.argv)>=2 else 'input'
data = open(input).read().strip().split('\n')


def solve():
  ans = 0
  for line in data:
    items = re.findall(r"mul\((\d+),(\d+)\)", line)
    for item in items:
      ans += int(item[0]) * int(item[1])
  return ans


def solve2():
  ans = 0
  enabled = True
  for line in data:
    p = re.compile(r"mul\((\d+),(\d+)\)")
    do = re.compile(r"do\(\)")
    dont = re.compile(r"don't\(\)")
    do_ranges = []
    dont_ranges = []
    for m in do.finditer(line):
      do_ranges.append(m.start())
    for m in dont.finditer(line):
      dont_ranges.append(m.start())

    p1 = 0
    p2 = 0


    nums = []
    for m in p.finditer(line):
      nums.append((m.start(), int(m.group(1)), int(m.group(2))))
    p_nums = 0

    for i in range(len(line)):
      if p1 < len(do_ranges) and i == do_ranges[p1]:
        enabled = True
        p1 += 1
      if p2 < len(dont_ranges) and i == dont_ranges[p2]:
        enabled = False
        p2 += 1
      if p_nums < len(nums) and i == nums[p_nums][0]:
        if enabled:
          ans += nums[p_nums][1] * nums[p_nums][2]
        p_nums += 1

  return ans


print(solve())
print(solve2())