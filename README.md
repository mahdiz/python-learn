Python Philosophy 
-----------------

Python is an extremely flexible language and gives you many fancy features such as metaclasses, 
access to bytecode, on-the-fly compilation, dynamic inheritance, object reparenting, import hacks, 
reflection, modification of system internals, etc.

- Python's philosophy: To describe something as clever is NOT considered a compliment in the Python 
culture. 

- Python uses dynamic typing and has a garbage collector for memory management. An important feature 
of Python is dynamic name resolution (late binding), which binds method and variable names during 
program execution.

- Rather than requiring all desired functionality to be built into the language's core, Python was 
designed to be highly extensible. New built-in modules can be easily written in C, C++ or Cython.

- The design of Python offers only limited support for functional programming in the Lisp tradition. 
The standard library has two modules (itertools and functools) that implement functional tools 
borrowed from Haskell and Standard ML.

Python Code Conventions
-----------------------

- Imports should be on separate lines. 

- TODOs should include the string TODO in all caps, followed by your username in parentheses: TODO(username): # TODO(someuser): Use a "*" here for concatenation operator.

- If a class inherits from no other base classes, explicitly inherit from object. This also applies to nested classes.

- Place related classes and top-level functions together in a module. Unlike Java, there is no need to limit yourself to one class per module.

- If an accessor (i.e. getter/setter) function would be trivial you should use public variables instead of accessor functions to avoid the extra cost of function calls in Python. When more functionality is added you can use property to keep the syntax consistent. On the other hand, if access is more complex, or the cost of accessing the variable is significant, you should use function calls. 

- Use CapWords for class names, but lower_with_under.py for module names. 

- Every Python source file should be importable. Your code should always check 
	
	if __name__ == '__main__': 
	
	before executing your main program so that the main program is not executed when the module is imported. All code at the top level will be executed when the module is imported. Be careful not to call functions, create objects, or perform other operations that should not be executed when the file is imported.

- Indent your code blocks with 2 spaces. Never use tabs or mix tabs and spaces.

- Two blank lines between top-level definitions. One blank line between method definitions and between the class line and the first method. Always have a single blank line at the end of the file.

- pychecker is a tool for finding bugs in Python source code. It finds problems that are typically caught by a compiler for less dynamic languages like C and C++. 

- How does python handle generic/template type scenarios? Python uses duck typing, so it doesn't need special syntax to handle multiple types. 