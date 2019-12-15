from ship_computer import ShipComputer
import sys

input_file = 'day-15/input.txt'

deltas = dict(zip('EWNS', [(1, 0), (-1, 0), (0, -1), (0, 1)]))
inputs = dict(zip('NSWE', [1,2,3,4]))

def explore_maze(memory):
  memory = memory.split(",")
  robot = ShipComputer(memory)
  grid = {}
  x, y = 0, 0
  oxygen = None
  direction = 'N'
  grid[(x,y)] = '.'
  try:
    while direction != None: #All directions visited - done
      # print(print_grid(grid,x,y))
      input = inputs[direction]
      robot.put_input(input)
      status = next(robot.execute_concurrent(True))
      if status == 0:
        wall_x = x + deltas[direction][0]
        wall_y = y + deltas[direction][1]
        grid[(wall_x,wall_y)] = '#'
      elif status == 1:
        x += deltas[direction][0]
        y += deltas[direction][1]
        grid[(x,y)] = '.'
      elif status == 2:
        x += deltas[direction][0]
        y += deltas[direction][1]
        grid[(x,y)] = '2'
        oxygen = (x,y)

      # Find a direction we haven't been in yet
      direction = None
      for next_dir in inputs.keys():
        next_x = x + deltas[next_dir][0]
        next_y = y + deltas[next_dir][1]
        if (next_x, next_y) not in grid:
          direction = next_dir
          break
      
      if direction == None: # All directions already explored - need to mark and backtrack
        grid[(x,y)] = "'" # visited
        for next_dir in inputs.keys():
          next_x = x + deltas[next_dir][0]
          next_y = y + deltas[next_dir][1]
          if grid[(next_x, next_y)] == '.':
            direction = next_dir
            break  
  except StopIteration:
    pass
  
  grid[oxygen] = '2'
  return grid, oxygen

def recursive_solve(grid, x, y):
  if grid[(x,y)] == '2':
    return True
  if grid[(x,y)] == "#" or grid[(x,y)] == 'v' : # visited or wall
    return False
  
  grid[(x,y)] = 'v'

  if recursive_solve(grid, x-1, y):
    grid[(x,y)] = '*'
    return True
  if recursive_solve(grid, x+1, y):
    grid[(x,y)] = '*'
    return True
  if recursive_solve(grid, x, y-1):
    grid[(x,y)] = '*'
    return True
  if recursive_solve(grid, x, y+1):
    grid[(x,y)] = '*'
    return True
  return False

def part1(memory):
  grid, _ = explore_maze(memory)
  recursive_solve(grid,0,0)
  return list(grid.values()).count('*')

def part2(memory):
  grid, oxygen = explore_maze(memory)
  grid[oxygen] = 'o'
  tick = 0

  while list(grid.values()).count("'") > 0:
    new_oxygens = [coord for coord in grid if grid[coord] == 'o']
    for coord in new_oxygens:
      x = coord[0]
      y = coord[1]
      # Find neighbours and mark them
      for next_dir in inputs.keys():
        adj_x = x + deltas[next_dir][0]
        adj_y = y + deltas[next_dir][1]
        if grid[(adj_x, adj_y)] == "'":
          grid[(adj_x, adj_y)] = 'o'
      grid[coord] = 'O'
    tick += 1
  return tick

def print_grid(grid ,x=None, y=None):
  print_grid = grid.copy()
  if x != None:
    print_grid[(x,y)] = 'D'    
  min_x = min(print_grid.keys(), key=lambda value: value[0])[0]
  max_x = max(print_grid.keys(), key=lambda value: value[0])[0]

  min_y = min(print_grid.keys(), key=lambda value: value[1])[1]
  max_y = max(print_grid.keys(), key=lambda value: value[1])[1]

  output = ''
  for h in range(min_y, max_y + 1):
    for w in range(min_x, max_x + 1):
      output += print_grid.get((w, h), ' ')
    output += '\n'
  return output

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))
