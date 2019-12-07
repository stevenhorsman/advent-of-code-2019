from ship_computer import ShipComputer
from itertools import permutations 

input_file = 'day-07/input.txt'

def part1(memory):
  program = memory.split(",").copy()
  vals = []
  perms = permutations([0, 1, 2, 3, 4]) 
  # perms = [[4,3,2,1,0]]
  for states in list(perms):
    amps = []
    for i in range(0, 5):
      amps.append(ShipComputer(program, states[i]))
    
    inputs = [0] * 5 # Initial puzzle input
    for i in range(0, len(amps)):
      amps[i].put_input(inputs[i])
      amps[i].execute()
      out = amps[i].get_output()
      inputs[(i+1) % 5] = out
    vals.append(inputs[0])
  return max(vals)

def part2(memory):
  program = memory.split(",").copy()
  vals = []
  # perms = permutations([5,6,7,8,9]) 
  perms = [[9,8,7,6,5]]
  for states in list(perms):
    amps = []
    for i in range(0, 5):
      amps.append(ShipComputer(program, states[i], True))
    
    inputs = [0] * 5 # Initial puzzle input
    try:
      while True:
        for i in range(0, len(amps)):
          amps[i].put_input(inputs[i])
          amps[i].execute()
          out = amps[i].get_output()
          inputs[(i+1) % 5] = out
    except StopIteration:
      vals.append(inputs[0])
  print('vals',vals)
  return max(vals)

if __name__ == "__main__":
    with open(input_file) as f:
       data = f.read()
    print("Part 1: ", part1(data))
    print("Part 2: ", part2(data))