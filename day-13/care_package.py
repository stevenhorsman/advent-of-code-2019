from ship_computer import ShipComputer
import sys

input_file = 'day-13/input.txt'

print_icons=[' ','#','2','_','°']

def get_direction(curr, rotation):
  if rotation == 0: # left turn
    return 'ULDR'[('ULDR'.index(curr) + 1) % len('ULDR')]
  elif rotation == 1: # right turn
    return 'URDL'[('URDL'.index(curr) + 1) % len('URDL')]

def get_grid_hash(position):
  return str(position[0]) + "," + str(position[1]) 

def follow_program(memory, no_quarters = None):
  memory = memory.split(",")
  if no_quarters != None:
    memory[0] = str(no_quarters)
  robot = ShipComputer(memory)
  grid = {}
  try:
    while True:
      x = next(robot.execute_concurrent(True))
      y = next(robot.execute_concurrent(True))
      tile = next(robot.execute_concurrent(True))
      grid[(x,y)] = tile
  except StopIteration:
    return grid

def part1(memory):
  grid = follow_program(memory)
  return list(grid.values()).count(2)

def part2(memory):
  memory = memory.split(",")
  memory[0] = 2
  robot = ShipComputer(memory)
  grid = {}
  score = -1
  ball_x = -1
  paddle_x = -1
  while True:
    robot.execute_until_blocked()
    outputs = robot.get_all_outputs()
    while len(outputs) > 0:
      x = outputs.pop(0)
      y = outputs.pop(0)
      tile = outputs.pop(0)
      if (x == -1 and y == 0):
        score = tile
      else:
        grid[(x,y)] = tile
      if tile == 4:
        ball_x = x
      elif tile == 3:
        paddle_x = x

    # print(print_grid(grid,score))
    if list(grid.values()).count(2) == 0:
      return score
    input = 0
    if paddle_x > ball_x:
      input = -1
    elif paddle_x < ball_x:
      input = 1
    paddle_x += input
    robot.put_input(input)

  return score

def print_grid(grid, score):
  min_x = min(grid.keys(), key=lambda value: value[0])[0]
  max_x = max(grid.keys(), key=lambda value: value[0])[0]

  min_y = min(grid.keys(), key=lambda value: value[1])[1]
  max_y = max(grid.keys(), key=lambda value: value[1])[1]

  output = 'score: ' + str(score) + '\n'
  for h in range(min_y, max_y + 1):
    for w in range(min_x, max_x + 1):
      output += print_icons[grid.get((w, h), 0)]
    output += '\n'
  return output

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  # print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))
