import tractor_beam
import fileinput

def test_part1():
  with open(tractor_beam.input_file) as f:
    data = f.read()
  expected = 213
  assert tractor_beam.part1(data) == expected

def test_part2():
  with open(tractor_beam.input_file) as f:
    data = f.read()
  expected = 7830987
  assert tractor_beam.part2(data) == expected
