import universal_orbit_map
import fileinput

def test_part1_example_1():
  data = """COM)B
    B)C
    C)D
    D)E
    E)F
    B)G
    G)H
    D)I
    E)J
    J)K
    K)L"""
  assert universal_orbit_map.part1(data) == 42

def test_part1():
  with open(universal_orbit_map.input_file) as f:
      data = f.read()
  expected = 151345
  assert universal_orbit_map.part1(data) == expected

def test_part2_example_1():
  data = """COM)B
    B)C
    C)D
    D)E
    E)F
    B)G
    G)H
    D)I
    E)J
    J)K
    K)L
    K)YOU
    I)SAN"""
  assert universal_orbit_map.part2(data) == 4

def test_part2():
    with open(universal_orbit_map.input_file) as f:
       data = f.read()
    expected = 391
    assert universal_orbit_map.part2(data) == expected
