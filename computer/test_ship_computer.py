from ship_computer import ShipComputer

def test_add_example_1():
    check_execute("1,0,0,0,99", "2,0,0,0,99")

def test_mul_example_2():
    check_execute("2,3,0,3,99", "2,3,0,6,99")

def test_mul_99_99_3():
    check_execute("2,4,4,5,99,0", "2,4,4,5,99,9801")

def test_seti():
    check_execute("98,1,0,99", "1,1,0,99")

def test_mul_immediate():
  check_execute("1002,4,3,4,33", "1002,4,3,4,99")

def test_negative_add():
  check_execute("1101,100,-1,4,0", "1101,100,-1,4,99")

def test_part1_example_4():
  check_execute("1,1,1,4,99,5,6,0,99", "30,1,1,4,2,5,6,0,99")

def test_input_output():
  ship_computer = execute("3,0,4,0,99",26)
  assert ship_computer.get_output() == 26

def test_part1_example_5():
    check_execute("1,9,10,3,2,3,11,0,99,30,40,50", "3500,9,10,70,2,3,11,0,99,30,40,50")
                  
def check_execute(input, output):
  memory = input.split(",")
  ship_computer = ShipComputer(memory)
  ship_computer.execute()
  expected = [int(i) for i in output.split(",")]
  expected.append([0] * 1000)
  assert ship_computer.get_memory() == expected

def execute(initial_memory, input = None):
  memory = initial_memory.split(",")
  ship_computer = ShipComputer(memory, input)
  ship_computer.execute()
  return ship_computer

def test_jump_if_true_doesnt_jumps():
  ship_computer = execute("1105,0,6,4,1,99,4,0,99")
  assert ship_computer.get_output() == 0

def test_jump_if_true_jumps():
  ship_computer = execute("1105,1,6,4,1,99,4,0,99")
  assert ship_computer.get_output() == 1105

def test_relative_base_set():
  ship_computer = execute("109,2000,109,19,99")
  assert ship_computer.relative_base == 2019

def test_output_relative_mode():
  ship_computer = execute("109,2000,204,-1999,99")
  assert ship_computer.get_output() == 2000

def test_equals_8_position_mode():
  program = "3,9,8,9,10,9,4,9,99,-1,8"
  check_equals_8(program,7)
  check_equals_8(program,8)
  check_equals_8(program,9)

def test_equals_8_immediate_mode():
  program = "3,3,1108,-1,8,3,4,3,99"
  check_equals_8(program,7)
  check_equals_8(program,8)
  check_equals_8(program,9)

def check_equals_8(memory, input):
  ship_computer = execute(memory,input)
  expected = 1 if input == 8 else 0
  assert ship_computer.get_output() == expected

def test_less_than_8_position_mode():
  program = "3,9,7,9,10,9,4,9,99,-1,8"
  check_less_than_8(program,7)
  check_less_than_8(program,8)
  check_less_than_8(program,9)

def test_less_than_8_immediate_mode():
  program = "3,3,1107,-1,8,3,4,3,99"
  check_less_than_8(program,7)
  check_less_than_8(program,8)
  check_less_than_8(program,9)

def check_less_than_8(memory, input):
  ship_computer = execute(memory,input)
  expected = 1 if input < 8 else 0
  assert ship_computer.get_output() == expected

def test_equals_0_position_mode():
  program = "3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9"
  # check_equals_0(program,-1)
  check_equals_0(program,0)
  # check_equals_0(program,1)

def test_equals_0_immediate_mode():
  program = "3,3,1105,-1,9,1101,0,0,12,4,12,99,1"
  check_equals_0(program,-1)
  check_equals_0(program,0)
  check_equals_0(program,1)

def check_equals_0(memory, input):
  ship_computer = execute(memory,input)
  expected = 0 if input == 0 else 1
  assert ship_computer.get_output() == expected

def test_compare_to_8_immediate_mode():
  program = """3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"""
  check_compare_to_8(program,7,999)
  check_compare_to_8(program,8,1000)
  check_compare_to_8(program,9,1001)

def check_compare_to_8(memory, input, expected):
  ship_computer = execute(memory,input)
  assert ship_computer.get_output() == expected

def test_computer_memory_capacity():
  quine = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
  ship_computer = execute(quine)
  assert ship_computer.get_output() == quine

def test_handle_big_numbers():
  program = "1102,34915192,34915192,7,4,7,99,0"
  ship_computer = execute(program)
  assert ship_computer.get_output() > 2^15

def test_handle_big_numbers_2():
  program = "104,1125899906842624,99"
  ship_computer = execute(program)
  assert ship_computer.get_output() == 1125899906842624