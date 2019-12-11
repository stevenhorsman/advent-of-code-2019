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
  expected = """.#
#.
"""
  assert space_image_format.part2("0222112222120000", 2, 2) == expected

def test_part2():
  with open(space_image_format.input_file) as f:
    data = f.read()
  expected = """
#.....##..#...##..#.###..
#....#..#.#...##..#.#..#.
#....#.....#.#.####.###..
#....#.##...#..#..#.#..#.
#....#..#...#..#..#.#..#.
####..###...#..#..#.###..
"""[1:]
  assert space_image_format.part2(data, 25, 6) == expected
