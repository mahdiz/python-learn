# Run with Python 2.x
# Python basic types: int, long, float, str, boolean, byte, list, tuple, set
# Lists are mutable and tuples are immutable.

from collections import deque

def input_example():
    # Reading an int
    i = int(raw_input("Type an integer: "))
    print i + 1

    # Reading two (or more) ints in one line. Note: (1,2) is a "tuple"
    v, e = (int(x) for x in raw_input("Type two integers: ").strip().split())
    print v, e

    # Reading a tuple (explicit cast is needed because the comprehension returns an iterable)
    t = tuple(int(x) for x in raw_input("Type two integers: ").strip().split())
    print t[0]  # Tuples are indexed similar to lists

    print raw_input().strip()       # Remove heading and trailing whitespaces
    print raw_input().strip('.')    # Remove heading and trailing dots

    a = raw_input('Type a space-separated list: ')             # Reading a space-separated list
    print a.split(' ')

    arr = map(int, raw_input('Type a space-separated list of ints: ').split(' '))  # Reading a space-separated int list
    arr.sort()
    print arr


def if_example():
    a = [int(i) for i in raw_input().strip().split()]

    if a[0] > 0:
        print "First is positive."
    elif a[0] == 0:                     # Note elif
        print "First is zero."
    elif a[0] % 2 == 0 and a[1] > 0 or a[2] < 0:         # Note 'and', 'or'
        print "Complicated :)"
    else:
        print "Something else :)"


def loop_example():
    for x in range(5):  # By default, range starts at 0
        print x

    for x in range(1, 5):  # Start at 1
        print x

    # Iterating over a string
    for c in "Hello world!":
        print c

    count = 0
    while count < 5:
        print count, " is  less than 5"
        count += 1
    else:
        print count, " is not less than 5"


def string_example():
    word = "Dragon"
    word = word.lower()     # To lower case

    print word[-1]    # Prints last character
    print word[-2]    # Prints second to last character
    print word[-2:]   # Prints the last two characters
    print word[:-2]   # Prints everything except last two characters
    print word[-1*len(word)]    # First element

    print 'a'*5       # Repeat 'a' 5 times
    print len(word)

    x = " test "
    print x.strip()
    x = "0023.57000"
    print x.strip('0')

    # Convert an int list to a space-separated string of int elements
    a = [1, 2, 3, 4, 5]
    print ' '.join(map(str, a))  # Prints '1 2 3 4 5'


def lambda_example():
    g = lambda x: x**2
    print g(8)


def lists_example():
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    b = [8, 9, 5, 3, 7, 1, 2, 0]
    print filter(lambda x: x % 2 == 0, a)   # Filter based on a condition
    print map(lambda x: x**2, a)            # Using map
    print map(lambda x, y: x+y, a, b)        # Map over two arrays
    print map(int, ['56', '3', '14'])        # Map cast

    # Append to a list
    a.append(15)

    # Append multiple elements to a list (append from an iterable)
    a.extend([9, 4, 6, 7])

    # Delete an element from a list
    a.remove(15)

    # Delete an element from a list using the index
    del a[3]
    del a[1:4]  # Delete a range

    # Reverse a list
    print list(reversed(a))    # NOTE: reversed returns an iterator of the reversed list. Use list() to get the list

    # Sorting an array
    c = [(3, 'three'), (1,'one'), (4, 'four'), (2,'two')]
    c.sort(key=lambda x: x[0])      # Note: Sorts the same list in-place
    print c

    # Reducing: continuously apply a function to array elements
    f = lambda x, y: x+y
    print reduce(f, [1, 2, 3, 4, 5])

    # List comprehension: A way of implementing the well-known mathematical notation of sets.
    s = (x**2 for x in [1, 2, 3, 4, 5])
    print list(s)

    # Zip two arrays to create pairs
    firsts = ['a', 'b', 'c']
    seconds = [4, 5, 6]
    print zip(firsts, seconds)


def data_structures_example():
    # Stacks are implemented using lists
    stack = [3, 4, 5]
    stack.append(6)  # Stack push
    print stack.pop()  # Stack pop

    # Queues are implemented using deque (note: list doesn't have popleft() so we should the deque collection)
    queue = deque([1, 2, 3])
    queue.append(4)  # Queue enqueue
    print queue.popleft()  # Queue deque


def matrix_example():
    A = [[1, 2], [3, 4]]
    print A

    M = [[0 for j in range(3)] for i in range(4)]  # Creates a 4x3 matrix using list comprehension
    print M


def dictionary_example():
    D = {}      # Empty dictionary
    D['a'] = 1
    D['b'] = 2
    D['c'] = 3

    print D

    for k in D.keys():
        print k, '->', D[k]

    for v in D.values():
        print v

    for k,v in D.items():
        print k, '->', v


# Kadane's algorithm
def max_subarray(a):
    n = len(a)
    maxSoFar = [0 for i in range(n)]
    for i in range(n):
        maxSoFar[i] = max(a[i], maxSoFar[i - 1] + a[i])

    return max(maxSoFar)


if __name__ == '__main__':
    data_structures_example()
