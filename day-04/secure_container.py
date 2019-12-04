import sys
from collections import Counter

input_file = 'day-04/input.txt'

def is_length_6(digits):
    return len(digits) == 6

def is_in_order(digits):
    return sorted(digits) == digits

def has_repeats(digits):
    return any(x >= 2 for x in Counter(digits).values())

def has_double(digits):
    return any(x == 2 for x in Counter(digits).values())

def test_password(input, count_filter):
    start,end = [int(string) for string in input.split('-')]

    digits_list = map(lambda input: [int(char) for char in str(input)], range(start, end))
    matches = list(filter(lambda x: (is_in_order(x)
        and count_filter(x) 
        and is_length_6(x)), digits_list))
    return matches

def part1(input):
    return len(test_password(input, has_repeats))

def part2(input):
    return len(test_password(input, has_double))

if __name__ == "__main__":
    with open(input_file) as f:
       data = f.read()
    print("Part 1: ", part1(data))
    print("Part 2: ", part2(data))
