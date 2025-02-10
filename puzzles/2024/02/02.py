import sys

input = sys.argv[1] if len(sys.argv)>=2 else 'input'
data = open(input).read().strip().split('\n')

def solve(part2 = False):
  ans = 0
  for line in data:
    s = [int(x) for x in line.split()]
    safe = True
    inc = 0
    for i in range(len(s)-1):
      diff = s[i+1] - s[i]
      if abs(diff) < 1 or abs(diff) > 3:
          safe = False
          break
      if diff < 0:
        if inc == 0:
          inc = 1
        elif inc == 2:
            safe = False
            break
      elif diff > 0:
        if inc == 0:
          inc = 2
        elif inc == 1:
            safe = False
            break
    if safe:
      ans += 1
    elif part2:
      for ig in range(len(s)):
        safe = True
        inc = 0
        new_s = s.copy()
        del new_s[ig]
        for i in range(len(s)-2):
          diff = new_s[i+1] - new_s[i]
          if abs(diff) < 1 or abs(diff) > 3:
              safe = False
              break
          if diff < 0:
            if inc == 0:
              inc = 1
            elif inc == 2:
                safe = False
                break
          elif diff > 0:
            if inc == 0:
              inc = 2
            elif inc == 1:
                safe = False
                break
        if safe:
          ans += 1
          break
  return ans


print(solve())
print(solve(part2=True))