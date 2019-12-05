import assembler

def test_add_010():
  check_execute("1002,4,3,4,33", "1002,4,3,4,99")

def test_negative_add():
  check_execute("1101,100,-1,4,0", "1101,100,-1,4,99")

def test_input():
  assert False
  check_execute("2,4,4,5,99,0", "2,4,4,5,99,9801")

def test_out():
  check_execute("4,0,99", "4,0,99") # Should print 4, how to check?

def test_part1_example_5():
    check_execute("1,9,10,3,2,3,11,0,99,30,40,50", "3500,9,10,70,2,3,11,0,99,30,40,50")

def check_execute(input, output):
    data = input.split(",")
    assert assembler.execute(data) == [int(i) for i in output.split(",")]
