import itertools
import math

input_file = 'day-16/input.txt'

base_pattern = [0,1,0,-1]

def transmission(input, phases = 100):
  curr_phase = [int(char) for char in input]
  for i in range(0,phases):
    new_phase = []
    for j in range(0,len(input)):
      pattern_length = (j+1) * len(base_pattern)
      patten_repeats = math.ceil(len(input) / pattern_length)
      total = 0
      for k in range(0,patten_repeats):
        # first j chars = 0, j -> 2j+1 = 1, 3j+2 -> 4j+3 = -1
        offset = k * pattern_length
        total += sum(curr_phase[offset + j: offset + (2*j) + 1])
        total -= sum(curr_phase[offset + (3*j) + 2: offset + (4*j) + 3])
      new_phase.append(abs(total) % 10)
    curr_phase = new_phase
  return curr_phase

def part1(input, phases = 100):
  curr_phase = transmission(input, phases)
  return "".join(map(str, curr_phase[0:8]))

# Hack from reddit to show that we can just use a partial sum calculation
def transmission2(input, phases = 100):
  curr_phase = [int(char) for char in input]
  # value(digit, phase) = value(digit + 1, phase) + value(digit, phase - 1)
  for i in range(0,phases):
    partial_sum = sum(curr_phase)
    for j in range(0, len(input)):
        curr_num = curr_phase[j]
        curr_phase[j] = abs(partial_sum) % 10
        partial_sum -= curr_num
  return curr_phase

def part2(input, phases = 100):
  offset = int(input[0:7])
  input = input * 10000

  curr_phase = transmission2(input[offset:], phases)
  return "".join(map(str, curr_phase[0:8]))

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))
