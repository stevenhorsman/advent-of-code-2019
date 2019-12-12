import nbody_problem
import fileinput

def test_part1_example_1():
  data = """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>"""
  assert nbody_problem.part1(data, 10) == 179

def test_part1_example_2():
  data = """<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>"""
  assert nbody_problem.part1(data,100) == 1940

def test_part1():
  with open(nbody_problem.input_file) as f:
    data = f.read()
  expected = 12466
  assert nbody_problem.part1(data,1000) == expected

def test_part2_example_1():
  data = """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>"""
  assert nbody_problem.part2(data) == 2772

def test_part2_example_2():
  data = """<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>"""
  assert nbody_problem.part2(data) == 4686774924

def test_part2():
  with open(nbody_problem.input_file) as f:
    data = f.read()
  expected = 360689156787864
  assert nbody_problem.part2(data) == expected
