import sensor_boost
import fileinput

def test_part1():
  with open(sensor_boost.input_file) as f:
    data = f.read()
  expected = 3340912345
  assert sensor_boost.part1(data) == expected

def test_part2():
  with open(sensor_boost.input_file) as f:
    data = f.read()
  expected = 51754
  assert sensor_boost.part2(data) == expected
