from ship_computer import ShipComputer
from collections import deque
import sys

#TODO - refactor and tidy
input_file = 'day-23/input.txt'

def part1(memory):
  memory = memory.split(",")
  computers = [0] * 50

  queue = [deque() for _ in range(50)]

  for i in range(50):
    computers[i] = ShipComputer(memory, i)
    computers[i].execute_until_blocked()

  try:
    while True:
      for i in range(50):
        computers[i].execute_until_blocked()
        if queue[i]:
          inputs = []
          while queue[i]:
            inputs.append(queue[i].popleft())
          print('Computer',i,'receiving',inputs)
          for input in inputs:
            computers[i].put_input(input)
        else:
          computers[i].put_input(-1)
        if computers[i].output.qsize() >=3:
          print('Computer',i,'qsize',computers[i].output.qsize())
          outputs = computers[i].get_all_outputs()
          # TODO change outputs to SimpleQueue/FIFO
          while len(outputs) >= 3:
            address = outputs.pop(0)
            x = outputs.pop(0)
            y = outputs.pop(0)
            print('Computer',i,'sent',address,x,y)
            if address == 255:
              return y
            queue[address].append(x)
            queue[address].append(y)
  except StopIteration:
    return -1


def part2(memory):
  memory = memory.split(",")
  computers = [0] * 50

  nat = [None,None]
  prev_nat_y = None

  queue = [deque() for _ in range(50)]

  for i in range(50):
    computers[i] = ShipComputer(memory, i)
    computers[i].execute_until_blocked()

  try:
    while True:
      sent = 0
      for i in range(50):
        computers[i].execute_until_blocked()
        if queue[i]:
          sent +=1
          inputs = []
          while queue[i]:
            inputs.append(queue[i].popleft())
          print('Computer',i,'receiving',inputs)
          for input in inputs:
            computers[i].put_input(input)
        else:
          computers[i].put_input(-1)
        if computers[i].output.qsize() >=3:
          print('Computer',i,'qsize',computers[i].output.qsize())
          outputs = computers[i].get_all_outputs()
          # TODO change outputs to SimpleQueue/FIFO
          while len(outputs) >= 3:
            address = outputs.pop(0)
            x = outputs.pop(0)
            y = outputs.pop(0)
            print('Computer',i,'sent',address,x,y)
            if address == 255:
              nat = [x,y]
            else:
              queue[address].append(x)
              queue[address].append(y)
      if sent == 0 and nat[0] != None:
        if nat[1] == prev_nat_y:
          return nat[1]
        else:
          queue[0].append(nat[0])
          queue[0].append(nat[1])
          prev_nat_y = nat[1]
  except StopIteration:
    return -1

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  # print("Part 2: ", part2(data))
