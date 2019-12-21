import math

input_file = 'day-16/input.txt'

def transmission(input, phases = 100):
  curr_phase = [int(char) for char in input]
  for i in range(0,phases):
    new_phase = []
    for j in range(0,len(input)):
      pattern_length = (j+1) * 4 #base patten length
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

# we can just use a partial sum calculation as after 1/2 way we can use the unitary matrix
def transmission2(curr_phase, phases = 100):
  input_length = len(curr_phase)
  curr_phase.append(0) # add zero on the end so that the end value works
  for i in range(phases):
    for j in range(input_length,0,-1):
      # Quicker than curr_phase[j-1] = abs(curr_phase[j] + curr_phase[j-1]) % 10
      temp = curr_phase[j] + curr_phase[j-1]
      if temp >= 0:
        curr_phase[j-1] = temp % 10
      else:
        curr_phase[j-1] = (-temp) % 10
  return curr_phase

# Slightly quicker implementation from https://www.reddit.com/r/adventofcode/comments/ebai4g/2019_day_16_solutions/fb3ksil/
def transmission2b(curr_phase, phases = 100):
  for i in range(phases):
    partial_sum = sum(curr_phase)
    for j in range(len(curr_phase)):
      t = partial_sum
      partial_sum -= curr_phase[j]
      # Quicker than curr_phase[j] = abs(t) % 10
      if t >= 0:
        curr_phase[j] = t % 10
      else:
        curr_phase[j] = (-t) % 10
  return curr_phase

def part2(input, phases = 100):
  offset = int(input[0:7])
  input = list(map(int, input)) * 10000
  curr_phase = transmission2b(input[offset:], phases)
  return "".join(map(str, curr_phase[0:8]))

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))
