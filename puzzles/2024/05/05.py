import sys
from collections import defaultdict, deque

input = sys.argv[1] if len(sys.argv)>=2 else 'input'
data = open(input).read().strip().split('\n')

def solve():
  rules = []
  reports = []
  p2 = False
  for line in data:
    if line == '':
      p2 = True
      continue
    if not p2:
      rules.append((int(line.split('|')[0]), int(line.split('|')[1])))
    else:
      reports.append([int(x) for x in line.split(',')])

  ans = 0
  total = 0

  for report in reports:
    correct = True
    for rule in rules:
      if rule[0] in report and rule[1] in report:
        if report.index(rule[0]) > report.index(rule[1]):
          correct = False
          break
    if correct:
      ans += report[len(report) // 2]
      total += 1

  return ans

def order(rules, report):
  adj = defaultdict(list)
  total = defaultdict(int)

  for r in report:
    adj[r] = []
    total[r] = 0

  for rule in rules:
    if rule[0] in report and rule[1] in report:
      adj[rule[0]].append(rule[1])
      total[rule[1]] += 1

  ordered = []
  q = deque()
  for k in total:
    if total[k] == 0:
      q.append(k)
  while len(q) > 0:
    e = q.popleft()
    ordered.append(e)
    for v in adj[e]:
      total[v] -= 1
      if total[v] == 0:
        q.append(v)
  return ordered[len(ordered) // 2]

def solve2():
  rules = []
  reports = []
  p2 = False
  for line in data:
    if line == '':
      p2 = True
      continue
    if not p2:
      rules.append((int(line.split('|')[0]), int(line.split('|')[1])))
    else:
      reports.append([int(x) for x in line.split(',')])

  ans = 0

  for report in reports:
    correct = True
    for rule in rules:
      if rule[0] in report and rule[1] in report:
        if report.index(rule[0]) > report.index(rule[1]):
          correct = False
          break
    if not correct:
      ans += order(rules, report)
  return ans

print(solve())
print(solve2())