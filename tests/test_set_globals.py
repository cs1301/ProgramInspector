import Program
import os

with open("./test_programs/{}".format(os.path.basename(__file__))) as _test_file_contents:
    _test_file = Program.Program(_test_file_contents.read(), globals_dict={"mysteryValue": "Taylor Swift"})


def basic_tests():
    assert _test_file.output.getvalue() == "Taylor Swift\n"

    _test_file.set_globals({"seeded_global_function_1": seeded_global_function_1})
    assert _test_file.call(seeded_global_function_1) == 5

    _test_file.set_globals({"seeded_global_function_name": seeded_global_function_2})
    assert _test_file.call(_test_file.globals.seeded_global_function_name) == 10


def seeded_global_function_1():
    return 5


def seeded_global_function_2():
    return 10

