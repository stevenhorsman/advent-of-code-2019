import cryostasis
import fileinput

def test_part1():
  with open(cryostasis.input_file) as f:
    data = f.read()
  expected = 136839232
  assert cryostasis.part1(data) == expected

