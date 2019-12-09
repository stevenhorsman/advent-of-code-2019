import sys
from ship_computer import ShipComputer

input_file = 'day-09/input.txt'

def part1(memory, input = 1):
    memory = memory.split(",")
    ship_computer = ShipComputer(memory, input)
    ship_computer.execute()
    return ship_computer.get_output()

def part2(input):
  return part1(input,2)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))
