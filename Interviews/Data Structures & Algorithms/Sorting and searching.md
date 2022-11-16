Most of the basic sorting algorithms run in $O(n^2)$, and they are not to be used. Instead, use your programming language's default sorting function.

**Time complexity**
| Algorithm      | Time       | Space      |
| -------------- | ---------- | ---------- |
| Bubble sort    | $O(n^2)$   | $O(1)$       |
| Insertion sort | $O(n^2)$   | $O(1)$      |
| Selection sort | $O(n^2)$   | $O(1)$      |
| Quicksort      | $O(nlog(n))$ | $O(nlog(n))$ |
| Mergesort      | $O(nlog(n))$ | $O(n)$       |
| Heapsort       | $O(nlog(n))$ | $O(1)$       |
| Counting sort  | $O(n+k)$     | $O(k)$       |
| Radix Sort     | $O(nk)$      | $O(n+k)$    |

Binary search → $O(log(n))$

**Things to look out for during interviews:**
Always remember the time and space complexity of the language's default sorting algorithm (Most of the time it is $O(nlog(n))$). Bonus point if you can name the sort. In Python, it is [Timsort](https://en.wikipedia.org/wiki/Timsort).

**Corner cases:**
- Empty sequence;
- sequence with one element;
- sequence with two elements;
- sequence containing duplicate elements

**Tip:** [Counting sort](https://en.wikipedia.org/wiki/Counting_sort) is a non-comparison-based sort you can use on numbers where you know the range of values beforehand.

## Algorithms
### Bubble Sort
Best: $O(n)$, Worst: $O(n^2)$.
Starting from the left, compare adjacent items and keep "bubbling" the larger one to the right. Repeat for the remaining N-1 items.

### Selection Sort
Best and Worst: $O(n^2)$.
Scan the list and find the smallest item, then swap it in the first position. Repeat this for all the other items.

### Insertion Sort
Best: $O(n)$, Worst: $O(n^2)$
Start from a sorted list of 1 item (the first) and N-1 unsorted elements. Take the first unsorted element and insert it in the first sorted list. Repeat until the unsorted list is empty.

### Quick Sort
Best: $O(nlog(n))$, Avg: $O(nlog(n))$, Worst: $O(n^2)$.
There are many versions, one of them works in the following way:
1. pick a “pivot” item;
2. partition the rest of the items in two groups, one composed of smaller items than the pivot, the other of the bigger items;
3. put the pivot between the two sublists;
4. repeat previous steps on the sublists, until the size of the sublist is 1;
5. combine the lists.

In-place memory version:
-   Pick a pivot item and swap it with the last item. We want to partition the data as above, and need to get the pivot out of the way.
-   Scan the items from left-to-right, and swap items greater than the pivot with the last item (and decrement the “last” counter). This puts the “heavy” items at the end of the list, a little like bubble sort.
-   Even if the item previously at the end is greater than the pivot, it will get swapped again on the next iteration.
-   Continue scanning the items until the “last item” counter overlaps the item you are examining – it means everything past the “last item” counter is greater than the pivot.
-   Finally, switch the pivot into its proper place. We know the “last item” counter has an item greater than the pivot, so we swap the pivot there.
-   Phew! Now, run quicksort again on the left and right subset lists. We know the pivot is in its final place (all items to left are smaller; all items to right are larger) so we can ignore it.

### Heapsort
Best/Avg/Worst: $O(nlog(n))$.
Add all items into a heap. Pop the largest item from the heap and insert it at the end (final position). Repeat for all the items.

### Counting Sort
Best/Avg/Worst: $O(n)$.
Assuming the data are integers, in a range of 0-k. Create an array of size K to keep track of how many items appear (3 items with value 0, 4 items with value 1, etc). Given this count, you can tell the position of an item — all the 1’s must come after the 0’s, of which there are 3. Therefore, the 1’s start at item #4. Thus, we can scan the items and insert them into their proper position.

### Radix Sort
Best/Avg/Worst: $O(n)$.
Get a series of numbers, and sort them one digit at a time (moving all the 1000’s ahead of the 2000’s, etc.). Repeat the sorting on each set of digits.

### Tim Sort (used by Python)
Best: $O(n)$, Avg: $O(nlog(n))$, Worst: $O(nlog(n))$.
We divide the Array into blocks known as **Run**. We sort those runs using insertion sort one by one and then merge those runs using the combine function used in merge sort. If the size of the Array is less than run, then Array gets sorted just by using Insertion Sort.
**Note** that the merge function performs well when size subarrays are powers of 2. The idea is based on the fact that insertion sort performs well for small arrays.

# Resources
1. [Tech Interview Handbook](https://www.techinterviewhandbook.org/algorithms/sorting-searching/) has a lot of additional resources;
2. [Guide to sorting](https://medium.com/basecs/sorting-out-the-basics-behind-sorting-algorithms-b0a032873add)
3. [Binary search](https://www.khanacademy.org/computing/computer-science/algorithms#binary-search)
4. [Better explained](https://betterexplained.com/articles/sorting-algorithms/)