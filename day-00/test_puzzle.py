import puzzle
import fileinput

input_file = 'day-00/input.txt'

def test_part1_example():
    data = """+1
       -2
       +3
       +1"""
    assert puzzle.part1(data) == 3

def test_part1():
    with open(input_file) as f:
       data = f.read()
    expected = 500
    assert puzzle.part1(data) == expected

def test_part2_example():
    data = """-6
         +3
         +8
         +5
         -6"""
    assert puzzle.part2(data) == 5

def test_part2():
    with open(input_file) as f:
       data = f.read()
    expected = 709
    assert puzzle.part2(data) == expected
