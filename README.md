# ProgramInspector

A Python module to enable autograders to better assess student programs.

## Program(plaintext_code[, timeout=5, input_strings=None])

Creates a Program object for the given program. 

`plaintext_code`: a string of python code

`timeout`: when running code, the amount of time that should be given before throwing an exception (for infinite loops)

`input_strings`: values to be entered as input (do not include newlines)

Ex:

```
program = Program("print('hello')", timeout=10, input_strings=['input', 'items'])
```

## Program.call(function[, \*args, \*\*kwargs])

Calls a function using staged input and timing out to avoid infinite loops. All output will be redirected to Program.out.

`function`: the function to call

`*args`: (optional) positional arguments for function call

`**kwargs`: (optional) keyword arguments for function call

Ex:

```
program_string = """
def test_function():
    print("Taylor Swift")
"""

program = Program(program_string)
program.call(program.globals.test_function)
print(program.out.getvalue())
```
Output:
```
Taylor Swift
```

## Program.count_for_loops([target])

Returns the number of for loops in the program. 

`target`: (optional) a function or a class may be passed in to analyze a specific region of code

## Program.count_list_comprehensions([target])

Returns the number of list comprehensions in the program. 

`target`: (optional) a function or a class may be passed in to analyze a specific region of code

## Program.count_recursive_calls(function[, \*args, \*\*kwargs])

Runs the given function with the given args and/or keywords as arguments and returns the number of recursive calls made. Note that this number does not include the initial call. 

`function`: the function to analyse. Note that the function will be called

`*args`: (optional) positional arguments for function call

`**kwargs`: (optional) keyword arguments for function call

## Program.count_while_loops([target])

Returns the number of while loops in the program. 

`target`: (optional) a function or a class may be passed in to analyze a specific region of code

## Program.prep_input(input_strings)

Stages input for Program.call. Note that input items can also be staged in the Program constructor.

`input_items`: a list of values that should be entered as input (do not include newlines)

Ex:

```
program_string = """
def test_function():
    print(input())
"""

program = Program(program_string)
program.prep_input(["hi"])
program.call(program.globals.test_function)
print(program.out.getvalue())
```

output:
```
hi
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

 

