"""
In python, arrays are homogeneous and can only hold data of single kind.
Because it's just a wrapper around a C array, 
But there are an array like datastrucre in python, called lists.

If memory is concern, work with arrays, if not, then work with lists like any other lang.
"""

"""
Python defines both an array and a list type and while they look and feel similar to one another they have their own uses. The array.array class in Python is a thin wrapper around a C array and this introduces some limitations. For example, Python arrays are homogeneous and can only hold data of a single kind. The type does take up much less space in memory than Python lists however so in general you would use an array if space was a concern or if you wanted to expose some C functionality.

As mentioned in the course, Python lists are the more frequently used type and the de facto representation of an array like structure. They are a heterogeneous and contiguous data structure.
"""