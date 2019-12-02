import program_alarm
import fileinput

input_file = 'day-02/input.txt'

def test_part1():
    with open(input_file) as f:
       data = f.read()
    expected = 5305097
    assert program_alarm.part1(data) == expected

def test_part2():
    with open(input_file) as f:
       data = f.read()
    expected = 4925
    assert program_alarm.part2(data) == expected
