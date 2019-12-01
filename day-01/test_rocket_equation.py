import rocket_equation
import fileinput

input_file = 'day-01/input.txt'

def test_part1_12():
    data = """12"""
    assert rocket_equation.part1(data) == 2

def test_part1_14():
    data = """14"""
    assert rocket_equation.part1(data) == 2

def test_part1_1969():
    data = """1969"""
    assert rocket_equation.part1(data) == 654

def test_part1_100756():
    data = """100756"""
    assert rocket_equation.part1(data) == 33583

def test_part1_example():
    data = """12
        14
        1969
        100756"""
    assert rocket_equation.part1(data) == 34241

def test_part1():
    with open(input_file) as f:
       data = f.read()
    expected = 3342050
    assert rocket_equation.part1(data) == expected

def test_part2_12():
    data = """12"""
    assert rocket_equation.part2(data) == 2

def test_part2_14():
    data = """14"""
    assert rocket_equation.part2(data) == 2

def test_part2_1969():
    data = """1969"""
    assert rocket_equation.part2(data) == 966

def test_part2_100756():
    data = """100756"""
    assert rocket_equation.part2(data) == 50346

def test_part2_example():
    data = """12
        14
        1969
        100756"""
    assert rocket_equation.part2(data) == 51316

def test_part2():
    with open(input_file) as f:
       data = f.read()
    expected = 5010211
    assert rocket_equation.part2(data) == expected
