import slam_shuffle
import fileinput

def test_part1_example_0():
  data = ""
  expected = "0 1 2 3 4 5 6 7 8 9"
  check_10_deck(data, expected)

def test_part1_example_new_stack():
  data = "deal into new stack"
  expected = "9 8 7 6 5 4 3 2 1 0"
  check_10_deck(data, expected)

def test_part1_example_cut_3():
  data = "cut 3"
  expected = "3 4 5 6 7 8 9 0 1 2"
  check_10_deck(data, expected)

def test_part1_example_cut_neg_4():
  data = "cut -4"
  expected = "6 7 8 9 0 1 2 3 4 5"
  check_10_deck(data, expected)

def test_part1_example_deal_with_increment_3():
  data = "deal with increment 3"
  expected = "0 7 4 1 8 5 2 9 6 3"
  check_10_deck(data, expected)  

def test_part1_example_1():
  data = """deal with increment 7
deal into new stack
deal into new stack"""
  expected = "0 3 6 9 2 5 8 1 4 7"
  check_10_deck(data, expected)

def test_part1_example_2():
  data = """cut 6
deal with increment 7
deal into new stack"""
  expected = "3 0 7 4 1 8 5 2 9 6"
  check_10_deck(data, expected)

def test_part1_example_3():
  data = """deal with increment 7
deal with increment 9
cut -2"""
  expected = "6 3 0 7 4 1 8 5 2 9"
  check_10_deck(data, expected)

def test_part1_example_4():
  data = """deal into new stack
cut -2
deal with increment 7
cut 8
cut -4
deal with increment 7
cut 3
deal with increment 9
deal with increment 3
cut -1"""
  expected = "9 2 5 8 1 4 7 0 3 6"
  check_10_deck(data, expected)

def test_part1_example_3():
  data = """cut 6
deal with increment 7
deal into new stack"""
  expected = "3 0 7 4 1 8 5 2 9 6"
  check_10_deck(data, expected)

def check_10_deck(instructions, expected):
  expected = [int(i) for i in expected.split()]
  assert slam_shuffle.part1(instructions, 10) == expected

def test_part1():
  with open(slam_shuffle.input_file) as f:
    data = f.read()
  expected = 3939
  assert slam_shuffle.part1(data, 10007, 2019) == expected

def test_part2_example_part1():
  with open(slam_shuffle.input_file) as f:
    data = f.read()
  expected = 7726
  assert slam_shuffle.part2(data, 10007, 2019, 1) == expected

def test_part2():
  with open(slam_shuffle.input_file) as f:
    data = f.read()
  expected = 55574110161534
  assert slam_shuffle.part2(data, 119315717514047, 2020, 101741582076661) == expected
