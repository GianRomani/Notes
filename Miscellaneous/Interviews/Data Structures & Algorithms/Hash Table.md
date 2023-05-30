The [Hash Table](https://www.techinterviewhandbook.org/algorithms/hash-table/), or hash map, is a data structure that implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function on an element to compute an index, also called a hash code, into an array of buckets or slots, from which the desired value can be found. During lookup, the key is hashed, and the resulting hash indicates where the corresponding value is stored.

In the case of hash collisions, there are a number of collision resolution techniques that can be used. You will unlikely be asked about details of collision resolution techniques in interviews:

-   **Separate chaining** - A linked list is used for each value, so that it stores all the collided items.
-   **Open addressing** - All entry records are stored in the bucket array itself. When a new entry has to be inserted, the buckets are examined, starting with the hashed-to slot and proceeding in some probe sequence, until an unoccupied slot is found.

**Time complexity**
| Operation | BigO | Note                                                    |
| --------- | ---- | ------------------------------------------------------- |
| Access    | N/A  | Accessing is not possible as the hash code is not known |
| Search    | O(1) |                                                         |
| Insert    | O(1) |                                                         |
| Remove    | O(1) |                                                         |


# Resources
1. [Medium 1](https://medium.com/basecs/taking-hash-tables-off-the-shelf-139cbf4752f0)
2. [Medium 2](https://medium.com/basecs/hashing-out-hash-functions-ea5dd8beb4dd)
3. [Video](https://www.coursera.org/lecture/data-structures-optimizing-performance/core-hash-tables-m7UuP)