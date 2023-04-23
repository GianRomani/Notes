A stack is an abstract data type that supports the operations **push** (insert a new element on the top of the stack) and **pop** (remove and return the most recently added element, the element at the top of the stack). As an abstract data type, stacks can be implemented using arrays or singly linked lists.

This behaviour is commonly called LIFO (last in, first out). The name "stack" for this type of structure comes from the analogy to a set of physical items stacked on top of each other.

Stacks are an important way of supporting nested or recursive function calls and is used to implement depth-first search. Depth-first search can be implemented using recursion or a manual stack.

**Note:** in Python, stack can be simulated using [List](https://docs.python.org/3/tutorial/datastructures.html) or by using [LifoQueue](https://docs.python.org/3/library/queue.html).

**Time complexity**
| Operation | Big-O  |
| --------- | ------ |
| Top/Peek  | $O(1)$ |
| Push      | $O(1)$ |
| Pop       | $O(1)$ |
| isEmpty   | $O(1)$ |
| Search    | $O(n)$ | 

**Corner cases:**
- Empty stack. Popping from an empty stack;
- Stack with one item;
- Stack with two items.

## Resources
1. [Tech Interview Handbook](https://www.techinterviewhandbook.org/algorithms/stack/)
2. [Medium](https://medium.com/basecs/stacks-and-overflows-dbcf7854dc67)
3. [Video](https://www.coursera.org/lecture/data-structures/stacks-UdKzQ)