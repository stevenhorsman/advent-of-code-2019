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

def get_3d_adjacents(x,y,z):
  adj = [
      (x-1, y, z),
      (x+1, y, z),
      (x, y-1, z),
      (x, y+1, z),
  ]
  actadj = []
  for aa in adj:
      za, xa, ya = aa
      if xa == -1:
          actadj.append((1, 2, za-1))
      elif xa == 2 and ya == 2 and x == 1:
          actadj.append((0, 0, za+1))
          actadj.append((0, 1, za+1))
          actadj.append((0, 2, za+1))
          actadj.append((0, 3, za+1))
          actadj.append((0, 4, za+1))
      elif xa == 2 and ya == 2 and x == 3:
          actadj.append((4, 0, za+1))
          actadj.append((4, 1, za+1))
          actadj.append((4, 2, za+1))
          actadj.append((4, 3, za+1))
          actadj.append((4, 4, za+1))
      elif xa == 5:
          actadj.append((3, 2, za-1))
      elif ya == -1:
          actadj.append((2, 1, za-1))
      elif ya == 2 and xa == 2 and y == 1:
          actadj.append(( 0, 0, za+1))
          actadj.append((1, 0, za+1))
          actadj.append((2, 0, za+1))
          actadj.append((3, 0, za+1))
          actadj.append((4, 0, za+1))
      elif ya == 2 and xa == 2 and y == 3:
          actadj.append((0, 4, za+1))
          actadj.append((1, 4, za+1))
          actadj.append((2, 4, za+1))
          actadj.append((3, 4, za+1))
          actadj.append((4, 4, za+1))
      elif ya == 5:
          actadj.append((2, 3, za-1))
      else:
          actadj.append(aa)
  return actadj

# def get_3d_adjacents(x, y, z):
#   # Out edges
#   if x == 0:
#     return [
#     (x, y - 1, z),
#     (1, 2, z - 1),
#     (x + 1, y, z),
#     (x, y + 1, z)
#   ]

#   if x == width - 1:
#     return [
#     (x, y - 1, z),
#     (x -1 , y, z),
#     (3, 2, z - 1),
#     (x, y + 1, z)
#   ]

#   if y == 0:
#     return [
#     (2, 1, z - 1),
#     (x -1 , y, z),
#     (x + 1, y, z),
#     (x, y + 1, z)
#   ]

#   if y == height - 1:
#     return [
#     (x, y - 1, z),
#     (x -1 , y, z),
#     (x + 1, y),
#     (x, y + 1, z - 1)
#   ]

# # Inner edges
#   if x == 1 and y == 2:
#     return [
#     (x, y - 1, z),
#     (x - 1, y, z),
#     (0, 0, z + 1),
#     (0, 1, z + 1),
#     (0, 2, z + 1),
#     (0, 3, z + 1),
#     (0, 4, z + 1),
#     (x, y + 1, z)
#   ]

#   if x == 3 and y == 2:
#     return [
#     (x, y - 1, z),
#     (x + 1, y, z),
#     (4, 0, z + 1),
#     (4, 1, z + 1),
#     (4, 2, z + 1),
#     (4, 3, z + 1),
#     (4, 4, z + 1),
#     (x, y + 1, z)
#   ]

#   if x == 2 and y == 1:
#     return [
#     (x, y - 1, z),
#     (x -1 , y, z),
#     (x + 1, y),
#     (0, 0, z + 1),
#     (1, 0, z + 1),
#     (2, 0, z + 1),
#     (3, 0, z + 1),
#     (4, 0, z + 1)
#   ]

#   if x == 2 and y == 3:
#     return [
#     (x, y - 1, z),
#     (x -1 , y, z),
#     (2, 3, z),
#     (0, 4, z + 1),
#     (1, 4, z + 1),
#     (2, 4, z + 1),
#     (3, 4, z + 1),
#     (4, 4, z + 1)
#   ]

#   return [
#     (x, y - 1),
#     (x - 1, y),
#     (x + 1, y),
#     (x, y + 1)
#   ]

