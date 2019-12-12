import sys
import re
import itertools
import math

input_file = 'day-12/input.txt'

class Body:
  def __init__(self, input_string):
    # From https://github.com/sophiebits/adventofcode/blob/master/2019/day12.py
    self.pos = [int(i) for i in re.findall(r'-?\d+', input_string)]
    self.vel = [0, 0, 0]
  
  def apply_gravity(self, other_body):
    for axis in range(0, len(self.pos)):
      if (self.pos[axis] > other_body.pos[axis]):
        self.vel[axis] -= 1
      if (self.pos[axis] < other_body.pos[axis]):
        self.vel[axis] += 1

  def update(self):
    for axis in range(0, len(self.pos)):
      self.pos[axis] += self.vel[axis]

  def get_potential_energy(self):
    return sum(abs(x) for x in self.pos)

  def get_kinetic_energy(self):
    return sum(abs(x) for x in self.vel)

  def get_energy(self):
    return self.get_kinetic_energy() * self.get_potential_energy()

  def __repr__(self):
    return "pos=<x=%d, y=%d, z=%d>, vel=<x=%d, y=%d, z=%d> total=%d" % (self.pos[0], self.pos[1] ,self.pos[2], self.vel[0], self.vel[1], self.vel[2], self.get_energy())

def step(bodies):
  for index_1, index_2 in itertools.combinations(range(0,len(bodies)), 2):
      bodies[index_1].apply_gravity(bodies[index_2])
      bodies[index_2].apply_gravity(bodies[index_1])
  for body in bodies:
    body.update()

def part1(input, ticks):
  bodies = [Body(line.strip()) for line in input.splitlines()]
  for tick in range(0,ticks):
    step(bodies)
  return sum(body.get_energy() for body in bodies)

def part2(input):
  bodies = [Body(line.strip()) for line in input.splitlines()]
  init_x = [(body.pos[0],body.vel[0]) for body in bodies]
  init_y = [(body.pos[1],body.vel[1]) for body in bodies]
  init_z = [(body.pos[2],body.vel[2]) for body in bodies]
  repeats = [0, 0, 0]

  ticks = 0
  while any(item == 0 for item in repeats):
    step(bodies)
    ticks +=1
    if repeats[0] == 0 and ([(body.pos[0],body.vel[0]) for body in bodies] == init_x):
      repeats[0] = ticks
    if repeats[1] == 0 and ([(body.pos[1],body.vel[1]) for body in bodies] == init_y):
      repeats[1] = ticks
    if repeats[2] == 0 and ([(body.pos[2],body.vel[2]) for body in bodies] == init_z):
      repeats[2] = ticks

  lcm = (repeats[0]*repeats[1]) // math.gcd(repeats[0],repeats[1])
  return (lcm*repeats[2]) // math.gcd(lcm,repeats[2])

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))
