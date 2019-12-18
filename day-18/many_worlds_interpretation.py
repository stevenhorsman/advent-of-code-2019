import sys
from collections import deque
from bidict import bidict
import math

input_file = 'day-18/input.txt'

# TODO - try create the paths and blocker between each robot and key - then we can compress the paths and neighbour finding

def get_adjacents(x, y):
  return [
    (x, y - 1),
    (x - 1, y),
    (x + 1, y),
    (x, y + 1)
  ]

def prepare_get_shortest_route(grid):
  robots = []
  keys = bidict()
  doors = bidict()

  for y in range(len(grid)):
        for x in range(len(grid[0])):
            value = grid[y][x]
            if value == '@':
              robots.append((x,y))
              grid[y][x] = '.'
            if value in 'abcdefghijklmnopqrstuvwxyz':
              # key = get_key(keys, value)
              # key.set_pos(x,y)
              keys[value] = (x,y)
              grid[y][x] = '.'
            if value in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
              # door = get_door(doors, value.lower())
              # key = get_key(keys,value.lower())
              # door.set_pos(x,y)
              # key.set_door(door)
              doors[(x,y)] = value.lower()
              grid[y][x] = '.'
  
  #Remove doors with no key
  doors = dict(filter(lambda elem: elem[1] in keys, doors.items()))

  #Robots has to be tuple as list not hashable
  return shortest_route(grid, doors, keys, tuple(robots), set())

def optimise_grid(grid):
  dead_ends = 0
  for y in range(1,len(grid)-1):
    for x in range(1,len(grid[0])-1):
      if grid[y][x] == '.':
        if len([(new_x,new_y) for (new_x,new_y) in get_adjacents(x, y) if grid[new_y][new_x] == '#']) == 3:
          dead_ends +=1
          grid[y][x] = '#'
  if dead_ends > 0:
    optimise_grid(grid)

# Based on https://github.com/sophiebits/adventofcode/blob/master/2019/day18.py
already_seen = {}
def shortest_route(grid, doors, keys, robots, owned_keys):
  if (robots, ''.join(sorted(owned_keys))) in already_seen:
    return already_seen[robots, ''.join(sorted(owned_keys))]
  # print(''.join(sorted(owned_keys)))
  available_keys = get_multiple_bots_reachable_keys(grid, doors, keys, robots, owned_keys)
  if len (available_keys) == 0:
    already_seen[robots, ''.join(sorted(owned_keys))] = 0
    return 0
  lengths = []
  for key, (path, pos, index) in available_keys.items():
    new_keys = owned_keys.copy()
    new_keys.add(key)
    nstarts = tuple(pos if i == index else p for i, p in enumerate(robots))
    lengths.append(len(path) + shortest_route(grid, doors, keys, nstarts, new_keys))
  already_seen[robots, ''.join(sorted(owned_keys))] = min(lengths)
  return min(lengths)

def get_multiple_bots_reachable_keys(grid, doors, keys, robots, owned_keys):
  found = {}
  for index, robot in enumerate(robots):
    available_keys = breadth_first_search(grid, doors, keys, robot, owned_keys)
    for key, (path, pos) in available_keys.items():
      found[key] = path, pos, index
  return found

def breadth_first_search(grid, doors, keys, start, owned_keys):
    queue = deque([([],start)])
    visited = set()
    found = {}
    while queue:
      path, current = queue.popleft()
      visited.add(current)
      is_locked_door = lambda x,y: ((x,y) in doors and doors[(x,y)] not in owned_keys)
      is_free_unvisited = lambda x,y: (grid[y][x] == "." and (x,y) not in visited and not is_locked_door(x,y))
      for neighbour in [(x,y) for (x,y) in get_adjacents(current[0], current[1]) if is_free_unvisited(x,y)]:
        new_path = path.copy()
        new_path.append(current)
        if neighbour in keys.inv and keys.inv[neighbour] not in owned_keys:
          found[keys.inv[neighbour]] = new_path, neighbour
        else:
          queue.append((new_path, neighbour))
    return found

def part1(input):
  grid = [[char for char in line] for line in input.splitlines()]

  optimise_grid(grid)

  return prepare_get_shortest_route(grid)

def part2(input):
  grid = [[char for char in line] for line in input.splitlines()]
  optimise_grid(grid)

  return prepare_get_shortest_route(grid)
  # return part2_hack(grid)

def part2_hack(grid):
  grid_height = math.ceil(len(grid)/2)
  grid_width = math.ceil(len(grid[0])/2)

  grid_1 = [[grid[y][x] for x in range(grid_width)] for y in range(grid_height)]
  grid_2 = [[grid[y][x+grid_width-1] for x in range(grid_width)] for y in range(grid_height)]
  grid_3 = [[grid[y+grid_height-1][x] for x in range(grid_width)] for y in range(grid_height)]
  grid_4 = [[grid[y+grid_height-1][x+grid_width-1] for x in range(grid_width)] for y in range(grid_height)]

  results = [prepare_get_shortest_route(grid_1),
    prepare_get_shortest_route(grid_2),
    prepare_get_shortest_route(grid_3),
    prepare_get_shortest_route(grid_4)]

  return sum(results)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  with open(input_file.replace("input.txt", "input_part2.txt")) as f:
    data = f.read()
  print("Part 2: ", part2(data))
