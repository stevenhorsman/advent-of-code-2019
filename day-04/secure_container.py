import sys
from collections import Counter

input_file = 'day-04/input.txt'

def is_length_6(digits):
    return len(digits) == 6

def is_in_order(digits):
    return all(l<=r for l,r in zip(digits, digits[1:]))
    # return sorted(digits) == digits

# from https://www.reddit.com/r/adventofcode/comments/e5u5fv/2019_day_4_solutions/f9lzbsy/
def has_adjacent_repeats(number_string):
    return any(d*2 in number_string for d in '0123456789')
    # return any(x >= 2 for x in Counter(digits).values()) # doesn't check adjacents

def has_adjacent_double(number_string):
    return any(d*2 in number_string and d*3 not in number_string for d in '0123456789')
    # return any(x == 2 for x in Counter(digits).values()) # doesn't check adjacents

def test_password(input, count_filter):
    start,end = [int(string) for string in input.split('-')]

    number_strings = map(lambda input: str(input), range(start, end + 1))
    matches = list(filter(lambda x: (is_in_order(x)
        and count_filter(x) 
        and is_length_6(x)),
        number_strings))
    return matches

def part1(input):
    return len(test_password(input, has_adjacent_repeats))

def part2(input):
    return len(test_password(input, has_adjacent_double))

if __name__ == "__main__":
    with open(input_file) as f:
       data = f.read()
    print("Part 1: ", part1(data))
    print("Part 2: ", part2(data))
