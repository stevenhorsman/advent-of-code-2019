import springdroid_adventure
import fileinput

def test_part1():
  with open(springdroid_adventure.input_file) as f:
    data = f.read()
  expected = 19361023
  assert springdroid_adventure.part1(data) == expected

def test_part2():
  with open(springdroid_adventure.input_file) as f:
    data = f.read()
  expected = 1141457530
  assert springdroid_adventure.part2(data) == expected
