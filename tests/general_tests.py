import Program
import os
import types

with open("./test_programs/{}".format(os.path.basename(__file__))) as _test_file_contents:
    _test_file = Program.Program(_test_file_contents.read(), input_strings=["hello"])


def globals_tests():
    assert "global_func_1" in _test_file.global_functions.keys()
    for name, function in _test_file.global_functions.items():
        assert "global" in name
        assert isinstance(function, types.FunctionType)

    assert "global_func_var_1" not in _test_file.global_functions.keys()
    assert "global_func_var_1" in _test_file.global_variables.keys()
    assert isinstance(_test_file.global_variables["global_func_var_1"], types.FunctionType)

    assert "global_var_1" in _test_file.global_variables.keys()
    assert _test_file.global_variables["global_var_1"] == 9999


def output_test():
    assert _test_file.out.getvalue() == "hello\nexpected output\n"
    _test_file.call(_test_file.globals.global_print_value, "hi")
    _test_file.call(_test_file.globals.global_print_value, "hey")
    assert _test_file.out.getvalue() == "hello\nexpected output\nhi\nhey\n"


def input_tests():
    _test_file.prep_input(["5"])
    assert "5" == _test_file.call(_test_file.globals.global_input_test)

    _test_file.prep_input(["1", "2"])
    assert "1" == _test_file.call(_test_file.globals.global_input_test)
    assert "2" == _test_file.call(_test_file.globals.global_input_test)
