import crossed_wires
import fileinput

def test_part1_example_1():
  data = """R8,U5,L5,D3
  U7,R6,D4,L4"""
  assert crossed_wires.part1(data) == 6

def test_part1_example_2():
  data = """R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83"""
  assert crossed_wires.part1(data) == 159

def test_part1_example_3():
  data = """R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"""
  assert crossed_wires.part1(data) == 135

def test_part1():
  with open(crossed_wires.input_file) as f:
    data = f.read()
  expected = 221
  assert crossed_wires.part1(data) == expected

def test_part2_example_1():
  data = """R8,U5,L5,D3
  U7,R6,D4,L4"""
  assert crossed_wires.part2(data) == 30

def test_part2_example_2():
  data = """R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83"""
  assert crossed_wires.part2(data) == 610

def test_part2_example_3():
  data = """R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"""
  assert crossed_wires.part2(data) == 410

def test_part2():
  with open(crossed_wires.input_file) as f:
    data = f.read()
  expected = 18542
  assert crossed_wires.part2(data) == expected
