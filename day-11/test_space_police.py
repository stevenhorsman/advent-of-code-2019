import space_police
import fileinput

def test_part1():
  with open(space_police.input_file) as f:
    data = f.read()
  expected = 1785
  assert space_police.part1(data) == expected

def test_part2():
  with open(space_police.input_file) as f:
    data = f.read()
  expected = """
 #  #   ##  ##  #      ## #### #### #  #   
 #  #    # #  # #       #    # #    #  #   
 ####    # #  # #       #   #  ###  ####   
 #  #    # #### #       #  #   #    #  #   
 #  # #  # #  # #    #  # #    #    #  #   
 #  #  ##  #  # ####  ##  #### #    #  #   
"""[1:]
  assert space_police.part2(data) == expected
