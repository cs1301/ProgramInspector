import imp
from types import CodeType, FunctionType
import dis
import copy
import types
import signal
import io
import sys
import ast
import inspect


class Program:
    def __init__(self, plaintext_code, timeout=5, input_strings=None):
        self.TIMEOUT = timeout

        self.output = io.StringIO()
        self.input = None
        self.prep_input(input_strings or [])

        old_stdout = sys.stdout
        old_stderr = sys.stderr
        old_in = sys.stdin

        sys.stdout = self.output
        sys.stderr = self.output
        sys.stdin = self.input

        self.plaintext_code = plaintext_code
        self.globals = imp.new_module("StudentCodeGlobals")
        try:
            exec(self.plaintext_code, self.globals.__dict__)
        finally:
            sys.stdout = old_stdout
            sys.stderr = old_stderr
            sys.stdin = old_in

        self.global_functions = {}
        self.global_classes = {}
        self.global_variables = {}
        self.compiled_code = compile(self.plaintext_code, "compiled_code", "exec")
        for const in self.compiled_code.co_consts:
            if isinstance(const, CodeType) and const.co_name in self.globals.__dict__.keys():
                global_object = self.globals.__dict__[const.co_name]
                if inspect.isfunction(global_object):
                    self.global_functions[global_object.__code__.co_name] = global_object
                elif inspect.isclass(global_object):
                    self.global_classes[global_object.__code__.co_name] = global_object
        for variable in self.compiled_code.co_names:
            if variable not in self.global_functions.keys() \
                    and variable not in self.global_classes.keys() \
                    and variable in self.globals.__dict__.keys():
                self.global_variables[variable] = self.globals.__dict__[variable]

        self.code_objects = self._collect_code()
        self.ast = ast.parse(self.plaintext_code)

    def count_while_loops(self, target=None, ignore_optimized=False):
        """
        :param target: (optional) Specific target to search.
        :param ignore_optimized: Will not count pointless while loops if enabled.
        :return: Number of while loops in search target.

        notes:
        SETUP_LOOP only occurs once per for loop and while loop
        SETUP_LOOP does not occur in list comprehensions
        """

        if ignore_optimized:
            target_code = None if target is None else self._collect_code(target.__code__)
            total_loops = self._count_op_occurrences(dis.opmap["SETUP_LOOP"], code=target_code)
            total_for_loops = self.count_for_loops(target=target)
            return total_loops - total_for_loops
        else:
            return self._count_ast_occurrences(ast.While, target=self._search_ast(target) if target else None)

    def count_for_loops(self, target=None):
        """
        :param target: (optional) Specific target to search.
        :return: Number of for loops in search target.
        """

        return self._count_ast_occurrences(ast.For, target=self._search_ast(target) if target else None)

    def count_list_comprehensions(self, target=None):
        """
        :param target: (optional) Specific target to search.
        :return: Number of list comprehensions in search target.

        notes:
        A list comprehension looks like:
        [100, const_index_1, 0]: LOAD_CONST '*<listcomp>*'
        [100, const_index_2, 0]: LOAD_CONST '*<listcomp>'
        """

        return self._count_ast_occurrences(ast.ListComp, target=self._search_ast(target) if target else None)

    def count_recursive_calls(self, function, *args, **kwargs):
        """
        Runs a given function and determines the number of recursive calls made.

        :param function: function to call
        :param args: positional arguments to pass to given function
        :param kwargs: keyword arguments to pass to given function
        :return: number of times function was called excluding initial call
        """

        # create the callee
        edited_globals = copy.deepcopy(self.globals.__dict__)
        inc_count_program = "def __inc_count__():\n\tglobal __count__\n\t__count__ += 1"
        inc_count_program_code = compile(inc_count_program, "__inc_count__", "exec")
        __inc_count__ = FunctionType(inc_count_program_code, edited_globals)
        edited_globals["__inc_count__"] = __inc_count__
        edited_globals["__count__"] = 0

        # create caller bytecode
        orig_code = function.__code__
        inc_code = bytes([dis.opmap["LOAD_GLOBAL"], len(orig_code.co_names), 0,
                          dis.opmap["CALL_FUNCTION"], 0, 0,
                          dis.opmap["POP_TOP"]])

        # update absolute jump targets
        edited_bytecode = list(orig_code.co_code)
        for instruction in dis.get_instructions(orig_code):
            if instruction.opcode in dis.hasjabs:
                edited_bytecode[instruction.offset + 1] += len(inc_code)
        edited_bytecode = bytes(edited_bytecode)

        # inject function call
        edited_code = CodeType(orig_code.co_argcount, orig_code.co_kwonlyargcount, orig_code.co_nlocals,
                               orig_code.co_stacksize, orig_code.co_flags, inc_code + edited_bytecode,
                               orig_code.co_consts, orig_code.co_names + ("__inc_count__",), orig_code.co_varnames,
                               orig_code.co_filename, "modified_" + orig_code.co_name, orig_code.co_firstlineno - 1,
                               orig_code.co_lnotab, orig_code.co_freevars, orig_code.co_cellvars)
        function_copy = types.FunctionType(edited_code, edited_globals)
        edited_globals[function.__code__.co_name] = function_copy

        # run modified function
        try:
            self.call(function_copy, *args, **kwargs)
        except (RuntimeError, TimeoutError):
            return -1
        return edited_globals["__count__"]

    def prep_input(self, input_strings):
        """
        Clears current input stream and preps input with given values.

        :param input_strings: a list of string values to be handed to input()
        :return: None
        """

        self.input = io.StringIO()
        for input_item in input_strings:
            self.input.write(str(input_item))
            self.input.write("\n")
        self.input.seek(0)

    def call(self, function, *args, **kwargs):
        """
        Calls a given function with proper handling of input, output and timeouts.

        :param function: function ot call
        :param args: positional arguments
        :param kwargs: keyword arguments
        :return: return value of function
        """

        old_stdout = sys.stdout
        old_stderr = sys.stderr
        old_in = sys.stdin

        sys.stdout = self.output
        sys.stderr = self.output
        sys.stdin = self.input

        def handler(signum, frame):
            raise TimeoutError("Function timeout: {}s".format(self.TIMEOUT))

        signal.signal(signal.SIGALRM, handler)
        signal.alarm(self.TIMEOUT)

        try:
            return function(*args, **kwargs)
        finally:
            signal.alarm(0)
            sys.stdout = old_stdout
            sys.stderr = old_stderr
            sys.stdin = old_in

    def _count_op_occurrences(self, opcode, code=None):
        """
        :param opcode: opcode to search for.
        :param code: (optional) Target to search.
        :return: number of occurrences of opcode in search target
        """

        if code is None:
            code = self.code_objects

        count = 0
        for bytecode in code:
            for instruction in dis.get_instructions(bytecode):
                if instruction.opcode == opcode:
                    count += 1

        return count

    def _collect_code(self, code=None):
        """
        Utility function for optimizing code access.

        :param code: parent code object
        :return: all child code objects of code
        """

        code_objects = []
        if code is None:
            code = self.compiled_code
        code_objects.append(code)
        for const in code.co_consts:
            if isinstance(const, CodeType):
                code_objects += self._collect_code(const)
        return code_objects

    def _count_ast_occurrences(self, query, node=None, target=None):
        node = node or self.ast if not target else ast.parse(target)
        count = 0
        if type(node) == query:
            count += 1

        if hasattr(node, "body"):
            for child in node.body:
                count += self._count_ast_occurrences(query, child)

        if hasattr(node, "value"):
            count += self._count_ast_occurrences(query, node.value)

        return count

    def _search_ast(self, query, node=None):
        node = node or self.ast

        if isinstance(node, ast.FunctionDef) or isinstance(node, ast.ClassDef):
            if node.name == query.__code__.co_name and node.lineno == query.__code__.co_firstlineno:
                return node

        if hasattr(node, "body"):
            for child in node.body:
                result = self._search_ast(query, child)
                if result is not None:
                    return result
