from ship_computer import ShipComputer
import sys

input_file = 'day-11/input.txt'

default_color = 1

def get_direction(curr, rotation):
  if rotation == 0: # left turn
    return 'ULDR'[('ULDR'.index(curr) + 1) % len('ULDR')]
  elif rotation == 1: # right turn
    return 'URDL'[('URDL'.index(curr) + 1) % len('URDL')]

def get_grid_hash(position):
  return str(position[0]) + "," + str(position[1]) 

def follow_program(memory, initial_input = 0):
  deltas = dict(zip('RLUD', [(1, 0), (-1, 0), (0, -1), (0, 1)]))
  grid = {}
  x, y = 0, 0
  robot = ShipComputer(memory.split(","))
  direction = 'U'
  default_color = initial_input
  try:
    while True:
      input = default_color
      default_color = 0
      if (x,y) in grid:
        input = grid[(x,y)]
      robot.put_input(input)
      paint = next(robot.execute_concurrent(True))
      grid[(x,y)] = paint
      rotation = next(robot.execute_concurrent(True))
      direction = get_direction(direction, rotation)
      x += deltas[direction][0]
      y += deltas[direction][1]
  except StopIteration:
    return grid

def part1(memory):
  grid = follow_program(memory)
  return len(grid.values())

def part2(memory):
  grid = follow_program(memory,1)
  min_x = min(grid.keys(), key=lambda value: value[0])[0]
  max_x = max(grid.keys(), key=lambda value: value[0])[0]

  min_y = min(grid.keys(), key=lambda value: value[1])[1]
  max_y = max(grid.keys(), key=lambda value: value[1])[1]

  output = ""
  for h in range(min_y, max_y + 1):
    for w in range(min_x, max_x + 1):
      output += ' ' if grid.get((w, h), 0) == 0 else "#"
    output += '\n'
  return output

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))
