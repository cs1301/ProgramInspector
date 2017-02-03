print(input())

def global_func_1():
    print("test_func_1")

    def not_global_func():
        print("not global")

global_var_1 = 9999
global_func_var_1 = global_func_1

print("expected output")


def global_print_value(value):
    print(value)


def global_input_test():
    return input()
