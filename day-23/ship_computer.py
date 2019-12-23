import sys
from queue import SimpleQueue, LifoQueue
from enum import Enum
class Status(Enum):
  IDLE = 0
  RUNNING = 1
  FINISHED = 2
  WAITING_FOR_INPUT = 3

class ShipComputer:

  def __init__(self, initial_memory, inputs = None):
    self.opcodes = {}
    self.memory = [int(i) for i in initial_memory]
    self.instruction_pointer = 0
    if (isinstance(inputs, int)):
      inputs = [inputs]
    self.inputs = SimpleQueue()
    if inputs != None:
      self.label = inputs[0]
      for input in inputs:
        self.inputs.put(input)
    self.output = LifoQueue()
    self.relative_base = 0
    self.status = Status.IDLE

    self.addOpCode(1, 'add', lambda memory, params: (params[2], memory[params[0]] + memory[params[1]], None), 3)
    self.addOpCode(2, 'mul', lambda memory, params: (params[2], memory[params[0]] * memory[params[1]], None), 3)
    self.addOpCode(3, 'input', self.get_input, 1) # SimpleQueue.get blocks
    self.addOpCode(4, 'output', self.put_output, 1)
    self.addOpCode(5, 'jump-if-true', lambda memory, params: (None, None, None if memory[params[0]] == 0 else memory[params[1]]), 2, 0)
    self.addOpCode(6, 'jump-if-false', lambda memory, params: (None, None, None if memory[params[0]] != 0 else memory[params[1]]), 2, 0)
    self.addOpCode(7, 'less-than', lambda memory, params: (params[2], 1 if memory[params[0]] < memory[params[1]] else 0, None), 3)
    self.addOpCode(8, 'equals', lambda memory, params: (params[2], 1 if memory[params[0]] == memory[params[1]] else 0, None), 3)
    self.addOpCode(9, 'rel_base', self.update_rel_base, 1)
    self.addOpCode(98, 'seti', lambda memory, params: (params[1], params[0], None), 2)
    self.addOpCode(99, 'halt', lambda memory, params: (None, None, None), 0)

  def update_rel_base(self, memory, params):
    self.relative_base += memory[params[0]]
    return (None, None, None)

  def get_memory(self):
    return self.memory

  def get_input(self, memory, params):
    if self.inputs.qsize() == 0:
      self.status = Status.WAITING_FOR_INPUT
      return (None, None, self.instruction_pointer)
    input = self.inputs.get() # SimpleQueue.get blocks
    self.status = Status.RUNNING
    return  (params[0], input, None)

  def put_output(self, memory, params):
    return (None, self.output.put(memory[params[0]]), None)

  def get_output(self):
    return self.output.get()

  def get_all_outputs(self):
    outputs = []
    while (not self.output.empty()):
      outputs.append(self.get_output())
    outputs.reverse() # LIFO -> FIFO queue
    return outputs

  def put_input(self, value):
    return self.inputs.put(value)

  def addOpCode(self, opcode, name, run_function, parmLength, ip_offset=None):
      self.opcodes[opcode] = self.createIntCode(name, run_function, parmLength, ip_offset)

  def execute_until_blocked(self):
    while self.tick():
      pass

  def tick(self):
    self.status = Status.RUNNING
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
        if param_modes[i] == 2: # relative
          memory_address = self.relative_base + self.memory[memory_address]
        parm_addresses.append(memory_address)
      curr_inst.run(parm_addresses)
      if opcode == 99: # halt
        self.status = Status.FINISHED
        return False
    else:
      sys.stderr.write("Error - IP opcode" + str(opcode))
    return self.status == Status.RUNNING

  def execute(self):
    try:
      while True:
        next(self.execute_concurrent())
    except StopIteration:
      return

  def execute_concurrent(self, concurrent_mode = False):
    while True:
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
          if param_modes[i] == 2: # relative
            memory_address = self.relative_base + self.memory[memory_address]
          parm_addresses.append(memory_address)
        curr_inst.run(parm_addresses)
        if opcode == 99: # halt
          return False
        if opcode == 4 and concurrent_mode: #output
          yield self.get_output()
      else:
        sys.stderr.write("Error - IP opcode" + str(opcode))

  def createIntCode(self, name, run_function, parameterLength, ip_offset=None):
    return ShipComputer.IntCode(self, name, run_function, parameterLength, ip_offset)

  class IntCode:
    def __init__(self, outer, name, run_function, parameterLength, ip_offset=None):
      self.computer = outer
      self.name = name
      self.run_function = run_function
      self.parameterLength = parameterLength
      self.ip_offset = ip_offset if ip_offset != None else parameterLength + 1

    def run(self, params):
      for address in params[:-1]:
        if address >= len(self.computer.memory):
          self.computer.memory += [0] * (10 + address - len(self.computer.memory))
      output, result, new_ip = self.run_function(self.computer.memory, params)
      if (output != None):
        if output >= len(self.computer.memory):
          self.computer.memory += [0] * (10 + output - len(self.computer.memory))
        self.computer.memory[output] = result
      if (new_ip != None):
        self.computer.instruction_pointer = new_ip
      else:
        self.computer.instruction_pointer += self.parameterLength + 1