import program_alarm
import fileinput

input_file = 'day-02/input.txt'

def test_part1_example_1():
    check_execute("1,0,0,0,99", "2,0,0,0,99")

def test_part1_example_2():
    check_execute("2,3,0,3,99", "2,3,0,6,99")

def test_part1_example_3():
    check_execute("2,4,4,5,99,0", "2,4,4,5,99,9801")

def test_part1_example_4():
    check_execute("1,1,1,4,99,5,6,0,99", "30,1,1,4,2,5,6,0,99")

def test_part1_example_5():
    check_execute("1,9,10,3,2,3,11,0,99,30,40,50", "3500,9,10,70,2,3,11,0,99,30,40,50")

def test_part1():
    with open(input_file) as f:
       data = f.read()
    expected = 5305097
    assert program_alarm.part1(data) == expected

def check_execute(input, output):
    data = input.split(",")
    assert program_alarm.execute(data) == [int(i) for i in output.split(",")]


# def test_part2_12():
#     data = """12"""
#     assert program_alarm.part2(data) == 2

# def test_part2_14():
#     data = """14"""
#     assert program_alarm.part2(data) == 2

# def test_part2_1969():
#     data = """1969"""
#     assert program_alarm.part2(data) == 966

# def test_part2_100756():
#     data = """100756"""
#     assert program_alarm.part2(data) == 50346

# def test_part2_example():
#     data = """12
#         14
#         1969
#         100756"""
#     assert program_alarm.part2(data) == 51316

# def test_part2():
#     with open(input_file) as f:
#        data = f.read()
#     expected = 5020211
#     assert program_alarm.part2(data) == expected
