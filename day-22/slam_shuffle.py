import sys

input_file = 'day-22/input.txt'

def part1(input, deck_size, result_position = None):
  deck = list(range(deck_size))

  instructions = input.splitlines()
  for instruction in instructions:
    if instruction == "deal into new stack":
      deck.reverse()
    elif instruction.startswith('cut '):
      cut = int(instruction.split()[1])
      deck = deck[cut:len(deck)] + deck[0:cut]
    elif instruction.startswith('deal with increment '):
      inc = int(instruction.split()[3])
      new_deck = deck[:]
      for i in range(deck_size):
        new_pos = (i * inc) % deck_size
        new_deck[new_pos] = deck[i]
      deck = new_deck

  if result_position != None:
    return deck.index(result_position)
  else:
    return deck

def inverse_mod(increment, deck_size):
  return pow(increment, deck_size-2, deck_size)

# See explaination in https://www.reddit.com/r/adventofcode/comments/ee0rqi/2019_day_22_solutions/fbnkaju/
def part2(input, deck_size, result_position, repeats):
  increment, offset = 1, 0

  instructions = input.splitlines()
  for instruction in instructions:
    if instruction == "deal into new stack":
      increment = (increment * -1) % deck_size
      offset = (offset + increment) % deck_size
    elif instruction.startswith('cut '):
      cut = int(instruction.split()[1])
      offset = (offset + (increment * cut)) % deck_size
    elif instruction.startswith('deal with increment '):
      inc = int(instruction.split()[3])
      increment = (increment * inverse_mod(inc, deck_size)) % deck_size

  repeated_increment = pow(increment, repeats, deck_size) # 3rd parm in power means mod by this
  repeated_offset = offset * (1 - pow(increment, repeats, deck_size)) * inverse_mod(1 - increment, deck_size)

  return (repeated_offset + repeated_increment * result_position) % deck_size

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))
