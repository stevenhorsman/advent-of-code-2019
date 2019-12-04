import sys

input_file = 'day-04/input.txt'

def part1(input):
    start,end = [int(string) for string in input.split('-')]

    matches = []

    for i in range(start, end):
        if meets_critera(i):
            matches.append(i)
    print(matches)
    return len(matches)

def meets_critera(input):
    digits = [int(char) for char in str(input)]
    if len(digits) != 6:
        return False

    double_found = False
   
    for i in range(len(digits)-1):
        if digits[i] == digits[i+1] :
            double_found = True
        if digits[i] > digits[i+1] :
            return False # It decreases

    return double_found

def part2(input):
    start,end = [int(string) for string in input.split('-')]

    matches = []

    for i in range(start, end):
        if meets_critera2(i):
            matches.append(i)
    print(matches)
    return len(matches)

def meets_critera2(input):
    digits = [int(char) for char in str(input)]
    if len(digits) != 6:
        return False

    double_found = False
   
    for i in range(len(digits)-1):
        if digits[i] == digits[i+1] :
            if i < len(digits)-2:
                if digits[i] != digits[i+2] :
                    double_found = True
            else:
                double_found = True
        
        if digits[i] > digits[i+1] :
            return False # It decreases

    return double_found

if __name__ == "__main__":
    with open(input_file) as f:
       data = f.read()
    print("Part 1: ", part1(data))
    print("Part 2: ", part2(data))
