import secure_container
import fileinput

def test_length_6_passes():
    check_length_6(123456, True)

def test_length_6_fails_5():
    check_length_6(12345, False)

def test_length_6_fails_7():
    check_length_6(1234567, False)

def check_length_6(input, expected):
    digits = [int(char) for char in str(input)]
    assert  secure_container.is_length_6(digits) == expected

def test_is_in_order_passes_1():
    check_is_in_order(123456, True)

def test_is_in_order_passes_2():
    check_is_in_order(111122, True)

def test_is_in_order_fails_1():
    check_is_in_order(12332, False)

def test_is_in_order_fails_2():
    check_is_in_order(54321, False)

def check_is_in_order(input, expected):
    digits = [int(char) for char in str(input)]
    assert  secure_container.is_in_order(digits) == expected

def test_has_repeats_passes_1():
    check_has_repeats(122223, True)

def test_has_repeats_passes_2():
    check_has_repeats(111122, True)

def test_has_repeats_passes_3():
    check_has_repeats(123432, True)

def test_has_repeats_fails_1():
    check_has_repeats(123456, False)

def check_has_repeats(input, expected):
    digits = [int(char) for char in str(input)]
    assert  secure_container.has_repeats(digits) == expected

def test_has_double_passes_1():
    check_has_double(123451, True)

def test_has_double_passes_2():
    check_has_double(111122, True)

def test_has_double_fails_1():
    check_has_double(111222, False)

def test_has_double_fails_2():
    check_has_double(123456, False)

def check_has_double(input, expected):
    digits = [int(char) for char in str(input)]
    assert secure_container.has_double(digits) == expected

def check_has_repeat(input, expected):
    assert secure_container.meets_criteria(input, secure_container.has_repeat_count) == expected

def test_part1():
    with open(secure_container.input_file) as f:
       data = f.read()
    expected = 1640 #910 too low
    assert secure_container.part1(data) == expected

def test_part2():
    with open(secure_container.input_file) as f:
       data = f.read()
    expected = 1126
    assert secure_container.part2(data) == expected
