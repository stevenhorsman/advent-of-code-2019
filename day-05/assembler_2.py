import sys

class IntCode:
    def __init__(self, name, runFunction, ip_offset):
        self.name = name
        self.runFunction = runFunction
        self.ip_offset = ip_offset

    def run(self, memory, input1, input2, output):
       result = self.runFunction(memory, input1, input2)
    #    print(self.name, memory[input1], memory[input2], "=", result)
       memory[output] = result

opcodes = {}
def addOpCode(opcode, name, op, ip_offset):  
    opcodes[opcode] = IntCode(name, op, ip_offset)

addOpCode(1, 'add', lambda memory, noun, verb: memory[noun] + memory[verb],4)
addOpCode(2, 'mul', lambda memory, noun, verb: memory[noun] * memory[verb],4)
# addOpCode(3, 'input', lambda memory, noun: memory[noun],2)
# addOpCode(4, 'output', lambda memory, noun: memory[noun],2)
addOpCode(99, 'halt', lambda memory, noun, verb: None,1)

def execute(inputs):
    inputs = [int(i) for i in inputs]
    instruction_pointer = 0
    while True:
        instruction_pointer = execute_instruction(inputs, instruction_pointer)
        if inputs[instruction_pointer] == 99:
            return inputs

def execute_instruction(inputs, instruction_pointer = 0):
    opcode = inputs[instruction_pointer]
    if opcode in opcodes.keys(): 
        curr_inst = opcodes[opcode]
        a, b, c = inputs[instruction_pointer + 1], inputs[instruction_pointer + 2], inputs[instruction_pointer + 3]
        curr_inst.run(inputs,a,b,c)
        instruction_pointer += curr_inst.ip_offset
    else: 
        sys.stderr.write("Error - IP opcode" + inputs[instruction_pointer])
    return instruction_pointer