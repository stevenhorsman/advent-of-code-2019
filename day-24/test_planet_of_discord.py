import planet_of_discord
import fileinput

def test_part1_example_1():
  data = """
....#
#..#.
#..##
..#..
#...."""[1:]
  assert planet_of_discord.part1(data) == 2129920

def test_part1():
  with open(planet_of_discord.input_file) as f:
    data = f.read()
  expected = 1151290
  assert planet_of_discord.part1(data) == expected

def test_part2_example_1():
  data = """
....#
#..#.
#..##
..#..
#...."""[1:]
  assert planet_of_discord.part2(data,10) == 99

def test_part2():
  with open(planet_of_discord.input_file) as f:
    data = f.read()
  expected = 1953
  assert planet_of_discord.part2(data) == expected
