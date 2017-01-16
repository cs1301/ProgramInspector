# ProgramInspector

A Python module to enable autograders to better assess student programs.

#### Program(plaintext_code[, timeout=5, input_strings=None])

Creates a Program object for the given program. 

`plaintext_code`: a string of python code

`timeout`: when running code, the amount of time that should be given before throwing an exception (for infinite loops)

`input_strings`: values to be entered as input (do not include newlines)



#### Program.call(function[, \*args, \*\*kwargs])

#### Program.count_recursive_calls(function[, \*args, \*\*kwargs])

#### Program.count_for_loops([target])

#### Program.count_while_loops([target])

#### Program.count_list_comprehensions([target])

#### Program.prep_input(input_strings)

Stages input for Program.call. Each item in input_strings should be a string. Note that input items can also be staged in the Program constructor.

```
program_string = """
def test_function():
    print(input())
"""

program = Program(program_string)
program.prep_input(["hi"])
program.call(test_function)
print(program.out.getvalue())
```

output:
```
hi
```

