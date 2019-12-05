import sys

class ShipComputer:

  def __init__(self, initial_memory, input = None):
    self.opcodes = {}
    self.memory = [int(i) for i in initial_memory]
    self.instruction_pointer = 0
    self.input = input
    self.output = []

    self.addOpCode(1, 'add', lambda memory, params: (params[2], memory[params[0]] + memory[params[1]]), 3)
    self.addOpCode(2, 'mul', lambda memory, params: (params[2], memory[params[0]] * memory[params[1]]), 3)
    self.addOpCode(3, 'input', lambda memory, params: (params[0], self.input), 1)
    self.addOpCode(4, 'output', lambda memory, params: (None, self.output.append(memory[params[0]])), 1)
    self.addOpCode(98, 'seti', lambda memory, params: (params[1], params[0]), 2)
    self.addOpCode(99, 'halt', lambda memory, params: (None, None), 0)

  def get_memory(self):
    return self.memory

  def get_output(self):
    return self.output

  def addOpCode(self, opcode, name, run_function, parmLength, ip_offset=None):
      self.opcodes[opcode] = self.createIntCode(name, run_function, parmLength, ip_offset)

  def execute(self):
    while self.memory[self.instruction_pointer] != 99:
      self.execute_instruction()
    return self.memory

  def execute_instruction(self):
    instruction = self.memory[self.instruction_pointer]
    opcode = instruction % 100
    param_modes = [(instruction // 100 ) % 10, (instruction // 1000 ) % 10, (instruction // 10000 ) % 10]
    if opcode in self.opcodes.keys():
      curr_inst = self.opcodes[opcode]
      parm_length = curr_inst.parameterLength
      parm_addresses = []
      for i in range(0, curr_inst.parameterLength):
        memory_address = self.instruction_pointer + 1 + i
        if param_modes[i] == 0: # position, not immediate, so dereference
          memory_address = self.memory[memory_address]
        parm_addresses.append(memory_address)

      #parameters = self.memory[self.instruction_pointer + 1:self.instruction_pointer + parm_length + 1]
      # TODO slice the number of arguments
      curr_inst.run(parm_addresses)
      self.instruction_pointer += curr_inst.ip_offset
    else:
      sys.stderr.write("Error - IP opcode" + self.memory[self.instruction_pointer])
    return self.instruction_pointer

  def createIntCode(self, name, run_function, parameterLength, ip_offset=None):
    return ShipComputer.IntCode(self, name, run_function, parameterLength, ip_offset=None)

  class IntCode:
    def __init__(self, outer, name, run_function, parameterLength, ip_offset=None):
      self.computer = outer
      self.name = name
      self.run_function = run_function
      self.parameterLength = parameterLength
      self.ip_offset = ip_offset if ip_offset != None else parameterLength + 1

    def run(self, params):
      output, result = self.run_function(self.computer.memory, params)
      if (output != None):
        self.computer.memory[output] = result
