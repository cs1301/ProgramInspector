import Program
import os

with open("./test_programs/{}".format(os.path.basename(__file__))) as _test_file_contents:
    _test_file = Program.Program(_test_file_contents.read())


def basic_tests():
    assert _test_file.count_while_loops(_test_file.globals.basic_program) == 1
    assert _test_file.count_while_loops(_test_file.globals.optimized_case) == 0
    assert _test_file.count_while_loops(_test_file.globals.nested_cases) == 5


def mixed_loop_test():
    assert _test_file.count_while_loops(_test_file.globals.mixed_loops) == 3


def file_test():
    assert _test_file.count_while_loops() == 10
