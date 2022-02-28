"""
Accessing Elements
Use the index operator on a list to access values using an index. Note that index values start at 0.
"""

>>> numbers = [1, 2, 3, 4, 5, 6]
>>> numbers[2]
3

"""
Using an index that is out of bounds of the current range of values results in a runtime error.
"""

>>> numbers[12]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range

"""
List Length
To determine the number of items in a list, use the len function.
"""

>>> len(numbers)
6

"""
len is often used to determine the range of valid index values in a list. To avoid runtime errors it is good practice to iterate over a list with a range defined by the result of calling len instead of a hard coded constant.
"""

>>> for i in range(len(numbers)):
...     print(numbers[i])
...
1
2
3
4
5
6

"""
List Operations
To add to a list, use the append(x) method
"""

>>> numbers.append(7)

"""
To add (or concatenate) one list to another, use extend(iterable)
"""

>>> numbers.extend([8, 9, 10])

"""
To insert an item into a list at a given position. Here the value 11 is inserted at index position 10.
"""

>>> numbers.insert(10, 11)

"""
Use the remove(x) method to remove an item from a list. remove() takes a value as an argument and removes the first element in the list that matches the argument.
"""

>>> numbers.remove(11)

"""
Searching for the position of an element in a list is possible using the index(x)
"""

>>> numbers.index(4)
3

"""
List Membership
Use the in and not in operators to test for membership in a list.
"""

>>> if 5 in numbers: print(True)
True
>>> if 30 not in numbers: print(True)
True

"""
Python lists are mutable which means any element can be updated using the index operator along with an index position.
"""

>>> numbers[0] = 22 # Updates first element in list to 22

"""
Additional Resources:

Lists
List Operations
"""