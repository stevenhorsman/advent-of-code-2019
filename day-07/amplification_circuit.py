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
    
    amps[0].put_input(0) # starting input to A
      # amps[i].execute()
    
    for i in range(0, len(amps)):
      out = next(amps[i].execute_concurrent(True))
      #out = amps[i].get_output()
      # out = amps[i].get_output()
      amps[(i+1) % 5].put_input(out)
    vals.append(amps[0].inputs.get())
  return max(vals)

def part2(memory):
  program = memory.split(",").copy()
  vals = []
  perms = permutations([5,6,7,8,9]) 
  # perms = [[9,8,7,6,5]]
  for states in list(perms):
    amps = []
    for i in range(0, 5):
      amps.append(ShipComputer(program, states[i]))
    
    amps[0].put_input(0) # starting input to A
      # amps[i].execute()
    try:
      i = 0
      while True:
    # for i in range(0, len(amps)):
        out = next(amps[i].execute_concurrent(True))
        #out = amps[i].get_output()
        # out = amps[i].get_output()
        i = (i+1) % 5
        amps[i].put_input(out)
    except StopIteration:
      vals.append(amps[0].inputs.get())
  return max(vals)

if __name__ == "__main__":
    with open(input_file) as f:
       data = f.read()
    print("Part 1: ", part1(data))
    print("Part 2: ", part2(data))