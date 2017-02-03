import Program
import os


def global_test():
    try:
        with open("./test_programs/{}".format(os.path.basename(__file__))) as _test_file_contents:
            _test_file = Program.Program(_test_file_contents.read(), timeout=1)
    except TimeoutError:
        return
    assert False
