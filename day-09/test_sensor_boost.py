import sensor_boost
import fileinput

def test_part1():
    with open(sensor_boost.input_file) as f:
       data = f.read()
    expected = 13978427
    assert sensor_boost.part1(data) == expected

def test_part2():
  with open(sensor_boost.input_file) as f:
      data = f.read()
  expected = 11189491
  assert sensor_boost.part1(data) == expected