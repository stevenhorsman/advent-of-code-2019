import sys

input_file = 'day-08/input.txt'

def part1(input, width, height):
  image_size = width * height
  no_layers = len(input) // image_size
  layers = []

  for l in range(0, no_layers):
    lower_bound = l * image_size
    upper_bound = (l+1)*image_size
    layers.append(input[lower_bound:upper_bound])

  zero_count = [layer.count('0') for layer in layers]
  min_layer = zero_count.index(min(zero_count))
  
  
  return layers[min_layer].count('1') *  layers[min_layer].count('2')

def part2(input):
  return 0

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))
