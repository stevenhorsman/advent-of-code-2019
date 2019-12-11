import sys
import itertools

input_file = 'day-08/input.txt'

def read_in_layers(input, width, height):
  input = [int(c) for c in input.rstrip()]
  image_size = width * height
  no_layers = len(input) // image_size
  layers = []

  for l in range(0, no_layers):
    layerlines = []
    for h in range(0,height):
      lower_bound = (l * image_size) + (h * width)
      upper_bound = (l * image_size) + ((h + 1) * width)
      layerlines.append(input[lower_bound:upper_bound])

    layers.append(layerlines)
  return layers

def part1(input, width, height):
  layers = read_in_layers(input, width, height)

  flattened_layers = [list(itertools.chain(*layer)) for layer in layers]
  
  # From https://github.com/GlenboLake/aoc2019/blob/master/day08.py, key decides how to compare the item
  min_zeros_layer = min(flattened_layers, key=lambda layer: layer.count(0))
  
  return min_zeros_layer.count(1) *  min_zeros_layer.count(2)

def chunks(xs, size):
    return [xs[i:i + size] for i in range(0, len(xs), size)]

def part2(input, width, height):
  layers = read_in_layers(input, width, height)
  
  # something in pixels = list(zip(**layers))?

  # From https://github.com/frerich/aoc2019/blob/master/python/day8/day8.py
  # merged = (next(n for n in stack if n != '2') for stack in zip(*layers))
  # rendered = ''.join(' ' if n == '0' else '#' for n in merged)
  output = ""
  for h in range(0,height):
    line = []
    for w in range(0,width):
      for l in range(0, len(layers)):
        if layers[l][h][w] != 2:
          output += '.' if layers[l][h][w] == 0 else "#"
          break
    output += '\n'
  return output
    
if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data, 25, 6))
  print("Part 2: ", part2(data, 25, 6))
