import sys
import math
from collections import defaultdict 

input_file = 'day-10/input.txt'

def get_asteriod_list(input):
  asteriod_list = []
  lines = input.split()
  for y in range(0, len(lines)):
    line = [char for char in lines[y]]
    for x in range(0, len(line)):
      if line[x] == '#':
        asteriod_list.append((x,y))
  return asteriod_list

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
  # atan 2 works out the anticlockwise angle from the x-axis
  angle = (math.pi/2 - math.atan2(y_diff,x_diff)) % math.tau,
  return (angle, math.hypot(x_diff,y_diff))
  # atan2 equiv to 
  # angle = math.pi/2
  # if y_diff != 0:
  #   angle = math.atan(round(x_diff/y_diff,5))
  # elif x_diff < 0:
  #   angle += math.pi

  # if y_diff < 0:
  #   angle += math.pi
  #   angle = angle % math.tau
  # return angle

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
