import sys
from collections import deque
from bidict import bidict
import math

input_file = 'day-18/input.txt'

class Vertex:
  def __init__(self, label, pos):
    self.label = label
    self.pos = pos
    self.edges = []

  def set_paths(self, paths, vertices):
    for k, (distance, doors) in paths.items():
      self.edges.append(Edge(vertices[k], distance, doors))

  def get_available_keys(self, current_keys):
    others = self.find_other_keys(current_keys)
    return {k: v for k, v in others.items() if k.label not in current_keys}
    # NOTE 1: alternative to other lines - needs note 2
    found = {}
    for e in self.edges:
      if e.dest.label not in current_keys and e.is_unblocked(current_keys):
        found[e.dest] = e.weight
    return found

  # Sort of dijkstra's, but stop paths when we find a new key
  def find_other_keys(self, current_keys):
    dist = {}
    dist[self] = 0
    queue = []
    queue.append(self)

    while queue:
      u = min(queue, key=lambda vertex: dist[vertex])
      queue.remove(u)

      connected = [e for e in u.edges if e.is_unblocked(current_keys)]
      for e in connected:
        alt = dist[u] + e.weight
        if e.dest not in dist:
          if e.dest.label in current_keys: # If found a new key, don't bother exploring this branch more
            queue.append(e.dest)
          dist[e.dest] = alt
        if alt < dist[e.dest]:
          dist[e.dest] = alt
    return dist


class Edge:
  def __init__(self, dest, weight, blockers):
    self.dest = dest
    self.weight = weight
    self.blockers = blockers

  def is_unblocked(self, keys):
    curr_blockers = [x for x in self.blockers if x not in keys]
    return len(curr_blockers) == 0

def get_vertices(grid):
  vertices = {}
  starts = []
  for y in range(len(grid)):
    for x in range(len(grid[0])):
      value = grid[y][x]
      if value == '@':
        starts.append(Vertex(value, (x,y)))
      if value in 'abcdefghijklmnopqrstuvwxyz':
        vertices[value] = Vertex(value, (x,y))
  return starts, vertices

def get_adjacents(x, y):
  return [
    (x, y - 1),
    (x - 1, y),
    (x + 1, y),
    (x, y + 1)
  ]

def find_paths(grid, start):
  queue = deque([([],start)])
  distance = {start: 0}
  found = {}
  while queue:
    doors, current = queue.popleft()
    is_free_unvisited = lambda x,y: (grid[y][x] != "#" and (x,y) not in distance)
    for neighbour in [(x,y) for (x,y) in get_adjacents(current[0], current[1]) if is_free_unvisited(x,y)]:
      value = grid[neighbour[1]][neighbour[0]]
      distance[neighbour] = distance[current] + 1
      if 'A' <= value <= 'Z':
        queue.append((doors + [value.lower()], neighbour))
      elif 'a' <= value <= 'z':
        found[value] = distance[neighbour], doors[:]
        # queue.append((doors, neighbour)) # NOTE 2: uncommented for note 1
      else:
        queue.append((doors, neighbour))
  return found

def part1(input):
  grid = [[char for char in line] for line in input.splitlines()]
  starts, vertices = get_vertices(grid)
  for k, v in vertices.items():
    paths = find_paths(grid, v.pos)
    v.set_paths(paths, vertices)
  for v in starts:
    paths = find_paths(grid, v.pos)
    v.set_paths(paths, vertices)
  global already_seen
  already_seen = {}
  return shortest_route(starts, [])

# Based on https://github.com/sophiebits/adventofcode/blob/master/2019/day18.py
already_seen = {}
def shortest_route(robots, owned_keys):
  robot_names = ''.join(sorted([robot.label for robot in robots]))
  if (robot_names, ''.join(sorted(owned_keys))) in already_seen:
    return already_seen[robot_names, ''.join(sorted(owned_keys))]
  available_keys = get_multiple_bots_reachable_keys(robots, owned_keys)
  if len (available_keys) == 0:
    already_seen[robots, ''.join(sorted(owned_keys))] = 0
    return 0
  lengths = []
  for vertex, (distance, index) in available_keys.items():
    nstarts = tuple(vertex if i == index else p for i, p in enumerate(robots))
    length = distance + shortest_route(nstarts, owned_keys + [vertex.label])
    # print('At',robot_names, 'with keys',owned_keys,length)
    lengths.append(length)
  already_seen[robot_names, ''.join(sorted(owned_keys))] = min(lengths)
  return min(lengths)

def get_multiple_bots_reachable_keys(robots, owned_keys):
  found = {}
  for index, robot in enumerate(robots):
    available_keys = robot.get_available_keys(owned_keys)
    for vertex, distance in available_keys.items():
      found[vertex] = distance, index
  return found

def part2(input):
  return part1(input)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  with open(input_file.replace("input.txt", "input_part2.txt")) as f:
    data = f.read()
  print("Part 2: ", part2(data))
