import many_worlds_interpretation
import fileinput

def test_part1_example_1():
  data = """#########
#b.A.@.a#
#########"""
  assert many_worlds_interpretation.part1(data) == 8

def test_part1_example_2():
  data = """########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################"""
  assert many_worlds_interpretation.part1(data) == 86

def test_part1_example_3():
  data = """########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################"""
  assert many_worlds_interpretation.part1(data) == 132

def test_part1_example_4():
  data = """#################
#i.G..c...e..H.p#
########.########
#j.A..b...f..D.o#
########@########
#k.E..a...g..B.n#
########.########
#l.F..d...h..C.m#
#################"""
  assert many_worlds_interpretation.part1(data) == 136

def test_part1_example_5():
  data = """########################
#@..............ac.GI.b#
###d#e#f################
###A#B#C################
###g#h#i################
########################"""
  assert many_worlds_interpretation.part1(data) == 81

def test_part1():
  with open(many_worlds_interpretation.input_file) as f:
    data = f.read()
  expected = 221
  assert many_worlds_interpretation.part1(data) == expected

def test_part2_example_1():
  data = """R8,U5,L5,D3
  U7,R6,D4,L4"""
  assert many_worlds_interpretation.part2(data) == 30

def test_part2_example_2():
  data = """R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83"""
  assert many_worlds_interpretation.part2(data) == 610

def test_part2_example_3():
  data = """R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"""
  assert many_worlds_interpretation.part2(data) == 410

def test_part2():
  with open(many_worlds_interpretation.input_file) as f:
    data = f.read()
  expected = 18542
  assert many_worlds_interpretation.part2(data) == expected
