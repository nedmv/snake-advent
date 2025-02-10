import sys

input = sys.argv[1] if len(sys.argv)>=2 else 'input'
data = open(input).read().strip().split('\n')


def parse():
  p2 = False
  vals = {}
  ops = []
  for line in data:
    if len(line) == 0:
      p2 = True
      continue
    if not p2:
      if line[0] == 'x':
        # x.append(True if line[5] == '1' else False)
        vals[line[0:3]] = int(line[5])
      else:
        # y.append(True if line[5] == '1' else False)
        vals[line[0:3]] = int(line[5])
    else:
      l = line.split(" ")
      ops.append((l[0], l[1], l[2], l[4]))
  return vals, ops


def solve():
  vals, ops = parse()

  changed = True
  while changed:
    changed = False
    for a, op, b, tg in ops:
      if a in vals and b in vals and tg not in vals:
        match op:
          case 'AND':
            vals[tg] = vals[a] & vals[b]
          case 'OR':
            vals[tg] = vals[a] | vals[b]
          case 'XOR':
            vals[tg] = vals[a] ^ vals[b]
        changed = True

  z = []
  for i in range(10):
    z.append(vals[f"z0{i}"])
  for i in range(10, 46):
    z.append(vals[f"z{i}"])

  mul = 1
  ans = 0
  for e in z:
    ans += mul * e
    mul *= 2
  return ans


def solve2():
  vals, ops = parse()

  limit = len(vals) // 2
  swaps = []

  for a, op, b, out in ops:
    if out[0] == 'z' and op != "XOR" and out[1::] != str(limit):
      swaps.append(out)
      continue
    match op:
      case "XOR":
        if out[0] < 'x' and a[0] < 'x' and b[0] < 'x':
          swaps.append(out)
          continue
        for inner_a, inner_op, inner_b, _ in ops:
          if inner_op == "OR" and (out == inner_a or out == inner_b):
            swaps.append(out)
            break
      case "AND":
        if a == "x00" or b == "x00":
          continue
        for inner_a, inner_op, inner_b, _ in ops:
          if inner_op != "OR" and (out == inner_a or out == inner_b):
            swaps.append(out)
            break

  return ",".join(sorted(swaps))


print(solve())
print(solve2()) 