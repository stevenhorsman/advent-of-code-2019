import sys
from ship_computer import ShipComputer

input_file = 'day-05/input.txt'

def part1(memory, input = 1):
    memory = memory.split(",").copy()
    ship_computer = ShipComputer(memory, input)
    ship_computer.execute()
    return ship_computer.get_output()

def part2(input):
    pass
    for noun in range(1, 100):
        for verb in range(1, 100):
            if part1(input, str(noun), str(verb)) == 19690720:
                return 100 * noun + verb

if __name__ == "__main__":
    with open(input_file) as f:
       data = f.read()
    print("Part 1: ", part1(data))
    print("Part 2: ", part2(data))
