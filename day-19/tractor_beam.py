from ship_computer import ShipComputer
import sys
import math

input_file = 'day-19/input.txt'

def is_tractor(memory, x, y):
  robot = ShipComputer(memory)
  robot.put_input(x)
  robot.put_input(y)
  robot.execute_until_blocked()
  return robot.get_output()

def find_beam_edges(memory, y, guess_min = 0, guess_max = 0):
  grid = {}
  start, stop = 0, 0
  for x in range(guess_min, y):
    tractor = is_tractor(memory, x, y)
    if tractor == 1:
      start = x
      break

  guess_max = max(guess_max, start)
  for x in range(guess_max, y):
    tractor = is_tractor(memory, x, y)
    if tractor == 0:
      stop = x
      break
  return start, stop

# Narrow down on start and stop ratios, getting more accurate each iteration
def find_ratios(memory, max_exp = 4):
  start_ratio, stop_ratio = 0, 0
  scale_ratio = 100
  base_factor = (scale_ratio + math.log(10**max_exp))

  for exp in range(1, max_exp+1):
    y_val = 10**exp
    start, stop = find_beam_edges(memory, y_val, round(start_ratio*y_val), round(stop_ratio*y_val))
    start_ratio = (start/y_val) * (scale_ratio + math.log(y_val)) / base_factor
    stop_ratio = (stop/y_val) * (scale_ratio + math.log(y_val)) / base_factor

  return start_ratio, stop_ratio

def follow_program(memory, size, start_ratio, stop_ratio):
  grid = {}
  for j in range(size):
    start_guess = math.floor(start_ratio * 0.9 * j)
    stop_guess = math.ceil(stop_ratio * 1.1 * j)
    for i in range(start_guess, stop_guess+1):
      grid[(i,j)] = is_tractor(memory, i, j)
  return grid

def part1(memory, size = 50):
  memory = memory.split(",")
  start_ratio, stop_ratio = find_ratios(memory, 3)
  grid = follow_program(memory, size, start_ratio, stop_ratio)
  return list(grid.values()).count(1)

def part2(memory):
  memory = memory.split(",")
  start_ratio, stop_ratio = find_ratios(memory)
  # Trying to solve stop_ratio * y - 100 = start_ratio * (y + 99)
  approx_y = round((100 + (start_ratio*99)) / (stop_ratio - start_ratio))

  for offset in range(-10,10):
    y_offset = approx_y + offset
    start, stop = find_beam_edges(memory, y_offset, round(start_ratio*y_offset), round(stop_ratio*y_offset))
    if is_tractor(memory, stop - 100, y_offset + 99):
      return (stop - 100) * 10000 + y_offset

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))
