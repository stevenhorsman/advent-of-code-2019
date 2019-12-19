import many_worlds_interpretation
import fileinput
import pytest

def test_part1_example_1():
  data = """
#########
#b.A.@.a#
#########"""[1:]
  assert many_worlds_interpretation.part1(data) == 8

def test_part1_example_1_dead_ends():
  data = """
###########
#.b.A.@.a.#
###########"""[1:]
  assert many_worlds_interpretation.part1(data) == 8

def test_part1_example_2():
  data = """
########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################"""[1:]
  assert many_worlds_interpretation.part1(data) == 86

def test_part1_example_3():
  data = """
########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################"""[1:]
  assert many_worlds_interpretation.part1(data) == 132

def test_part1_example_4():
  data = """
#################
#i.G..c...e..H.p#
########.########
#j.A..b...f..D.o#
########@########
#k.E..a...g..B.n#
########.########
#l.F..d...h..C.m#
#################"""[1:]
  assert many_worlds_interpretation.part1(data) == 136

def test_part1_example_5():
  data = """
########################
#@..............ac.GI.b#
###d#e#f################
###A#B#C################
###g#h#i################
########################"""[1:]
  assert many_worlds_interpretation.part1(data) == 81

def test_part1_example_6():
  data = """
########################
#@..............ac.GI.b#
###d###f################
###A###C################
###g###i################
########################"""[1:]
  assert many_worlds_interpretation.part1(data) == 61

def test_part1():
  with open(many_worlds_interpretation.input_file) as f:
    data = f.read()
  expected = 3512
  assert many_worlds_interpretation.part1(data) == expected

def test_part2_example_1():
  data = """
#######
#a.#Cd#
##@#@##
#######
##@#@##
#cB#Ab#
#######"""[1:]
  assert many_worlds_interpretation.part2(data) == 8

def test_part2_example_2():
  data = """
###############
#d.ABC.#.....a#
######@#@######
###############
######@#@######
#b.....#.....c#
###############"""[1:]
  assert many_worlds_interpretation.part2(data) == 24

def test_part2_example_3():
  data = """
#############
#DcBa.#.GhKl#
#.###@#@#I###
#e#d#####j#k#
###C#@#@###J#
#fEbA.#.FgHi#
#############"""[1:]
  assert many_worlds_interpretation.part2(data) == 32

def test_part2_example_4():
  data = """
#############
#g#f.D#..h#l#
#F###e#E###.#
#dCba@#@BcIJ#
#############
#nK.L@#@G...#
#M###N#H###.#
#o#m..#i#jk.#
#############"""[1:]
  assert many_worlds_interpretation.part2(data) == 72

def test_part2():
  with open(many_worlds_interpretation.input_file.replace("input.txt", "input_part2.txt")) as f:
    data = f.read()
  expected = 1514
  assert many_worlds_interpretation.part2(data) == expected
