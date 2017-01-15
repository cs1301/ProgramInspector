import traceback
import os

tests = [filename[:-3] for filename in os.listdir(os.path.dirname(__file__))
         if filename.endswith(".py") and filename not in ["run_tests.py"]]

for test_file_name in tests:
    print("\033[94m{}:\033[0m".format(test_file_name))
    exec("import {}".format(test_file_name))
    for test_case in [x for x in dir(eval(test_file_name)) if x.endswith("_tests") or x.endswith("_test")]:
        try:
            eval("{}.{}()".format(test_file_name, test_case))
            print("\033[92m\t{}: OK\033[0m".format(test_case))
        except Exception as err:
            print("\033[91m\t{}: ERROR\033[0m".format(test_case))
            print("\t\t" + traceback.format_exc().replace("\n", "\n\t\t"))
