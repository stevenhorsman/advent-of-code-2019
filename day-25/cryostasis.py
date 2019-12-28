from ship_computer import ShipComputer
import sys
import random
from itertools import combinations 
from collections import deque
import re

input_file = 'day-25/input.txt'

directions = ['north', 'south', 'east', 'west']
item_blacklist = ['escape pod', 'giant electromagnet', 'infinite loop', 'photons', 'molten lava']
correct_items = ['shell', 'fixed point', 'polygon', 'candy cane'] #Set to None to work out items
deltas = dict(zip(['east','west','north','south'], [(1, 0), (-1, 0), (0, 1), (0, -1)]))
opposites = dict(zip(['east','west','north','south'], ['west','east','south','north']))
inventory = []

def part1(memory):
  memory = memory.split(",")
  robot = ShipComputer(memory)
  grid = {}
  x, y = 0, 0
  room, directions, items, success = handle_room(robot)
  grid[(x,y)] = room
  direction = directions[0]

  while direction != None: #All directions visited - done
    run_command(robot, direction)
    room, directions, items, success = handle_room(robot)
    if success:
      if room == '== Pressure-Sensitive Floor ==':
        return success
      x += deltas[direction][0]
      y += deltas[direction][1]
      grid[(x,y)] = room
    # if we have 8 items, or the correct items, then go to security checkpoint
    inventory = get_inventory(robot)
    if len(inventory) == 8 or (correct_items != None and all(item in inventory for item in correct_items)):
      commands = work_out_route_to_sec_check(grid, room)
      for command in commands[:-1]:
        run_command(robot, command)
        room, directions, items, success = handle_room(robot)
      direction = commands[-1]
      run_command(robot, direction)
      room, directions, items, success = handle_room(robot)
    if room == '== Security Checkpoint ==':
      back_track = opposites[direction]
      pressure_floor_dir = list(filter(lambda dir: dir != back_track, directions))[0]
      if len(inventory) == 8 or (correct_items != None and all(item in inventory for item in correct_items)):
        for item in inventory:
          run_command(robot,'drop ' + item, True)
        if correct_items != None:
          for item in correct_items:
            run_command(robot,'take ' + item, True)
          run_command(robot,pressure_floor_dir)
          output = get_output_ascii(robot)
        else:
          for comb in combinations(inventory,4):
            for item in comb:
              run_command(robot,'take ' + item, True)
            run_command(robot,pressure_floor_dir)
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
          return int(re.findall("\d\d+",output.splitlines()[-1])[0])
      else:
        # Don't try pressure floor yet
        directions.remove(pressure_floor_dir)
    
    # direction = random.choice(directions)
    # Find a direction we haven't been in yet
    direction = None
    for dir in directions:
      new_x = x + deltas[dir][0]
      new_y = y + deltas[dir][1]
      if (new_x, new_y) not in grid:
        direction = dir
        break

    if direction == None: # All directions already explored - need to mark and backtrack
      direction = random.choice(directions)
      # if room != '== Security Checkpoint ==': # Never mark security checkpoint unvisited
      #   grid[(x,y)] = "v"+grid[(x,y)] # visited
      # for dir in directions:
      #   next_x = x + deltas[dir][0]
      #   next_y = y + deltas[dir][1]
      #   if not grid[(next_x, next_y)].startswith('v'):
      #     direction = dir
      #     break  

def get_adjacents(x, y):
  return [
    (x, y - 1),
    (x - 1, y),
    (x + 1, y),
    (x, y + 1)
  ]

def work_out_route_to_sec_check(grid, current_room):
  start_pos = list(grid.keys())[list(grid.values()).index(current_room)]
  queue = deque([(start_pos, 0)])
  prev = {}
  visited = set()

  while queue:
    pos, distance = queue.popleft()
    if pos in visited:
      continue
    visited.add(pos)
    if grid[pos] == '== Security Checkpoint ==':
      curr = pos
      path = [pos]
      while prev[curr] != start_pos:
        path = [prev[curr]] + path
        curr = prev[curr]
      path = [start_pos] + path
      # path_string = ''
      # for segment in path:
      #   path_string += grid[segment] + ','
      commands = []
      for i in range(1,len(path)):
        delta_x = path[i][0] - path[i-1][0]
        delta_y = path[i][1] - path[i-1][1]
        commands.append(list(deltas.keys())[list(deltas.values()).index((delta_x, delta_y))])
      return commands
    is_free_unvisited = lambda pos: (pos in grid and pos not in visited)
    for neighbour in [pos for pos in get_adjacents(pos[0], pos[1]) if is_free_unvisited(pos)]:
      queue.append((neighbour, distance + 1))
      prev[neighbour] = pos

def get_inventory(robot):
  # run_command(robot,'inv')
  # inv = get_output_ascii(robot)
  # return [s.replace('- ','') for s in inv.splitlines()[2:] if s.startswith('- ')]
  return inventory

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
  items = [item for item in items if item not in item_blacklist]
  for item in items:
    run_command(robot, 'take ' + item, True)
    inventory.append(item)
  return room, directions, items, success

def parse_outputs(robot):
  success = True
  output = get_output_ascii(robot)
  room = output.splitlines()[3]
  directions = []
  items = []
  sections = output.split('\n\n')
  for section in sections:
    if section.startswith('Doors here lead:'):
      directions = [s.replace('- ','') for s in section.splitlines()[1:]]
    elif section.startswith('Items here:'):
      items = [s.replace('- ','') for s in section.splitlines()[1:]]
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
