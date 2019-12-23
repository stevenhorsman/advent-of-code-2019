from ship_computer import ShipComputer
from collections import deque
import sys

input_file = 'day-23/input.txt'

def run_nics(memory, exit_on_255 = False):
  memory = memory.split(",")
  computers = [0] * 50

  nat = [None,None]
  prev_nat_y = None

  queue = [deque() for _ in range(50)]

  for i in range(50):
    computers[i] = ShipComputer(memory, i)
    computers[i].execute_until_blocked()

  try:
    while True:
      idle = True
      for i in range(50):
        computers[i].execute_until_blocked()

        if queue[i]:
          idle = False
          while queue[i]:
            computers[i].put_input(queue[i].popleft())
        else:
          computers[i].put_input(-1)

        if computers[i].output.qsize() >=3:
          idle = False
          outputs = computers[i].get_all_outputs()
          while len(outputs) >= 3:
            address, x, y = outputs.pop(0), outputs.pop(0), outputs.pop(0)
            if address == 255:
              if exit_on_255:
                return y
              else:
                nat = [x,y]
            else:
              queue[address].extend([x,y])

      if idle and nat[0] != None:
        if nat[1] == prev_nat_y:
          return nat[1]
        else:
          queue[0].extend(nat)
          prev_nat_y = nat[1]
  except StopIteration:
    return -1

def part1(memory):
  return run_nics(memory, True)

def part2(memory):
  return run_nics(memory)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  # print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))
