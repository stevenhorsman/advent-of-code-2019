import sys

class IntCode:
    def __init__(self, name, runFunction, ip_offset):
        self.name = name
        self.runFunction = runFunction
        self.ip_offset = ip_offset

    def run(self, memory, offset):
        output, result = self.runFunction(memory, offset)
        if (output != None):
            memory[output] = result

opcodes = {}
def addOpCode(opcode, name, op, ip_offset):
    opcodes[opcode] = IntCode(name, op, ip_offset)

addOpCode(1, 'add', lambda memory, arguments: (arguments[2], memory[arguments[0]] + memory[arguments[1]]), 4)
addOpCode(2, 'mul', lambda memory, arguments: (arguments[2], memory[arguments[0]] * memory[arguments[1]]), 4)
# addOpCode(3, 'input', lambda memory, noun: memory[noun],2)
# addOpCode(4, 'output', lambda memory, noun: memory[noun],2)
addOpCode(98, 'seti', lambda memory, arguments: (arguments[1], arguments[0]), 3)
addOpCode(99, 'halt', lambda memory, arguments: (None, None), 1)

def execute(memory):
  memory = [int(i) for i in memory]
  instruction_pointer = 0
  while True:
    instruction_pointer = execute_instruction(memory, instruction_pointer)
    if memory[instruction_pointer] == 99:
      return memory

def execute_instruction(memory, instruction_pointer=0):
  opcode = memory[instruction_pointer]
  if opcode in opcodes.keys():
    curr_inst = opcodes[opcode]
    ip_offset = curr_inst.ip_offset
    arguments = memory[instruction_pointer +
                        1:instruction_pointer + ip_offset]
    # TODO slice the number of arguments
    curr_inst.run(memory, arguments)
    instruction_pointer += ip_offset
  else:
    sys.stderr.write("Error - IP opcode" + memory[instruction_pointer])
  return instruction_pointer
