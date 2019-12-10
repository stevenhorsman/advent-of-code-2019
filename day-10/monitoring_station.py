import sys
import math
from collections import defaultdict 

input_file = 'day-10/input.txt'

def get_asteriod_list(input):
  # From https://github.com/sparkyb/adventofcode/blob/master/2019/day10.py
  # enumerate converts line in (index, value) pairs
  return [(x, y) for y, line in enumerate(input.split())
          for x, c in enumerate(line) if c == '#']

def find_best_asteroid(asteriod_list):
  seen_map = dict((asteriod, get_no_visible_asteroids(asteriod, asteriod_list)) for asteriod in asteriod_list)
  best = max(seen_map, key=seen_map.get)
  return (best,seen_map[best])

def part1(input):
  asteriod_list = get_asteriod_list(input)
  best, seen = find_best_asteroid(asteriod_list) 
  return seen

def get_no_visible_asteroids(asteriod, asteriods):
  other_asteroids = get_other_asteroids(asteriod, asteriods)
  return len(set([value[0] for value in other_asteroids.values()]))

def get_other_asteroids(asteriod, asteriods):
  others = asteriods.copy()
  others.remove(asteriod)
  return dict((other, get_angle_mag(asteriod, other),) for other in others)

def get_angle_mag(asteriod, other):
  x_diff = (other[0] - asteriod[0])
  y_diff = (asteriod[1] - other[1]) # Our y system is backwards - up is negative
  angle = math.atan2(x_diff,y_diff) % math.tau,
  return (angle, math.hypot(x_diff,y_diff))

def part2(input, number=200):
  asteriod_list = get_asteriod_list(input)
  best = find_best_asteroid(asteriod_list)[0]
  other_asteroids = get_other_asteroids(best, asteriod_list)
  angles = defaultdict(list)
  for asteroid, (angle, mag) in sorted(other_asteroids.items(), key=lambda item: item[1][0]):
    angles[angle].append((asteroid,mag))
    
  for a in angles.keys():
    angles[a] = sorted(angles[a], key=lambda value: value[1])

  destroy_order = []
  while len(angles) > 0:
    for angle, asteroid_list in sorted(angles.items()):
      destroy_order.append(angles[angle].pop(0)[0])
      if len(angles[angle]) == 0:
        del angles[angle]

  nth_destroyed = destroy_order[number-1] # 1 indexed
  return 100 * nth_destroyed[0] + nth_destroyed[1]

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))
