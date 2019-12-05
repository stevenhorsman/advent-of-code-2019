import sunny_with_asteroids
import fileinput

def test_part1():
    with open(sunny_with_asteroids.input_file) as f:
       data = f.read()
    expected = 13978427
    assert sunny_with_asteroids.part1(data,1) == expected

def test_part2():
  with open(sunny_with_asteroids.input_file) as f:
      data = f.read()
  expected = 11189491
  assert sunny_with_asteroids.part1(data,5) == expected
