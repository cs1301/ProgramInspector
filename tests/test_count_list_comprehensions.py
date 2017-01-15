import Program
import os

with open("./test_programs/{}".format(os.path.basename(__file__))) as _test_file_contents:
    _test_file = Program.Program(_test_file_contents.read())


def basic_tests():
    assert _test_file.count_list_comprehensions(_test_file.globals.basic_program) == 1


def file_test():
    assert _test_file.count_list_comprehensions() == 1
