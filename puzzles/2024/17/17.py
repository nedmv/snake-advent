import sys

input = sys.argv[1] if len(sys.argv)>=2 else 'input'
data = open(input).read().strip().split('\n')

class Register:
  A = 0
  B = 0
  C = 0

def parse_program():
  return [int(x) for x in data[4].split(" ")[1].split(",")]

def get_combo_operand(op, registers: Register):
  val = 0
  match op:
    case 4:
      val = registers.A
    case 5:
      val = registers.B
    case 6:
      val = registers.C
    case 7:
      print("invalid")
    case _:
      val = op
  return val

def get_new_val(op, registers: Register):
  return registers.A // pow(2, get_combo_operand(op, registers))

def run_once(prog, registers):
  printed = 0
  for i in range(0, len(prog), 2):
    op = prog[i+1]
    match prog[i]:
      case 0:
        registers.A = get_new_val(op, registers)
      case 1:
        registers.B ^= op
      case 2:
        registers.B = get_combo_operand(op, registers) % 8
      case 3:
        pass # use input property to not implement proper jump
      case 4:
        registers.B ^= registers.C
      case 5:
        printed = get_combo_operand(op, registers) % 8
      case 6:
        registers.B = get_new_val(op, registers)
      case 7:
        registers.C = get_new_val(op, registers)
      case _:
        print("invalid op")
  return printed


def solve():
  registers = Register()
  registers.A = int(data[0].split(" ")[2])
  prog = parse_program()

  output = []
  while registers.A != 0:
    output.append(chr(ord('0')+run_once(prog, registers)))
  return ','.join(output)

def solve2():
  registers = Register()
  prog = parse_program()
  candidates = [(len(prog)-1, 0)]
  possible_ans = None

  while len(candidates) > 0:
    pos, val = candidates.pop()
    for cur in reversed(range(val*8, (val+1)*8)):
      registers.A = cur
      registers.B = 0
      registers.C = 0
      if run_once(prog, registers) == prog[pos]:
        if pos == 0:
          possible_ans = cur
        else:
          candidates.append((pos-1, cur))
    if possible_ans != None:
      return possible_ans
  return 0


print(solve())
print(solve2())