import Program
import os

with open("./test_programs/{}".format(os.path.basename(__file__))) as _test_file_contents:
    _test_file = Program.Program(_test_file_contents.read())


def basic_tests():
    assert _test_file.count_if_statements() == 8
    assert _test_file.count_if_expressions() == 1
