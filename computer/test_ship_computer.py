from ship_computer import ShipComputer

def test_add_example_1():
    check_execute("1,0,0,0,99", "2,0,0,0,99")

def test_mul_example_2():
    check_execute("2,3,0,3,99", "2,3,0,6,99")

def test_mul_99_99_3():
    check_execute("2,4,4,5,99,0", "2,4,4,5,99,9801")

def test_seti():
    check_execute("98,1,0,99", "1,1,0,99")

# def test_add_010():
#   check_execute("1002,4,3,4,33", "1002,4,3,4,99")

# def test_negative_add():
#   check_execute("1101,100,-1,4,0", "1101,100,-1,4,99")

def test_part1_example_4():
  check_execute("1,1,1,4,99,5,6,0,99", "30,1,1,4,2,5,6,0,99")

def test_input_output():
  ship_computer = execute("3,0,4,0,99",26)
  assert ship_computer.output == [26]

def test_part1_example_5():
    check_execute("1,9,10,3,2,3,11,0,99,30,40,50",
                  "3500,9,10,70,2,3,11,0,99,30,40,50")
                  
def check_execute(input, output):
  memory = input.split(",")
  ship_computer = ShipComputer(memory)
  ship_computer.execute()
  assert ship_computer.get_memory() == [int(i) for i in output.split(",")]

def execute(initial_memory, input = None):
  memory = initial_memory.split(",")
  ship_computer = ShipComputer(memory, input)
  ship_computer.execute()
  return ship_computer
