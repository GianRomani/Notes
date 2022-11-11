[Arrays](https://www.guru99.com/array-data-structure.html) hold values of the same type at contiguous memory locations. In an array, we're usually concerned about two things - the position/index of an element and the element itself.

**Advantages**:
- store multiple elements of the same type with just one variable;
- accessing elements is fast, if an index is used (in linked list we have to traverse the list anyway);
**Disadvantages**:
- adding and removal of elements is slow because we have to shift remaining elements (obviously removing or adding an element from/in the last position is not a problem);
- the size can be fixed, and it can not be altered afterwards;

**Common terms**:
- subarray → range of contiguous values within an array ([2,3,4] is s subarray for [1,2,3,4,5]);
- subsequence → sequence derived from the original one, where elements are not necessarily contiguous ([1,3,5] is a subsequence from [1,2,3,4,5])

**Time complexity**
|Operation|Big-O|Note|
|-----|------|-----|
|Access|O(1)||
|Search|O(n)|
|Search(Sorted array)|O(log(n))||
|Insert|O(n)|Insertion requires shifting of all the subsequent elements|
|Insert(at the end)|O(1)|No need for shifting|
|Remove|O(n)|Removal requires shifting of all the subsequent elements|
|Remove(at the end)|O(1)|No need for shifting|


**Questions and things to watch out for:**
- are there duplicates values in the array? Would the presence of duplicates values affect the answer?
- Do not go out of bounds;
- concatenation and slicing would take O(n). Use start and end indices

**Corner cases:**
- empty sequence;
- sequence with 1 or 2 elements;
- sequence with repeated elements;
- duplicated values in the sequence

## Techniques

### Sliding window 
See [here](https://www.geeksforgeeks.org/window-sliding-technique/). 
It can be used if the size of the window is fixed throughout the complete nested loop. General idea: compute the result of the 1st window and then use a loop to slide the window by 1.
Example: compute maximum sum of *k* elements in an array of size *n* → Compute the result for the first window and then for the second one subtract the first value of the previous block from the sum and add the new element.

**Cost**: O(n)

### Two pointers
A general version of [[#Sliding window]].
Used to pointers to traverse one or two arrays. 
Example: merge of two sorted arrays.

### Traversing from the right
It consists in traversing from the end instead of the start, see [here](https://leetcode.com/problems/daily-temperatures/).

### Sorting the array
If the array is sorted, some sort of binary search can be used → solution should be faster than O(n).

Sometimes sorting can simplify the problem by a lot.

### Precomputation
For questions where summation or multiplication of a subarray is involved, pre-computation using hashing or a prefix/suffix sum/product might be useful.

### Index as a hash key
If you are given a sequence and the interviewer asks for O(1) space, it might be possible to use the array itself as a hash table. For example, if the array only has values from 1 to N, where N is the length of the array, negate the value at that index (minus one) to indicate the presence of that number.

### Traversing the array more than once
This might be obvious, but traversing the array twice/thrice (as long as fewer than n times) is still O(n). Sometimes traversing the array more than once can help you solve the problem while keeping the time complexity to O(n).

# References
1. [Tech Interview](https://www.techinterviewhandbook.org/algorithms/array/)