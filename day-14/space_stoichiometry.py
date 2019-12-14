import sys
import re
import math

input_file = 'day-14/input.txt'

# Stolen from https://github.com/sparkyb/adventofcode/blob/master/2019/day14.py
def get_reactions(input):
  reactions = {}
  for line in input.splitlines():
    match = re.search(r'^((?:\d+ [A-Z]+, )*\d+ [A-Z]+) => (\d+) ([A-Z]+)$', line)
    output_amount = int(match.group(2))
    output = match.group(3)
    inputs = []
    for input in match.group(1).split(', '):
      input_amount, input = input.split(' ')
      inputs.append((int(input_amount), input))
    reactions[output] = (output_amount, inputs)
  return reactions

def calculate_ore(reactions, required = 1):
  targets = {}
  targets['FUEL'] = required
  while any(targets[chemical] > 0 and chemical != 'ORE' for chemical in targets):
    target = [chemical for chemical in targets if targets[chemical] > 0 and chemical != "ORE"][0]
    target_amount = targets[target]
    amount, inputs = reactions[target]
    scale_factor = math.ceil(target_amount / amount)
    targets[target] -= scale_factor * amount
    for input in inputs:
      if input[1] in targets:
        targets[input[1]] += scale_factor * input[0]
      else:
        targets[input[1]] = scale_factor * input[0]
  return targets['ORE']

# Got fixed from https://www.reddit.com/r/adventofcode/comments/eafj32/2019_day_14_solutions/faqf899/
def part1(input):
  reactions = get_reactions(input)
  return calculate_ore(reactions, 1)

def part2(input):
  reactions = get_reactions(input)
  target = 1000000000000
  min, max = 0, 100000000
  while min < max - 1:
    mid = (min + max) // 2
    created = calculate_ore(reactions, mid)
    if created > target:
      max = mid
    else :
      min = mid

  return (max if calculate_ore(reactions, max) <= target else min)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))
