from ship_computer import ShipComputer
import sys
from itertools import chain 
from collections import Counter 

input_file = 'day-17/input.txt'

def get_direction(curr, rotation):
  direction_string = '^<v>'
  if rotation == 'L':
    return direction_string[(direction_string.index(curr) + 1) % len(direction_string)]
  elif rotation == 'R':
    return direction_string[(direction_string.index(curr) - 1) % len(direction_string)]

deltas = dict(zip('><^v', [(1, 0), (-1, 0), (0, -1), (0, 1)]))

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

def get_adjacents(x, y):
  return [
    (x, y - 1),
    (x - 1, y),
    (x + 1, y),
    (x, y + 1)
  ]

def count_matches(lst, x): 
  return sum(lst[i:i+len(x)]==x for i in range(len(lst)))

def remove_matches(lst, x): 
  matches = [lst[i:i+len(x)]==x for i in range(len(lst))]
  indices = [i for i, x in enumerate(matches) if x == True]
  to_remove = []
  for index in indices:
    for i in range(index,index+len(x)):
      to_remove.append(i)

  return [lst[i] for i in range(0,len(lst)) if i not in to_remove]

def replace_matches(lst, x, replace): 
  matches = [lst[i:i+len(x)]==x for i in range(len(lst))]
  indices = [i for i, x in enumerate(matches) if x == True]

  to_remove = []
  for index in indices:
    lst[index] = replace
    for i in range(index+1,index+len(x)):
      to_remove.append(i)

  return [lst[i] for i in range(0,len(lst)) if i not in to_remove]
  
# TODO - write a solver that follows the scaffolding until it hits the end and then works out how to turn. Should end up with: 
# L,12,L,10,R,8,L,12,R,8,R,10,R,12,L,12,L,10,R,8,L,12,R,8,R,10,R,12,L,10,R,12,R,8,L,10,R,12,R,8,R,8,R,10,R,12,L,12,L,10,R,8,L,12,R,8,R,10,R,12,L,10,R,12,R,8
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
  
  print("".join([ chr(c) for c in outputs]))
  path = find_path(scaffolds, x, y, curr_dir)
  print(path)

  (pattern,new_path) = remove_shortest_end(path)
  (pattern_2,pattern_3) = remove_shortest_end(new_path)
  patterns=[pattern, pattern_2, pattern_3]
  #Check if all paths repeat
  for i in range(0,len(patterns)):
    possible_match = 1
    while (count_matches(patterns[i],patterns[i][0:possible_match+1]) > 2):
      possible_match += 1
      temp_pattern = patterns[i][0:possible_match]
      if len(remove_matches(patterns[i], temp_pattern)) == 0:
        patterns[i] = temp_pattern

  patterns.sort(key=len)
  for i in range(0,len(patterns)-1):
    if count_matches(patterns[-1],patterns[i]) > 0:
      patterns[-1] = remove_matches(patterns[-1],patterns[i])

  #Assume a's are correct pattern now
  main_routine = replace_matches(path, patterns[0],'A')
  main_routine = replace_matches(main_routine, patterns[1],'B')
  main_routine = replace_matches(main_routine, patterns[2],'C')

  instructions = [','.join(main_routine),','.join(patterns[0]).replace('R','R,').replace('L','L,'), ','.join(patterns[1]).replace('R','R,').replace('L','L,'), ','.join(patterns[2]).replace('R','R,').replace('L','L,'),'n']

  # Mark's 
  # instructions = ['A,A,B,C,C,A,C,B,C,B', 'L,4,L,4,L,6,R,10,L,6','L,12,L,6,R,10,L,6','R,8,R,10,L,6','n']
  # instructions = ['A,B,A,B,C,C,B,A,B,C', 'L,12,L,10,R,8,L,12','R,8,R,10,R,12','L,10,R,12,R,8','n']
  for instruction in instructions:
    inputs = [ ord(c) for c in instruction+'\n']
    for code in inputs:
      robot.put_input(code)
  robot.execute_until_blocked()
  outputs = robot.get_all_outputs()
  print("".join([ chr(c) for c in outputs]))
  return outputs[-1]

def remove_shortest_end(path):
  possible_match = 1
  while (count_matches(path,path[0:possible_match+1]) > 2):
    possible_match += 1

  start_max=possible_match

  possible_match = 1
  while (count_matches(path,path[-(possible_match+1):]) > 2):
    possible_match += 1
  end_max=possible_match

  if (start_max < end_max):
    pattern = path[0:start_max]
    new_path = remove_matches(path, pattern)
  else:
    pattern = path[-end_max:]
    new_path = remove_matches(path, pattern)

  return (pattern, new_path)

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

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))
