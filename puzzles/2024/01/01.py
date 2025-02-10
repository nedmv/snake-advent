import sys

input = sys.argv[1] if len(sys.argv)>=2 else 'input'
data = open(input).read().strip().split('\n')

def get_lists():
  l1 = []
  l2 = []
  for line in data:
    s = line.split()
    l1.append(int(s[0]))
    l2.append(int(s[1]))
  return l1, l2

def solve():
  l1, l2 = get_lists()
  l1.sort()
  l2.sort()
  ans = 0
  for i in range(len(l1)):
    ans += abs(l1[i] - l2[i])
  return ans

def solve2():
  l1, l2 = get_lists()
  ans = 0
  for i in range(len(l1)):
    t = l1[i]
    times = 0
    for j in range(len(l2)):
      if l2[j] == t:
        times += 1
    ans += t * times
  return ans

print(solve())
print(solve2())