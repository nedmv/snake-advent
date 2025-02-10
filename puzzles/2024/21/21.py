import sys
from functools import cache
from queue import PriorityQueue
from copy import copy

moves = [-1, 0, 1, 0, -1] #NESW

input = sys.argv[1] if len(sys.argv)>=2 else 'input'
data = open(input).read().strip().split('\n')

keypads = [('789','456','123','#0A'),('#^A','<v>')] # numeric, directional
move_sym = '^>v<'


@cache
def find_best_path_by_cost(start_c, fin_c, id):
  keypad = keypads[id]
  rows = len(keypad)
  cols = len(keypad[0])

  seen = [[1e21 for _ in range(cols)] for _ in range(rows)]
  start = (0, 0)
  fin = (0, 0)
  for r in range(rows):
    for c in range(cols):
      if keypad[r][c] == start_c:
        start = (r, c)
        seen[r][c] = 0
      if keypad[r][c] == fin_c:
        fin = (r, c)

  q = PriorityQueue()
  q.put((0, start[0], start[1], ''))
  paths = []
  limit = int(1e21)

  while not q.empty():
    cost, row, col, path = q.get()
    if cost > limit:
      break
    if (row, col) == fin:
      limit = cost
      paths.append(path)
      continue
  
    for i in range(4):
      r = row + moves[i]
      c = col + moves[i+1]

      if 0 <= r < rows and 0 <= c < cols and keypad[r][c] != '#':
        new_cost = cost + 1
        if seen[r][c] >= new_cost:
          seen[r][c] = new_cost
          q.put((new_cost, r, c, path + move_sym[i]))
  return paths

@cache
def operate_keypad_by_best_cost(code, id):
  paths = ['']
  next = []
  start_c = 'A'
  lim = 1e21
  for c in code:
    cur_paths = find_best_path_by_cost(start_c, c, id)
    for p in paths:
      for cp in cur_paths:
        next.append(p+cp+'A')
    paths = copy(next)
    next = []
    start_c = c
  return paths

@cache
def find_optimal_solution(path, depth):
  if depth == 0:
    return len(path)
  ans = 0
  prev = 'A'

  for ch in path:
    next_paths = find_best_path_by_cost(prev, ch, 1)
    prev = ch
    cur_min = int(1e21)
    for p in next_paths:
      cur_min = min(cur_min, find_optimal_solution(p+'A', depth-1))
    ans += cur_min
  return ans


def enter_code(code, depth):
  paths = operate_keypad_by_best_cost(code, 0)
  best = 1e21
  for path in paths:
    best = min(best, find_optimal_solution(path, depth))
  return best

def solve(depth):
  codes = []
  for line in data:
    codes.append(line)

  ans = 0
  for code in codes:
    l = enter_code(code, depth)
    ans += l * int(code[:len(code)-1])
  return ans


print(solve(2))
print(solve(25))