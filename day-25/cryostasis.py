from ship_computer import ShipComputer
import sys
import random
from itertools import combinations 
import re

input_file = 'day-25/input.txt'

directions = ['north', 'south', 'east', 'west']
item_blacklist = ['escape pod', 'giant electromagnet', 'infinite loop', 'photons', 'molten lava']
correct_items = ['shell', 'fixed point', 'polygon', 'candy cane'] #Set to None to work out items
deltas = dict(zip(['east','west','north','south'], [(1, 0), (-1, 0), (0, -1), (0, 1)]))
# opposites = dict(zip(['east','west','north','south'], ['west','east','south','north']))

def part1(memory):
  memory = memory.split(",")
  robot = ShipComputer(memory)
  grid = {}
  x, y = 0, 0
  room, directions, items, success = handle_room(robot)
  grid[(x,y)] = room
  direction = directions[0]

  while direction != None: #All directions visited - done
    # print(print_grid(grid,x,y))
    run_command(robot, direction)
    room, directions, items, success = handle_room(robot)
    if room == '== Security Checkpoint ==':
      pass
      # only try going to the pressure floor if we have the items we need, move logic from below up here, then remove randomisation
    if success:
      if room == '== Pressure-Sensitive Floor ==':
        return success
      x += deltas[direction][0]
      y += deltas[direction][1]
      grid[(x,y)] = room

    direction = random.choice(directions)
    # Find a direction we haven't been in yet
    # direction = None
    # for dir in directions:
    #   new_x = x + deltas[dir][0]
    #   new_y = y + deltas[dir][1]
    #   if (new_x, new_y) not in grid:
    #     direction = dir
    #     break

    # if direction == None: # All directions already explored - need to mark and backtrack
    #   grid[(x,y)] = "v"+grid[(x,y)] # visited
    #   for dir in directions:
    #     next_x = x + deltas[dir][0]
    #     next_y = y + deltas[dir][1]
    #     if not grid[(next_x, next_y)].startswith('v'):
    #       direction = dir
    #       break  

def depth_first_search(robot, room, directions, visited):
  if room in visited:
    return
  for direction in directions:
    clone = copy.deepcopy(robot)
    run_command(clone, direction)
    depth_first_search()

def handle_room(robot):
  robot.execute_until_blocked()
  room, directions, items, success = parse_outputs(robot)
  #Take all items we see
  # print('At', room, 'with', items, 'and',directions)
  items = [item for item in items if item not in item_blacklist]
  for item in items:
    run_command(robot, 'take ' + item, True)
  return room, directions, items, success

def parse_outputs(robot):
  success = True
  output = get_output_ascii(robot)
  # print(output)
  room = output.splitlines()[3]
  if room == '== Pressure-Sensitive Floor ==':
    run_command(robot,'inv')
    inv = get_output_ascii(robot)
    inventory = [s.replace('- ','') for s in inv.splitlines()[2:] if s.startswith('- ')]
    # print('Inventory:',inventory)
    if len(inventory) == 8:
      for item in inventory:
        run_command(robot,'drop ' + item, True)
      if correct_items != None:
        for item in correct_items:
          run_command(robot,'take ' + item, True)
        run_command(robot,'west') #TODO - not hardcoded
        output = get_output_ascii(robot)
      else:
        for comb in combinations(inventory,4):
          for item in comb:
            run_command(robot,'take ' + item, True)
          run_command(robot,'west') #TODO - not hardcoded
          output = get_output_ascii(robot)
          if 'ejected' not in output:
            print('The combination:', comb)
            break
          for item in comb:
            run_command(robot,'drop ' + item, True)
    if 'ejected' in output:
      success = False
      output = output.split('\n\n\n')[2]
      room = output.splitlines()[3]
    elif 'You may proceed.' in output:
      success = int(re.findall("\d\d+",output.splitlines()[-1])[0])
  directions = []
  items = []
  sections = output.split('\n\n')
  for section in sections:
    if section.startswith('Doors here lead:'):
      directions = [s.replace('- ','') for s in section.splitlines()[1:]]
    elif section.startswith('Items here:'):
      items = [s.replace('- ','') for s in section.splitlines()[1:]]
  # print('At', room, 'with', items, 'and',directions)
  return room, directions, items, success

def get_output_ascii(robot):
  outputs = robot.get_all_outputs()
  return "".join([ chr(c) for c in outputs])

def run_command(robot, command, process_output = False):
  # print('Issuing',command)
  inputs = [ ord(c) for c in command+'\n']
  for code in inputs:
    robot.put_input(code)
  robot.execute_until_blocked()
  if process_output:
    outputs = robot.get_all_outputs()

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
