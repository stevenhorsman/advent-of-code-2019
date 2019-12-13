import care_package
import fileinput

def test_part1():
  with open(care_package.input_file) as f:
    data = f.read()
  expected = 200
  assert care_package.part1(data) == expected

def test_part2():
  with open(care_package.input_file) as f:
    data = f.read()
  expected = 9803
  assert care_package.part2(data) == expected
