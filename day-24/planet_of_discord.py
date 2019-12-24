import sys
import copy

input_file = 'day-24/input.txt'

#TODO - define better
width = 5
height = 5

def get_biodiversity(grid):
  biodiversity = 0
  rank = 1
  for y in range(len(grid)):
    for x in range(len(grid[y])):
      if grid[y][x] == '#':
        biodiversity += rank
      rank *= 2
  return biodiversity

def get_adjacents(x, y):
  return [
    (x, y - 1),
    (x - 1, y),
    (x + 1, y),
    (x, y + 1)
  ]

def part1(input):
  grid = [[char for char in line] for line in input.splitlines()]

  width = len(grid[0])
  height = len(grid)
  biodiversities = set()

  tick = 0
  while True:
    print('After',tick,'ticks:')
    for line in grid:
      print(''.join(line))
    biodiversity = get_biodiversity(grid)
    if biodiversity in biodiversities:
      return biodiversity
    biodiversities.add(biodiversity)
    
    grid = evolve(grid)
    tick += 1
    print('')
  return -1

def evolve(grid):
  # width = len(grid[0])
  # height = len(grid)
  is_in_grid = lambda x,y: (0 <= x < width and 0 <= y < height)
  new_grid = copy.deepcopy(grid)

  for y in range(height):
    for x in range(width):
      neighbours = len([(new_x,new_y) for (new_x,new_y) in get_adjacents(x,y) if is_in_grid(new_x,new_y) and grid[new_y][new_x] == '#'])
      new_state = '.'
      if (grid[y][x] == '#' and neighbours == 1) or (grid[y][x] == '.' and neighbours in [1,2]):
        new_state = '#'
      new_grid[y][x] = new_state
  return new_grid

def get_3d_adjacents(x, y, z):
  adjacents = []

  #horozontal neighbours
  if x == 0:
    adjacents.append((1, 2, z - 1))
    adjacents.append((x + 1, y, z))
  elif x == width - 1:
    adjacents.append((3, 2, z - 1))
    adjacents.append((x - 1, y, z))
  elif x == 1 and y == 2:
    adjacents.append((x - 1, y, z))
    adjacents.append((0, 0, z + 1))
    adjacents.append((0, 1, z + 1))
    adjacents.append((0, 2, z + 1))
    adjacents.append((0, 3, z + 1))
    adjacents.append((0, 4, z + 1))
  elif x == 3 and y == 2:
    adjacents.append((x + 1, y, z))
    adjacents.append((4, 0, z + 1))
    adjacents.append((4, 1, z + 1))
    adjacents.append((4, 2, z + 1))
    adjacents.append((4, 3, z + 1))
    adjacents.append((4, 4, z + 1))
  else:
    adjacents.append((x - 1, y, z ))
    adjacents.append((x + 1, y, z ))

  # Vertical neighbours
  if y == 0:
    adjacents.append((2, 1, z - 1))
    adjacents.append((x, y + 1, z))
  elif y == height - 1:
    adjacents.append((2, 3, z - 1))
    adjacents.append((x, y - 1, z))  
  elif x == 2 and y == 1:
    adjacents.append((x, y - 1, z))
    adjacents.append((0, 0, z + 1))
    adjacents.append((1, 0, z + 1))
    adjacents.append((2, 0, z + 1))
    adjacents.append((3, 0, z + 1))
    adjacents.append((4, 0, z + 1))
  elif x == 2 and y == 3:
    adjacents.append((x, y + 1, z))
    adjacents.append((0, 4, z + 1))
    adjacents.append((1, 4, z + 1))
    adjacents.append((2, 4, z + 1))
    adjacents.append((3, 4, z + 1))
    adjacents.append((4, 4, z + 1))
  else:
    adjacents.append((x, y - 1, z ))
    adjacents.append((x, y + 1, z ))

  return adjacents

def get_3d_neighbour_count(grid, x, y, z):
  return sum(1 for triple in get_3d_adjacents(x, y, z) if triple in grid)

def evolve_3d(grid):
  max_z = max(z for x, y, z in grid)
  min_z = min(grid, key = lambda p: p[2])[2] #alt way of getting min

  # width = len(grid[0])
  # height = len(grid)
  new_grid = set()
  for x in range(width):
    for y in range(height):
      for z in range(min_z - 1, max_z + 2):
        if x==2 and y==2:
          continue
        if (x,y,z) in grid and get_3d_neighbour_count(grid, x,y, z) == 1:
          new_grid.add((x,y,z))
        if (x,y,z) not in grid and get_3d_neighbour_count(grid, x,y, z) in (1,2):
          new_grid.add((x,y,z))
  return new_grid

def part2(input, ticks = 200):
  grid = set()
  grid_array = [[char for char in line] for line in input.splitlines()]
  for y in range(len(grid_array)):
    for x in range(len(grid_array[y])):
      if grid_array[y][x] == '#':
        grid.add((x,y,0))

  for i in range(ticks):
      grid = evolve_3d(grid)

  return len(grid)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))
