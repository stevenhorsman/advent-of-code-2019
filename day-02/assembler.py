import sys

class IntCode:
    def __init__(self, name, runFunction):
        self.name = name
        self.runFunction = runFunction

    def run(self, memory, input1, input2, output):
       result = self.runFunction(memory, input1, input2)
    #    print(self.name, memory[input1], memory[input2], "=", result)
       memory[output] = result

opcodes = {}
def addOpCode(opcode, name, op):  
    opcodes[opcode] = IntCode(name, op)

addOpCode(1, 'add', lambda memory, noun, verb: memory[noun] + memory[verb])
addOpCode(2, 'mul', lambda memory, noun, verb: memory[noun] * memory[verb])
addOpCode(99, 'halt', lambda memory, noun, verb: None)

def execute(inputs):
    inputs = [int(i) for i in inputs]
    instruction_pointer = 0
    while True:
        execute_instruction(inputs, instruction_pointer)
        instruction_pointer += 4
        if inputs[instruction_pointer] == 99:
            return inputs

def execute_instruction(inputs, instruction_pointer = 0):
    opcode = inputs[instruction_pointer]
    if opcode in opcodes.keys(): 
        curr_inst = opcodes[opcode]
        a, b, c = inputs[instruction_pointer + 1], inputs[instruction_pointer + 2], inputs[instruction_pointer + 3]
        curr_inst.run(inputs,a,b,c)
    else: 
        sys.stderr.write("Error - IP opcode" + inputs[instruction_pointer])
    return inputs