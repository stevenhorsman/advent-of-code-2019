from ship_computer import ShipComputer
import sys
from itertools import chain 
from collections import Counter 

input_file = 'day-17/input.txt'

def get_adjacents(x, y):
  return [
    (x, y - 1),
    (x - 1, y),
    (x + 1, y),
    (x, y + 1)
  ]

def part1(memory):
  memory = memory.split(",")
  robot = ShipComputer(memory)
  robot.execute_until_blocked()
  outputs = robot.get_all_outputs()
  map = "".join([ chr(c) for c in outputs])
  # print(map)
  lines = map.splitlines()
  scaffolds = [(x,y) for y in range(0,len(lines)) for x in range(0,len(lines[y])) if lines[y][x] == '#']

  is_intersection = lambda x,y: all(adjacent in scaffolds for adjacent in get_adjacents(x,y))
  return sum([x * y for (x,y) in scaffolds if is_intersection(x,y)])

def get_direction(curr, rotation):
  direction_string = '^<v>'
  if rotation == 'L':
    return direction_string[(direction_string.index(curr) + 1) % len(direction_string)]
  elif rotation == 'R':
    return direction_string[(direction_string.index(curr) - 1) % len(direction_string)]

deltas = dict(zip('><^v', [(1, 0), (-1, 0), (0, -1), (0, 1)]))

def find_path(scaffolds, x, y, curr_dir):
  path = []
  while True:
    curr_move = ""
    # do we move left or right?
    next_dir = get_direction(curr_dir,'R')
    next_x = x + deltas[next_dir][0]
    next_y = y + deltas[next_dir][1]
    if (next_x, next_y) in scaffolds:
      curr_dir = next_dir
      curr_move = 'R'
    else:
      next_dir = get_direction(curr_dir,'L')
      next_x = x + deltas[next_dir][0]
      next_y = y + deltas[next_dir][1]
      if (next_x, next_y) in scaffolds:
        curr_dir = next_dir
        curr_move = 'L'
      else:
        # Can't move any further
        return path
    moves = 0
    end = False
    while not end:
      next_x = x + deltas[next_dir][0]
      next_y = y + deltas[next_dir][1]
      if (next_x, next_y) in scaffolds:
        moves +=1
        x, y = next_x, next_y
      else:
        path.append(curr_move+str(moves))
        end = True

def count_matches(lst, x): 
  return sum(lst[i:i+len(x)]==x for i in range(len(lst)))

def remove_matches(lst, x): 
  return replace_matches(lst, x, [])
  
def replace_matches(lst, x, replace): 
  matches = [lst[i:i+len(x)]==x for i in range(len(lst))]
  indices = [i for i, x in enumerate(matches) if x == True]

  to_remove = []
  for index in indices:
    for j in range(len(replace)):
      lst[index+j] = replace[j]
    for i in range(index + len(replace),index + len(x)):
      to_remove.append(i)

  return [lst[i] for i in range(0,len(lst)) if i not in to_remove]
  
def get_first_pattern(path):
  possible_match = 1
  while (count_matches(path,path[0:possible_match+1]) > 2):
    possible_match += 1

  return path[0:possible_match]

def get_instructions(path):
  patterns = []
  remaining_path = path[:]
  for _ in range(1,3): # There are 3 patterns: A,B & C
    pattern = get_first_pattern(remaining_path)
    patterns.append(pattern)
    remaining_path = remove_matches(remaining_path, pattern)
  patterns.append(remaining_path) # Whatever remains is the last pattern

  #Check if any of the patterns repeat
  for i in range(len(patterns)):
    possible_match = 1
    while (count_matches(patterns[i],patterns[i][0:possible_match+1]) > 2):
      possible_match += 1
      temp_pattern = patterns[i][0:possible_match]
      if len(remove_matches(patterns[i], temp_pattern)) == 0:
        patterns[i] = temp_pattern

  # Check if longest pattern contains any of the shortest ones as well
  patterns.sort(key=len)
  for i in range(0,len(patterns)-1):
    if count_matches(patterns[-1],patterns[i]) > 0:
      patterns[-1] = remove_matches(patterns[-1],patterns[i])

  for (pattern, instruction) in zip(patterns, 'ABC'):
    path = replace_matches(path, pattern, instruction)

  instructions = [path] + patterns + ['n']
  return [(','.join(instruction)).replace('R','R,').replace('L','L,') for instruction in instructions]

def part2(memory):
  memory = memory.split(",")
  memory[0] = 2
  robot = ShipComputer(memory)

  robot.execute_until_blocked()
  outputs = robot.get_all_outputs()
  lines = "".join([ chr(c) for c in outputs]).splitlines()
  scaffolds = [(x,y) for y in range(0,len(lines)) for x in range(0,len(lines[y])) if lines[y][x] == '#']
  (x,y) = [(x,y) for y in range(0,len(lines)) for x in range(0,len(lines[y])) if lines[y][x] in '^<v>'][0]
  curr_dir = lines[y][x]
  
  path = find_path(scaffolds, x, y, curr_dir)
  instructions = get_instructions(path)

  # instructions = ['A,B,A,B,C,C,B,A,B,C', 'L,12,L,10,R,8,L,12','R,8,R,10,R,12','L,10,R,12,R,8','n']
  for instruction in instructions:
    inputs = [ ord(c) for c in instruction+'\n']
    for code in inputs:
      robot.put_input(code)
  robot.execute_until_blocked()
  outputs = robot.get_all_outputs()
  # print("".join([ chr(c) for c in outputs]))
  return outputs[-1]

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  # print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))
