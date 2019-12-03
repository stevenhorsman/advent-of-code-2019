import sys

input_file = 'day-03/input.txt'

def produce_tick_map(path_string):
    deltas = dict(zip('RLUD', [(1, 0), (-1, 0), (0, 1), (0, -1)]))
    
    x = 0
    y = 0 
    tick = 0
    wire_path = {}
    for path in path_string:
        direction = path[:1]
        length = int(path [1:])
        for _ in range(length):
            x += deltas[direction][0]
            y += deltas[direction][1]
            point = (x,y)
            tick+=1
            if point not in wire_path:
                wire_path[point] = tick
    return wire_path

def calculate_wire_overlaps(input, overlap_value_fn):
    lines = input.split() # str.split without any arguments splits on any whitespace and essentially strips leading/trailing whitespace.
    wire1 = lines[0].split(",")
    wire2 = lines[1].split(",")

    wire1_path = produce_tick_map(wire1)
    wire2_path = produce_tick_map(wire2)

    crosses = wire1_path.keys() & wire2_path.keys() # keys are sets in python == set(wire1_path.keys()) & set(wire2_path.keys())
    cross_distances = [overlap_value_fn(wire1_path, wire2_path, x) for x in crosses]

    return min(cross_distances)

def manhattan(map1, map2, point):
    return abs(point[0]) + abs(point[1])

def part1(input):
    return calculate_wire_overlaps(input, manhattan)

def sum_ticks(map1, map2, key):
    return map1[key] + map2[key]

def part2(input):
    return calculate_wire_overlaps(input, sum_ticks)

if __name__ == "__main__":
    with open(input_file) as f:
       data = f.read()
    print("Part 1: ", part1(data))
    print("Part 2: ", part2(data))
