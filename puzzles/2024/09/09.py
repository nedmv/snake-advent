import sys

input = sys.argv[1] if len(sys.argv)>=2 else 'input'
data = open(input).read().strip().split('\n')


def solve():
  ans = 0
  unzipped = []
  is_file = True
  id = 0
  for l in data[0]:
    l = int(l)
    if is_file:
      for i in range(l):
        unzipped.append(id)
      id += 1
    else:
      for i in range(l):
        unzipped.append(-1)
    is_file = not is_file

  l = 0
  r = len(unzipped)-1
  while l < r:

    if unzipped[l] != -1:
      l += 1
      continue
    if unzipped[r] == -1:
      r -= 1
      continue
    unzipped[l] = unzipped[r]
    unzipped[r] = -1
    l += 1
    r -= 1

  for i in range(len(unzipped)):
    if unzipped[i] != -1:
      ans += i * unzipped[i]

  return ans

def solve2():
  ans = 0
  sizes = []
  files = []
  is_file = True
  id = 0
  for l in data[0]:
    l = int(l)
    sizes.append(l)
    if is_file:
      files.append(id)
      id += 1
    else:
      files.append(-1)
    is_file = not is_file

  pos = len(files) - 1
  while pos > 0:
    if files[pos] != -1:
      found = False
      for i in range(pos):
        if files[i] == -1 and sizes[i] >= sizes[pos]:
          found = True
          diff = sizes[i] - sizes[pos]
          files[i] = files[pos]
          sizes[i] = sizes[pos]
          files[pos] = -1
          if diff > 0:
            files.insert(i+1, -1)
            sizes.insert(i+1, diff)
          else:
            pos -= 1
          break
      if not found:
        pos -= 1
    else:
      pos -= 1

  pos = 0
  for f in range(len(files)):
    if files[f] != -1:
      for i in range(sizes[f]):
        ans += pos * files[f]
        pos += 1
    else:
      for i in range(sizes[f]):
        pos += 1

  return ans


print(solve())
print(solve2())