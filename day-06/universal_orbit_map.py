import sys

input_file = 'day-06/input.txt'

def get_ancestor_path(orbits, node):
  if (node in orbits.keys()):
    return [node] + get_ancestor_path(orbits, orbits[node])
  else: # No parent
    return [node]

def part1(input):
  orbit_pairs = [line.split(")") for line in input.split()]
  orbits = {orbiter: parent for parent, orbiter in orbit_pairs}
  length = 0
  for node in orbits.keys():
    length += len(get_ancestor_path(orbits, node)) - 1
  return length

def part2(input):
  orbit_pairs = [line.split(")") for line in input.split()]
  orbits = {orbiter: parent for parent, orbiter in orbit_pairs}

  you_path = get_ancestor_path(orbits,"YOU")
  santa_path = get_ancestor_path(orbits,"SAN")
  difference = set(you_path).symmetric_difference(set(santa_path))

  return len(difference) - 2 # includes you and santa nodes


if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))
