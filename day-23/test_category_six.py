import category_six
import fileinput

def test_part1():
  with open(category_six.input_file) as f:
    data = f.read()
  expected = 17949
  assert category_six.part1(data) == expected

def test_part2():
  with open(category_six.input_file) as f:
    data = f.read()
  expected = 12326
  assert category_six.part2(data) == expected
