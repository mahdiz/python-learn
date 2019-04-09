
# Learning Python
Run using Python 3.0+

## Basics 


```python
# Reading an int
i = int(input("Enter an integer: "))
print(i+1)
```

    Enter an integer: 6
    7



```python
# Reading multiple values
v1, v2, v3 = (int(x) for x in input("Enter three integers: ").strip().split())
print("(" + str(v1*2) + ", " + str(v2*2) + ", " + str(v3*2) + ")")
```

    Enter three integers: 6 7 8
    (12, 14, 16)



```python
# Creating a tuple
t = tuple(int(x) for x in input("Enter a comma-separated list of integers: ").strip().split(','))
print(tuple(x*2 for x in t))
```

    Enter a comma-separated list of integers: 4,5,6,7
    (8, 10, 12, 14)



```python
print(sorted([8,3,1,0,2,7]))
```

    [0, 1, 2, 3, 7, 8]



```python
for x in range(4):  # By default, range starts at 0, i.e., [0,4)
    print(x)
```

    0
    1
    2
    3



```python
for x in range(3,6):
    print(x)
```

    3
    4
    5



```python
a = [1,2,3,4,5,6,7,8]
b = [4,5,6,7,8,9,0,1]
print(a[-1])    # Last values
print(a[-2])    # Second to last values
print(a[-2:])   # The last two values
print(a[:-2])   # Everything except the last two values
```

    8
    7
    [7, 8]
    [1, 2, 3, 4, 5, 6]



```python
# Zip two arrays to create pairs
firsts = ['a', 'b', 'c']
seconds = [4, 5, 6]
print(list(zip(firsts, seconds)))
```

    [('a', 4), ('b', 5), ('c', 6)]


### If Statements


```python
if a[0] > 0:
    print("First is positive.")
elif a[0] == 0:                     # Note: elif, not elseif
    print("First is zero.")
elif a[0] != -65:
    print("First is not -65.")
elif a[0] % 2 == 0 and a[1] > 0 or a[2] < 0:         # Note: 'and', 'or'
    print("Complicated :)")
else:
    print("Something else :)")
```

    First is positive.



```python
print("Not found!" if 6 not in a else "Found!")         # one-line if (Note: "not in")
```

    Found!


### Bitwise Operations
``0b`` at beginning defines binary literals.


```python
a = 0b1110
b = 0b1001
print("AND=" + str(a & b) + ", OR=" + str(a | b) + ", XOR=" + str(a ^ b) + ", NOT=" + str(~a) + ", SHIFT-LEFT=" + str(a << 1))
```

    AND=8, OR=15, XOR=7, NOT=-15, SHIFT-LEFT=28



```python
print(list(1 << i for i in range(10)))         # fastest way to generate powers of two
```

    [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]


## Lambda Expressions


```python
# Lambdas are nameless functions
f = lambda x,y: x + y**2
print(f(4,3))
```

    13



```python
c = [(3, 'three'), (1,'one'), (4, 'four'), (2, 'two')]
c.sort(key=lambda x: x[1])
print(c)
```

    [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]


## Map, Reduce, and Filter


```python
# Map applies a function to every item in a list and returns a new list
items = [1, 2, 3, 4, 5]
print(list(map(lambda x: x**2, items)))
```

    [1, 4, 9, 16, 25]



```python
# Reduce also applies a function to every item but returns only a single value that combine
# combines all items accroding to the function
from functools import reduce
print(reduce(lambda x,y: x*y, items))
```

    120



```python
# Filter creates a list of elements for which a function returns true
print(list(filter(lambda x: x % 2 == 0, items)))
```

    [2, 4]



```python
a = [6, 7, 8, 9, 10]
print(list(map(lambda x, y: x+y, items, a)))       # Map over two arrays
```

    [7, 9, 11, 13, 15]


## Data Structures


```python
# Dictionary
dic = {}
dic['a'] = 5
dic['b'] = 6
dic[123] = 7
print(dic)
```

    {'a': 5, 'b': 6, 123: 7}