def get_3d_neighbour_count(grid, x, y, z):
  return sum(1 for triple in get_3d_adjacents(x,y,z) if triple in grid)

def countadj(grid, bugs, x, y, l):
  c = 0
  adj = [
      (l, x-1,y),
      (l, x+1,y),
      (l, x,y-1),
      (l, x,y+1),
  ]
  actadj = []
  for aa in adj:
      la, xa, ya = aa
      if xa == -1:
          actadj.append((la-1, 1, 2))
      elif xa == 2 and ya == 2 and x == 1:
          actadj.append((la+1, 0, 0))
          actadj.append((la+1, 0, 1))
          actadj.append((la+1, 0, 2))
          actadj.append((la+1, 0, 3))
          actadj.append((la+1, 0, 4))
      elif xa == 2 and ya == 2 and x == 3:
          actadj.append((la+1, 4, 0))
          actadj.append((la+1, 4, 1))
          actadj.append((la+1, 4, 2))
          actadj.append((la+1, 4, 3))
          actadj.append((la+1, 4, 4))
      elif xa == 5:
          actadj.append((la-1, 3, 2))
      elif ya == -1:
          actadj.append((la-1, 2, 1))
      elif ya == 2 and xa == 2 and y == 1:
          actadj.append((la+1, 0, 0))
          actadj.append((la+1, 1, 0))
          actadj.append((la+1, 2, 0))
          actadj.append((la+1, 3, 0))
          actadj.append((la+1, 4, 0))
      elif ya == 2 and xa == 2 and y == 3:
          actadj.append((la+1, 0, 4))
          actadj.append((la+1, 1, 4))
          actadj.append((la+1, 2, 4))
          actadj.append((la+1, 3, 4))
          actadj.append((la+1, 4, 4))
      elif ya == 5:
          actadj.append((la-1, 2, 3))
      else:
          actadj.append(aa)
  translated = [(x,y,z) for (z,x,y) in actadj]

  ans = sum(1 for triple in translated if triple in grid)
  alt = get_3d_neighbour_count(grid, x,y,l)

  return ans

def stepb(grid, bugs):
    min_z = min(z for x, y, z in grid)
    max_z = max(z for x, y, z in grid)

    new_grid = set()
    nbugs = set()
    for lev in range(min_z - 1, max_z + 2):
        for i in range(5):
            for j in range(5):
                if i==2 and j==2:
                    continue
                if (lev,i,j) in bugs and countadj(grid, bugs, i,j,lev) == 1:
                    nbugs.add((lev,i,j))
                    new_grid.add((i,j,lev))
                if (lev,i,j) not in bugs and countadj(grid, bugs, i,j,lev) in (1,2):
                    nbugs.add((lev,i,j))
                    new_grid.add((i,j,lev))
    return new_grid, nbugs

def evolve_3d(grid):

  #TODO - lambda?
  min_z = min(z for x, y, z in grid)
  max_z = max(z for x, y, z in grid)

  # width = len(grid[0])
  # height = len(grid)
  # is_in_grid = lambda x,y: (0 <= x < width and 0 <= y < height)
  nbugs = set()
  for lev in range(min_z - 1, max_z + 2):
      for i in range(5):
          for j in range(5):
              if i==2 and j==2:
                  continue
              if (i,j,lev) in grid and get_3d_neighbour_count(grid, lev,i,j) == 1:
                  nbugs.add((i,j,lev))
              if (i,j,lev) not in grid and get_3d_neighbour_count(grid, lev,i,j) in (1,2):
                  nbugs.add((i,j,lev))
  return nbugs

def part2(input, ticks = 200):
  grid = set()
  bugs = set()
  grid_array = [[char for char in line] for line in input.splitlines()]
  for y in range(len(grid_array)):
    for x in range(len(grid_array[y])):
      if grid_array[y][x] == '#':
        grid.add((x,y,0))
        bugs.add((0,x,y))

  for i in range(ticks):
      grid,bugs = stepb(grid,bugs)

  return len(grid)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))
