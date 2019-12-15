import oxygen_system
import fileinput

def test_part1():
  with open(oxygen_system.input_file) as f:
    data = f.read()
  expected = 374
  assert oxygen_system.part1(data) == expected

def test_part2():
  with open(oxygen_system.input_file) as f:
    data = f.read()
  expected = 482
  assert oxygen_system.part2(data) == expected
