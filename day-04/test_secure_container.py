import secure_container
import fileinput

def test_rule_example_1():
    data = 111111
    assert secure_container.meets_critera(data) == True

def test_rule_example_2():
    data = 223450
    assert secure_container.meets_critera(data) == False

def test_rule_example_3():
    data = 123789
    assert secure_container.meets_critera(data) == False

def test_rule_example_4():
    data = 200000
    assert secure_container.meets_critera(data) == False

def test_part1():
    with open(secure_container.input_file) as f:
       data = f.read()
    expected = 1640 #910 too low
    assert secure_container.part1(data) == expected

def test_part2_rule_example_1():
    data = 112233
    assert secure_container.meets_critera2(data) == True

def test_part2_rule_example_2():
    data = 123444
    assert secure_container.meets_critera2(data) == False

def test_part2_rule_example_3():
    data = 111122
    assert secure_container.meets_critera2(data) == True

def test_part2_rule_example_4():
    data = 200000
    assert secure_container.meets_critera2(data) == False

def test_part2():
    with open(secure_container.input_file) as f:
       data = f.read()
    expected = 1126
    assert secure_container.part2(data) == expected
