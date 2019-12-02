def part1(input):
    lines = input.splitlines()
    return sum(fuel_calc(int(line)) for line in lines)

def fuel_calc(input):
    return (input // 3) - 2  # // is floor divison == math.floor(input/3) - 2

def recursive_fuel_calc(input):
    curr = fuel_calc(input)
    if curr > 0:
        return curr + recursive_fuel_calc(curr)
    else:
        return 0

def part2(input):
    lines = input.splitlines()
    return sum(recursive_fuel_calc(int(line)) for line in lines)

if __name__ == "__main__":
    input_file = 'day-01/input.txt'
    with open(input_file) as f:
       data = f.read()
    print("Part 1: ", part1(data))
    print("Part 2: ", part2(data))