import set_and_forget
import fileinput

def test_part1():
  with open(set_and_forget.input_file) as f:
    data = f.read()
  expected = 4600
  assert set_and_forget.part1(data) == expected

def test_part2():
  with open(set_and_forget.input_file) as f:
    data = f.read()
  expected = 1113411
  assert set_and_forget.part2(data) == expected

def test_part2_craig():
  with open('day-17/craig.txt') as f:
    data = f.read()
  expected = 914900
  assert set_and_forget.part2(data) == expected

def test_part2_amf():
  with open('day-17/amf.txt') as f:
    data = f.read()
  expected = 945911
  assert set_and_forget.part2(data) == expected

def test_part2_hindess():
  with open('day-17/hindess.txt') as f:
    data = f.read()
  expected = 762405
  assert set_and_forget.part2(data) == expected
