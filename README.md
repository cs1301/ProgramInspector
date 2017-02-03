# ProgramInspector

A Python module to enable autograders to better assess student programs.

## Program(plaintext_code[, timeout=5, input_strings=None])

Creates a Program object for the given program. 

`plaintext_code`: a string of python code

`timeout`: when running code, the amount of time that should be given before throwing an exception (for infinite loops)

`input_strings`: values to be entered as input (do not include newlines)

Ex:

```
import ProgramInspector as PI
program = PI.Program("print('hello')", timeout=10, input_strings=['input', 'items'])
```

#### Program.globals
A module containing the compiled program.

#### Program.global_classes
A dictionary of global classes in the program

#### Program.global_functions
A dictionary of global functions in the program

#### Program.global_variables
A dictionary of global variables in the program
 
#### Program.input
Input stream for Program.call
 
#### Program.output
Output stream for Program.call
 
#### Program.plaintext_code
The program in plaintext as it was instantiated

## Program.call(function[, \*args, \*\*kwargs])

Calls a function using staged input and timing out to avoid infinite loops. All output will be redirected to Program.output.

`function`: the function to call

`*args`: (optional) positional arguments for function call

`**kwargs`: (optional) keyword arguments for function call

Ex:

```
program_string = """
def test_function(val):
    print(val)
"""

import ProgramInspector as PI
program = PI.Program(program_string)
program.call(program.globals.test_function, "Taylor Swift")
print(program.output.getvalue())
```
Output:
```
Taylor Swift
```

## Program.count_for_loops([target])

Returns the number of for loops in the program. Does not include list comprehensions. 

`target`: (optional) a function or a class may be passed in to analyze a specific region of code

Ex:
```
program_string = """
def example():
    for x in range(10):
        print(x)

    while x in [x for x in [1, 2, 3]]:
        pass
"""

import ProgramInspector as PI
program = PI.Program(program_string)
program.count_for_loops(program.globals.example)
print(program.output.getvalue())
```
Output:
```
1
```
## Program.count_if_statements([target])

Returns the number of if statementss in the program. Does not include if expressions. 

`target`: (optional) a function or a class may be passed in to analyze a specific region of code

Ex:
```
program_string = """
def example(a):
    if a == 5:
        pass
    elif a == 4:
        pass
    else:
        pass
        
    if True:
        pass
        
    a = 1 if True else 2
"""

import ProgramInspector as PI
program = PI.Program(program_string)
program.count_if_statements(program.globals.example)
print(program.output.getvalue())
```
Output:
```
2
```

## Program.count_if_expressions([target])

Returns the number of if expressions in the program. 

`target`: (optional) a function or a class may be passed in to analyze a specific region of code

Ex:
```
program_string = """
def example(a):
    if a == 5:
        pass
    elif a == 4:
        pass
    else:
        pass
        
    if True:
        pass
        
    a = 1 if True else 2
"""

import ProgramInspector as PI
program = PI.Program(program_string)
program.count_if_expressions(program.globals.example)
print(program.output.getvalue())
```
Output:
```
1
```

## Program.count_list_comprehensions([target])

Returns the number of list comprehensions in the program. 

`target`: (optional) a function or a class may be passed in to analyze a specific region of code

Ex:
```
program_string = """
def example():
    for x in range(10):
        print(x)

    while x in [x for x in [1, 2, 3]]:
        pass
"""

import ProgramInspector as PI
program = PI.Program(program_string)
program.count_list_comprehensions(program.globals.example)
print(program.output.getvalue())
```
Output:
```
1
```

## Program.count_recursive_calls(function[, \*args, \*\*kwargs])

Runs the given function with the given args and/or keywords as arguments and returns the number of recursive calls made. Note that this number does not include the initial call. 

`function`: the function to analyze. Note that the function will be called

`*args`: (optional) positional arguments for function call

`**kwargs`: (optional) keyword arguments for function call

Ex:
```
program_string = """
def example(val):
    if val > 0:
        example(val - a)
"""

import ProgramInspector as PI
program = PI.Program(program_string)
program.count_recursive_calls(program.globals.example, 5)
print(program.output.getvalue())
```

Output:
```
5
```

## Program.count_while_loops([target])

Returns the number of while loops in the program. 

`target`: (optional) a function or a class may be passed in to analyze a specific region of code

Ex:
```
program_string = """
def example():
    for x in range(10):
        print(x)

    while x in [x for x in [1, 2, 3]]:
        pass
"""

import ProgramInspector as PI
program = PI.Program(program_string)
program.count_while_loops(program.globals.example)
print(program.output.getvalue())
```
Output:
```
1
```

## Program.prep_input(input_strings)

Stages input for Program.call. Note that input items can also be staged in the Program constructor.

`input_items`: a list of values that should be entered as input (do not include newlines)

Ex:

```
program_string = """
def test_function():
    print(input())
"""

import ProgramInspector as PI
program = PI.Program(program_string)
program.prep_input(["hi"])
program.call(program.globals.test_function)
print(program.output.getvalue())
```

output:
```
hi
```
