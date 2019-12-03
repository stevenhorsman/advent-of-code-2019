import sys

def part1(input):
    lines = [i.strip() for i in input.splitlines()]
    wire1 = lines[0].split(",")
    wire2 = lines[1].split(",")

    x = 0
    y = 0 
    wire1_path = []
    for path in wire1:
        direction = path[:1]
        length = path [1:]
        for i in range(0, int(length)): 
            if direction == 'R':
                x+=1
                wire1_path.append((x,y))
            if direction == 'L':
                x-=1
                wire1_path.append((x,y))
            if direction == 'U':
                y+=1
                wire1_path.append((x,y))
            if direction == 'D':
                y-=1
                wire1_path.append((x,y))

    x = 0
    y = 0 
    wire2_path = []
    for path in wire2:
        direction = path[:1]
        length = path [1:]
        for i in range(0, int(length)): 
            if direction == 'R':
                x+=1
                wire2_path.append((x,y))
            if direction == 'L':
                x-=1
                wire2_path.append((x,y))
            if direction == 'U':
                y+=1
                wire2_path.append((x,y))
            if direction == 'D':
                y-=1
                wire2_path.append((x,y))

    print(wire1_path)
    print(wire2_path)

    crosses = set(wire1_path) & set(wire2_path)

    cross_distances = map(manhattan, crosses)

    print("Crosses", cross_distances)

    return min(cross_distances)

def manhattan(point):
    return abs(point[0]) + abs(point[1])

def part2(input):
    return part1(input)

if __name__ == "__main__":
    input_file = 'day-03/input.txt'
    with open(input_file) as f:
       data = f.read()
    print("Part 1: ", part1(data))
    print("Part 2: ", part2(data))
