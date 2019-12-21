from ship_computer import ShipComputer
import sys

input_file = 'day-21/input.txt'

# Jump if any of the next 3 are holes and 4th is ground
part1_program = """
NOT A J
NOT B T
OR T J
NOT C T
OR T J
AND D J
WALK"""[1:]

 # Part 1 AND 5th is ground, or 8th - ie we can carry on from spot we land
part2_program = part1_program.replace("WALK","""
NOT E T
NOT T T
OR H T
AND T J
RUN"""[1:])

def run_springbot_get_output(memory, program):
  memory = memory.split(",")
  robot = ShipComputer(memory)
  robot.execute_until_blocked()
  outputs = robot.get_all_outputs()
  map = "".join([ chr(c) for c in outputs])
  # print(map)

  instructions = program.splitlines()
  for instruction in instructions:
    inputs = [ ord(c) for c in instruction + '\n']
    for code in inputs:
      robot.put_input(code)
  robot.execute_until_blocked()
  outputs = robot.get_all_outputs()
  # print("".join([ chr(c) for c in outputs[:-1]]))
 
  return outputs[-1]

def part1(memory):
  return run_springbot_get_output(memory, part1_program)
  
def part2(memory):
  return run_springbot_get_output(memory, part2_program)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  # print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))
