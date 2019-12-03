import sys

input_file = 'day-03/input.txt'

def produce_tick_map(path_string):
    x = 0
    y = 0 
    tick = 0
    wire_path = {}
    for path in path_string:
        direction = path[:1]
        length = path [1:]
        for _ in range(int(length)):
            if direction == 'R':
                x+=1
            if direction == 'L':
                x-=1
            if direction == 'U':
                y+=1
            if direction == 'D':
                y-=1
            point = (x,y)
            tick+=1
            if point not in wire_path:
                wire_path[point] = tick
    return wire_path

def calculate_wire_overlaps(input, overlap_value_fn):
    lines = [i.strip() for i in input.splitlines()]
    wire1 = lines[0].split(",")
    wire2 = lines[1].split(",")

    wire1_path = produce_tick_map(wire1)
    wire2_path = produce_tick_map(wire2)

    crosses = set(wire1_path.keys()) & set(wire2_path.keys())
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
