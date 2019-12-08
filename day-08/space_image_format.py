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

def part2(input, width, height):
  image_size = width * height
  no_layers = len(input) // image_size
  layers = []

  for l in range(0, no_layers):
    lower_bound = l * image_size
    upper_bound = (l+1)*image_size
    layers.append(input[lower_bound:upper_bound])
  
  image = []
  for h in range(0,height):
    line = []
    for w in range(0,width):
      pixel = ' '
      for l in range(0, no_layers):
        if layers[l][(h*width) + w] != '2':
          pixel = layers[l][(h*width) + w]
          break
      line.append(pixel)
    image.append(line)

  output = ""  
  for line in image:
    output += "".join(line) + "\n"

  return output
    
if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data, 25, 6))
  print("Part 2: ", part2(data, 25, 6))