```python
# Enumerate dictionary keys
for k in dic.keys():
    print(k, '->', dic[k])
```

    a -> 5
    b -> 6
    123 -> 7



```python
# Another way
for k,v in dic.items():
    print(k, '->', v)
```

    a -> 5
    b -> 6
    123 -> 7



```python
# Stacks are implemented using lists
stack = [3, 4, 5]
stack.append(6)     # Stack push
print(stack.pop()) 
```

    6



```python
# List can be used as a queue but it's inefficient to pop the first element (O(n)) so we use class queue
from queue import Queue
q = Queue()
q.put(4)        # enqueue
q.put(2)
q.put(5)
print(q.get())  # deque
```

    4


## Matrices


```python
# Basic Python matrix
print([[1, 2], [3, 4]])
M = [[0 for j in range(3)] for i in range(4)]  # Creates a 4x3 matrix using list comprehension
print(M)
```

    [[1, 2], [3, 4]]
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]



```python
# numpy matrix is much more powerful
import numpy as np
A = np.matrix([[1, 2], [3, 4]])
print(A*2)
print(A.T)   # transpose
```

    [[2 4]
     [6 8]]
    [[1 3]
     [2 4]]


## Classes


```python
class Person:

    def __init__(self, first, last):       # constructor
        self.firstname = first
        self.lastname = last

    def __str__(self):                     # like Java's ToString()
        return self.firstname + " " + self.lastname

x = Person("Betty", "Simpson")
print(x)
```

    Betty Simpson



```python
# Inheritance
class Employee(Person):

    def __init__(self, first, last, staffnum):
        super().__init__(first, last)
        self.staffnumber = staffnum

    def GetStaffNumber(self):             # self has to be fed into every method
        return self.staffnumber
    
    def __str__(self):                    # overriding
        return super().__str__() + ", " +  self.staffnumber

y = Employee("Michael", "Jackson", "1007")
print(y)
```

    Michael Jackson, 1007


## Examples
### DFS Traversal


```python
graph = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}

def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for child in graph[node]:
            dfs(graph, child, visited)
    return visited

visited = dfs(graph, 'A', [])
print(visited)
```

    ['A', 'B', 'S', 'C', 'D', 'E', 'H', 'G', 'F']


### BFS Traversal


```python
from queue import Queue

def bfs(graph, node):
    visited = []
    q = Queue()
    q.put(node)
    while not q.empty():
        n = q.get()
        if n not in visited:
            visited.append(n)
            for child in graph[n]:
                q.put(child)
    return visited
            
visited = bfs(graph, 'A')
print(visited)
```

    ['A', 'B', 'S', 'C', 'G', 'D', 'E', 'F', 'H']


### Quick Sort


```python
def quick_sort(arr, left, right):
    if left >= right:
        return
    
    pivot = arr[int((left+right)/2)]
    index = partition(arr, left, right, pivot)
    quick_sort(arr, left, index - 1)
    quick_sort(arr, index, right)
    
        
def partition(arr, left, right, pivot):
    while left <= right:       
        while arr[left] < pivot:
            left += 1

        while arr[right] > pivot:
            right -= 1

        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return left
        
a = [8,9,7,1,5,4,6,3,0,2]
quick_sort(a, 0, 9)
print(a)
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


### Other Examples
Given an array of single-digit integers, add one to the integer represented by the array.


```python
def add_one(arr):
    a = [0]*len(arr)
    i = 1
    while i <= len(a) and arr[-i] == 9:
        a[-i] = 0
        i += 1
    
    if i <= len(a):
        a[-i] = arr[-i] + 1
        i += 1
        while i <= len(a):
            a[-i] = arr[-i]
            i += 1
    else:
        a.insert(0,1)
    return a

print(add_one([1,2,3,4]))
print(add_one([1,2,3,9]))
print(add_one([9,9,9,9]))
print(add_one([]))
```

    [1, 2, 3, 5]
    [1, 2, 4, 0]
    [1, 0, 0, 0, 0]
    [1]


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
