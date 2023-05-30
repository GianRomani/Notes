Like arrays, a linked list is used to represent sequential data. It is a linear collection of data elements whose order is not given by their physical placement in memory, as opposed to arrays, where data is stored in sequential blocks of memory. Instead, each element contains an address of the next element. It is a data structure consisting of a collection of nodes which together represent a sequence.

In its most basic form, each node contains: data, and a reference (in other words, a link) to the next node in the sequence.

**Pros:** Insertion and deletion of a node in the list (given its location) is O(1) whereas in arrays the following elements will have to be shifted.

**Cons:** Access time is linear because directly accessing elements by its position in the list is not possible (in arrays you can do `arr[4]` for example). You have to traverse from the start.

**Types of linked lists:**
- Singly linked list: each node points to the next one, and the last one points to `null`;
- Doubly linked list: each node has two pointers, `next` which points to the next node and `prev` which points to the previous one. The `next` pointer of the last node and the `prev` of the first both point to `null`;
- Circular linked list: special type of singly linked list in which the last node points back to the first one. The circular double linked list also exists.

**Note:** Python does not have an implementation for linked list.

**Time complexity**
| Operation | Big-O  | Note                                                 |
| --------- | ------ | ---------------------------------------------------- |
| Access    | $O(n)$ |                                                      |
| Search    | $O(n)$ |                                                      |
| Insert    | $O(1)$ | Assumes you have traversed to the insetion position  |
| Remove    | $O(1)$ | Assumes you have traversed to the node to be removed |

**Common routines:**
- Counting the number of nodes in the linked list;
- Reversing a linked list in-place;
- Finding the middle node of the linked list using two pointers;
- Merging two linked lists together.

**Corner cases:**
- Empty linked list (head is `null`);
- Single node;
- Two nodes;
- Linked list has cycles. **Tip:** clarify beforehead with the interviewer whether there can be a cycle in the list.

## Techniques

**Sentinel/dummy nodes:** Adding a sentinel/dummy node at the head and/or tail might help to handle many edge cases where operations have to be performed at the head or the tail. The presence of dummy nodes essentially ensures that operations will never have be done on the head or the tail, thereby removing a lot of headache in writing conditional checks to dealing with null pointers. Be sure to remember to remove them at the end of the operation.

**Two pointers:** very common approach used in several scenarios:
- getting the $k^{th}$ from the last node;
- detecting cycles → one pointer increments twice as much as the other, if the two pointers meet then a cycle is present;
- getting the middle node → one pointer increments twice as much as the other. When the fast node reaches the end of the list, the slower one will be at the middle.

**Using space:** many linked list problems can be easily solved by creating a new linked list and adding nodes to the new linked list with the final result. This approach is the easiest one, but often the interviewer could ask to solve the problem in-place.

**Modification operations:** some common operations that can be easily achieved:
- truncate a list;
- swapping values of nodes;
- combining two nodes.

## Resources
1. [Tech Interview Handbook](https://www.techinterviewhandbook.org/algorithms/linked-list/)
2. [Medium part 1](https://medium.com/basecs/whats-a-linked-list-anyway-part-1-d8b7e6508b9d)
3. [Medium part 2](https://medium.com/basecs/whats-a-linked-list-anyway-part-2-131d96f71996)
4. [Video 1](https://www.coursera.org/lecture/data-structures/singly-linked-lists-kHhgK)
5. [Video 2](https://www.coursera.org/lecture/data-structures/doubly-linked-lists-jpGKD)