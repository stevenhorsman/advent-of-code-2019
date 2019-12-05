import assembler

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

def check_execute(input, output):
    data = input.split(",")
    assert assembler.execute(data) == [int(i) for i in output.split(",")]
