import sys

def part1(inputs):
    inputs = inputs.split(",")
    inputs[1]="12"
    inputs[2]="2"
    result = execute(inputs)
    return result[0]

def execute(inputs):
    inputs = [int(i) for i in inputs] 
    program_counter = 0
    while True:
        execute_instruction(inputs, program_counter)
        program_counter += 4
        if inputs[program_counter] == 99:
            return inputs

def execute_instruction(inputs, program_counter = 0):
    if (inputs[program_counter] == 1):
        a = inputs[program_counter+1]
        b = inputs[program_counter+2]
        c = inputs[program_counter+3]
        inputs[c] = inputs[a] + inputs[b]
    elif (inputs[program_counter] == 2):
        a = inputs[program_counter + 1]
        b = inputs[program_counter + 2]
        c = inputs[program_counter + 3]
        inputs[c] = inputs[a] * inputs[b]
    elif (inputs[program_counter] == 99):
        pass
    else:
        sys.stderr.write("Error - pc code" + inputs[program_counter])
    return inputs


def part2(input):
    return input
