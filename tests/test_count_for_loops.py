import Program
import os

with open("./test_programs/{}".format(os.path.basename(__file__))) as _test_file_contents:
    _test_file = Program.Program(_test_file_contents.read())


def basic_tests():
    assert _test_file.count_for_loops(_test_file.globals.basic_program) == 1
    assert _test_file.count_for_loops(_test_file.globals.zero_case) == 0


def complex_tests():
    assert _test_file.count_for_loops(_test_file.globals.complex_1) == 4


def file_test():
    assert _test_file.count_for_loops() == 6
