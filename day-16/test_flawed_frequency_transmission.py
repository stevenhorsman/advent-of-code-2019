import flawed_frequency_transmission
import fileinput

def test_part1_example_1():
  data = "12345678"
  assert flawed_frequency_transmission.part1(data,1) == "48226158"
  assert flawed_frequency_transmission.part1(data,2) == "34040438"
  assert flawed_frequency_transmission.part1(data,3) == "03415518"
  assert flawed_frequency_transmission.part1(data,4) == "01029498"

def test_part1_example_2():
  data = "80871224585914546619083218645595"
  assert flawed_frequency_transmission.part1(data) == "24176176"

def test_part1_example_3():
  data = "19617804207202209144916044189917"
  assert flawed_frequency_transmission.part1(data) == "73745418"

def test_part1_example_4():
  data = "69317163492948606335995924319873"
  assert flawed_frequency_transmission.part1(data) == "52432133"

def test_part1():
  with open(flawed_frequency_transmission.input_file) as f:
    data = f.read()
  expected = "19239468"
  assert flawed_frequency_transmission.part1(data) == expected

def test_part2_example_1():
  data = "03036732577212944063491565474664"
  assert flawed_frequency_transmission.part2(data) == "84462026"

def test_part2_example_2():
  data = "02935109699940807407585447034323"
  assert flawed_frequency_transmission.part2(data) == "78725270"

def test_part2_example_3():
  data = "03081770884921959731165446850517"
  assert flawed_frequency_transmission.part2(data) == "53553731"

def test_part2():
  with open(flawed_frequency_transmission.input_file) as f:
    data = f.read()
  expected = '96966221'
  assert flawed_frequency_transmission.part2(data) == expected
