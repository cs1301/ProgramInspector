import Program
import os

with open("./test_programs/{}".format(os.path.basename(__file__))) as _test_file_contents:
    _test_file = Program.Program(_test_file_contents.read(), timeout=1)


def basic_tests():
    for i in range(-2, 10):
        assert _test_file.count_recursive_calls(_test_file.globals.basic_program, i) == max(i, 0)
        assert _test_file.count_recursive_calls(_test_file.globals.renamed_recursive_call, i) == max(i, 0)
        assert _test_file.count_recursive_calls(_test_file.globals.nested_recursive_call, i) == max(i, 0)
        assert _test_file.count_recursive_calls(_test_file.globals.looping_recursion, i) == max(
            sum([3 ** x for x in range(1, i + 1)]), i)


def arg_tests():
    for i in range(-2, 6):
        assert _test_file.count_recursive_calls(_test_file.globals.kwarg_function, i) == max(i, 0)

    for i in range(-2, 100):
        assert _test_file.count_recursive_calls(_test_file.globals.var_arg_test, *list(range(i))) == max(i, 0)

    assert _test_file.count_recursive_calls(_test_file.globals.large_arg_test, 10 ** 100 + 5) == 5


def variable_tests():
    assert _test_file.count_recursive_calls(_test_file.globals.many_constants, 5) == 5
    assert _test_file.count_recursive_calls(_test_file.globals.many_globals, 5) == 5


def error_tests():
    assert _test_file.count_recursive_calls(_test_file.globals.unending_recursion) == -1
    assert _test_file.count_recursive_calls(_test_file.globals.timeout_test) == -1
