import sys
from ship_computer import ShipComputer

def part1(input, noun="12", verb="2"):
    inputs = input.split(",").copy()
    inputs[1] = noun
    inputs[2] = verb
    ship_computer = ShipComputer(inputs)
    result = ship_computer.execute()
    return result[0]

def part2(input):
    for noun in range(1, 100):
        for verb in range(1, 100):
            if part1(input, str(noun), str(verb)) == 19690720:
                return 100 * noun + verb

if __name__ == "__main__":
    input_file = 'day-02/input.txt'
    with open(input_file) as f:
       data = f.read()
    print("Part 1: ", part1(data))
    print("Part 2: ", part2(data))