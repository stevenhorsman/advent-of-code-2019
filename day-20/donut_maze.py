import sys
from collections import deque
import math

input_file = 'day-20/input.txt'

class Vertex:
  def __init__(self, label, pos):
    self.label = label
    self.pos = pos
    self.edges = []

  def add_pos(self, other_pos):
    self.positions.append(other_pos)

  def add_edge(self, vertex, weight = 0):
    self.edges.append(Edge(vertex, weight))

  def get_edges(self):
    return self.edges

  def add_paths(self, paths, vertices):
    for k, distance in paths.items():
      self.edges.append(Edge(vertices[k], distance))

  def __repr__(self):
    return "vertex %s @ (%s)" % (self.label, self.pos)

class Edge:
  def __init__(self, dest, weight):
    self.dest = dest
    self.weight = weight

def get_vertices(grid):
  vertices = {}

  #Logic inspired by from https://github.com/sophiebits/adventofcode/blob/master/2019/day20.py
  for y in range(2, len(grid) - 2):
    for x in range(2, len(grid[0]) - 2):
      if grid[y][x] != '.':
        continue
      for pair in get_adjacent_pairs(grid, x, y):
        if all(cell.isalpha() for cell in pair):
          label = ''.join(pair)
          if (x <= 3 or x >= len(grid[0]) - 3 or y <= 3 or y >= len(grid) - 3 ):
            label += 'o' #outer
          else:
            label += 'i' #inner
          vertices[label] = Vertex(label, (x,y))
  return vertices

def get_adjacent_pairs(grid, x, y):
  return [
    grid[y][x-2:x],
    grid[y][x+1:x+3],
    grid[y-2][x]+grid[y-1][x],
    grid[y+1][x]+grid[y+2][x]
  ]

def dijkstra(vertices, source, dest):
  dist = {vertex: sys.maxsize for vertex in vertices}
  prev = {vertex: None for vertex in vertices}
  queue = vertices.copy()

  dist[source] = 0

  while queue:
    u = min(queue, key=lambda vertex: dist[vertex])
    if u == dest:
      # print path
      # path = ""
      # curr = u
      # while prev[curr] != source:
      #   path = prev[curr].label + "," + path
      #   curr = prev[curr]
      # print('path from ', source, 'to', dest, ":", path)
      return dist[u]
    
    queue.remove(u)

    for e in u.get_edges():
      alt = dist[u] + e.weight
      if alt < dist[e.dest]:
        dist[e.dest] = alt
        prev[e.dest] = u

def get_adjacents(x, y):
  return [
    (x, y - 1),
    (x - 1, y),
    (x + 1, y),
    (x, y + 1)
  ]

def find_paths(grid, start):
  queue = deque([start])
  distance = {start: 0}
  found = {}
  while queue:
    current = queue.popleft()
    is_free_unvisited = lambda x,y: ((grid[y][x] == "." or len(grid[y][x]) == 3) and (x,y) not in distance)
    for neighbour in [(x,y) for (x,y) in get_adjacents(current[0], current[1]) if is_free_unvisited(x,y)]:
      value = grid[neighbour[1]][neighbour[0]]
      distance[neighbour] = distance[current] + 1
      if len(value) == 3:
        found[value] = distance[neighbour]
        # queue.append((doors, neighbour)) #TODO - remove this line and instead let edges find their other edge in vertex.getAvailableKey
      else:
        queue.append(neighbour)
  return found

def part1(input):
  grid = [[char for char in line] for line in input.splitlines()]
  
  vertices = get_vertices(grid)
  # Update grid with vertices and create back-links
  for k, v in vertices.items():
    pos = v.pos
    grid[pos[1]][pos[0]] = k
    if (k.endswith('i')):
      pair = vertices[k.replace('i','o')]
      pair.add_edge(v, 1)
      v.add_edge(pair, 1)

  # Find adjacent vertices
  for k, v in vertices.items():
    paths = find_paths(grid, v.pos)
    v.add_paths(paths, vertices)

  return dijkstra(list(vertices.values()), vertices['AAo'], vertices['ZZo'])

def get_neighbours(grid, vertices, pos):
  (x, y, level) = pos
  is_free = lambda x,y: (grid[y][x] == "." or len(grid[y][x]) == 3)
  neighbours = [(x,y, level) for (x,y) in get_adjacents(x, y) if is_free(x,y)]
  value = grid[y][x]
  if len(value) == 3: #portal
    inner = value[2] == 'i'
    if inner:
      outer = vertices[value[0:2]+'o']
      neighbours.append((outer.pos[0], outer.pos[1], level + 1))
    elif level > 0:
      if value not in ['AAo', 'ZZo']:
        inner = vertices[value[0:2]+'i']
        neighbours.append((inner.pos[0], inner.pos[1], level - 1))
  return neighbours

def breadth_first_search(grid, vertices, start, goal):
  queue = deque([(start,0)])
  visited = set()
  while queue:
    pos, distance = queue.popleft()
    if pos in visited:
      continue
    visited.add(pos)
    if pos == goal:
      return distance
    for neighbour in get_neighbours(grid, vertices, pos):
      queue.append((neighbour, distance + 1))
  return sys.maxsize

def part2(input):
  grid = [[char for char in line] for line in input.splitlines()]

  vertices = get_vertices(grid)  
  # Update grid with vertices
  for k, v in vertices.items():
    pos = v.pos
    grid[pos[1]][pos[0]] = k

  start_vertex = vertices['AAo']
  start = (start_vertex.pos[0], start_vertex.pos[1], 0)
  goal_vertex = vertices['ZZo']
  goal = (goal_vertex.pos[0], goal_vertex.pos[1], 0)

  # solve with bfs
  return breadth_first_search(grid, vertices, start, goal)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))
