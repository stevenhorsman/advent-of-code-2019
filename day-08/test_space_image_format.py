import space_image_format
import fileinput

def test_part1_example_1():
  assert space_image_format.part1("123456789012", 3, 2) == 1

def test_part1():
  with open(space_image_format.input_file) as f:
    data = f.read()
  expected = 1088
  assert space_image_format.part1(data, 25, 6) == expected

def test_part2_example_1():
  expected = """01
10
"""
  assert space_image_format.part2("0222112222120000", 2, 2) == expected

def test_part2():
  with open(space_image_format.input_file) as f:
    data = f.read()
  expected = """1000001100100011001011100
1000010010100011001010010
1000010000010101111011100
1000010110001001001010010
1000010010001001001010010
1111001110001001001011100
"""
  assert space_image_format.part2(data, 25, 6) == expected
