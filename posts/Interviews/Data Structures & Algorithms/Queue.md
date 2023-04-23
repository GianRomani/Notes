A queue is a linear collection of elements that are maintained in a sequence. The sequence can be modified by the addition of elements at one end of the sequence (**enqueue** operation) and the removal of elements from the other end (**dequeue** operation). Usually, the end of the sequence at which elements are added is called the back, tail, or rear of the queue, and the end at which elements are removed is called the head or front of the queue. As an abstract data type, queues can be implemented using arrays or singly linked lists.
This behaviour is commonly called **FIFO** (first in, first out). The name “queue” for this type of structure comes from the analogy to people lining up in real life to wait for goods or services.

**Note:** Breadth-first search is commonly implemented using queues.

**Note:** In Python, queues are implemented in [queue](https://docs.python.org/3/library/queue.html).

**Time complexity**
| Operation     | Big-O  |
| ------------- | ------ |
| Enqueue/Offer | $O(1)$ |
| Dequeue/Poll  | $O(1)$ |
| Front         | $O(1)$ |
| Back          | $O(1)$ |
| isEmpty       | $O(1)$ | 

**Corner cases:**
- Empty queue;
- Queue with one item;
- Queue with two items.


## Resources
1. [Tech Interview Handbook](https://www.techinterviewhandbook.org/algorithms/queue/)
2. [Medium](https://medium.com/basecs/to-queue-or-not-to-queue-2653bcde5b04)
3. [Video](https://www.coursera.org/lecture/data-structures/queues-EShpq)