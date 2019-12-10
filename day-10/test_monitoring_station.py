import monitoring_station
import fileinput

def test_part1_example_1():
  data = """.#..#
            .....
            #####
            ....#
            ...##"""
  assert monitoring_station.part1(data) == 8

def test_part1_example_2():
  data = """......#.#.
            #..#.#....
            ..#######.
            .#.#.###..
            .#..#.....
            ..#....#.#
            #..#....#.
            .##.#..###
            ##...#..#.
            .#....####"""
  assert monitoring_station.part1(data) == 33

def test_part1_example_3():
  data = """#.#...#.#.
            .###....#.
            .#....#...
            ##.#.#.#.#
            ....#.#.#.
            .##..###.#
            ..#...##..
            ..##....##
            ......#...
            .####.###."""
  assert monitoring_station.part1(data) == 35

def test_part1_example_4():
  data = """.#..#..###
            ####.###.#
            ....###.#.
            ..###.##.#
            ##.##.#.#.
            ....###..#
            ..#.#..#.#
            #..#.#.###
            .##...##.#
            .....#.#.."""
  assert monitoring_station.part1(data) == 41

def test_part1_example_5():
  data = """.#..##.###...#######
            ##.############..##.
            .#.######.########.#
            .###.#######.####.#.
            #####.##.#.##.###.##
            ..#####..#.#########
            ####################
            #.####....###.#.#.##
            ##.#################
            #####.##.###..####..
            ..######..##.#######
            ####.##.####...##..#
            .#####..#.######.###
            ##...#.##########...
            #.##########.#######
            .####.#.###.###.#.##
            ....##.##.###..#####
            .#.#.###########.###
            #.#.#.#####.####.###
            ###.##.####.##.#..##"""
  assert monitoring_station.part1(data) == 210

def test_part1():
  with open(monitoring_station.input_file) as f:
    data = f.read()
  expected = 303
  assert monitoring_station.part1(data) == expected

def test_part2_example_1():
  data = """.#..#
            .....
            #####
            ....#
            ...##"""
  check_part_2(data, destroyed_no=1, destroyed=(3,2))
  check_part_2(data, destroyed_no=2, destroyed=(4,0))

def test_part2_example_5():
  data = """.#..##.###...#######
            ##.############..##.
            .#.######.########.#
            .###.#######.####.#.
            #####.##.#.##.###.##
            ..#####..#.#########
            ####################
            #.####....###.#.#.##
            ##.#################
            #####.##.###..####..
            ..######..##.#######
            ####.##.####...##..#
            .#####..#.######.###
            ##...#.##########...
            #.##########.#######
            .####.#.###.###.#.##
            ....##.##.###..#####
            .#.#.###########.###
            #.#.#.#####.####.###
            ###.##.####.##.#..##"""
  check_part_2(data, destroyed_no=1, destroyed=(11,12))
  check_part_2(data, destroyed_no=2, destroyed=(12,1))  
  check_part_2(data, destroyed_no=3, destroyed=(12,2))  
  check_part_2(data, destroyed_no=10, destroyed=(12,8))  
  check_part_2(data, destroyed_no=20, destroyed=(16,0))  
  check_part_2(data, destroyed_no=50, destroyed=(16,9))  
  check_part_2(data, destroyed_no=100, destroyed=(10,16))  
  check_part_2(data, destroyed_no=199, destroyed=(9,6))     
  check_part_2(data, destroyed=(8,2))
  check_part_2(data, destroyed_no=201, destroyed=(10,9))  
  check_part_2(data, destroyed_no=299, destroyed=(11,1))  

def test_part2():
  with open(monitoring_station.input_file) as f:
    data = f.read()
  expected = (4,8)
  check_part_2(data, destroyed=expected)

def check_part_2(data, destroyed_no = 200, destroyed=(0,0)):
  assert monitoring_station.part2(data, destroyed_no) == destroyed[0] * 100 + destroyed[1]

