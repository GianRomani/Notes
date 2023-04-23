A heap is a specialized tree-based data structure which is a complete tree that satisfies the heap property.

-   Max heap - In a max heap the value of a node must be greatest among the node values in its entire subtree. The same property must be recursively true for all nodes in the tree.
-   Min heap - In a min heap the value of a node must be smallest among the node values in its entire subtree. The same property must be recursively true for all nodes in the tree.

In the context of algorithm interviews, heaps and priority [[Queue]]s can be treated as the same data structure. A heap is a useful data structure when it is necessary to repeatedly remove the object with the highest (or lowest) priority, or when insertions need to be interspersed with removals of the root node.

**Note:** Python has [this](https://docs.python.org/3/library/heapq.html) implementation.

**Note:** If you see a top or lowest *k* being mentioned in the question, it is usually a signal that a heap can be used to solve the problem. If you require the top _k_ elements use a Min Heap of size _k_. Iterate through each element, pushing it into the heap (for python `heapq`, invert the value before pushing to find the max). Whenever the heap size exceeds _k_, remove the minimum element, that will guarantee that you have the _k_ largest elements.

**Time complexity**
| Operation                                    | Big-O     |
| -------------------------------------------- | --------- |
| Find max/min                                 | O(1)      |
| Insert                                       | O(log(n)) |
| Remove                                       | O(log(n)) |
| Heapify (create a heap out of a given array) | O(n)      | 


## Resources
1. [Tech Interview Handbook](https://www.techinterviewhandbook.org/algorithms/heap/)
2. [Medium](https://medium.com/basecs/learning-to-love-heaps-cef2b273a238)
3. [Heap sort](https://medium.com/basecs/heapify-all-the-things-with-heap-sort-55ee1c93af82)
4. [Yale University](http://www.cs.yale.edu/homes/aspnes/classes/223/notes.html#heaps)
5. 