/*
JavaScript does not have an explicit array data type and arrays are represented by the Array object which is a list like object. Array is an Object type with special constructor and accessor methods. Its prototype has methods to perform traversal and mutation operations.

JavaScript arrays are heterogeneous, meaning the types of elements are not fixed and neither is the size. Unlike the description given in the course video, arrays in JavaScript are not contiguous data structures and the data stored in the array can be located in a non-contiguous location.

There are several ways to create an array:
*/

var arr = new Array(1);
var arr = Array(1);
var arr = [1];

/*
Since arrays are regular JavaScript objects with syntactic sugar there are some nuances to their behavior. Creating a new array does not allocate any memory and the size of an array and its corresponding length are not always the same.

Consider the following snippet:
*/
var values = [];
values[0] = 1;
values[9] = 2;


/*
Here an array has been created and two values have been inserted at index positions 0 and 9. The length of the array here is actually 10, even though there are only 2 elements in the array.

Additional Resources:

MDN: Array
MDN: Indexed Collections
*/