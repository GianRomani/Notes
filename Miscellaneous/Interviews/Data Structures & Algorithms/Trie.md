Tries are special [[Tree]]s (prefix trees) that make searching and storing strings more efficient. Tries have many practical applications, such as conducting searches and providing autocomplete.

**Time complexity**
*m* is the length of the string used in the operation.
| Operation | Big-O |
| --------- | ----- |
| Search    | O(m)  |
| Insert    | O(m)  |
| Remove    | O(m)  | 

**Corner cases:**
-   Searching for a string in an empty trie
-   Inserting empty strings into a trie

**Tip:** Sometimes preprocessing a dictionary of words (given in a list) into a trie, will improve the efficiency of searching for a word of length k, among n words. Searching becomes O(k) instead of O(n).

## Resources
1. [Tech Interview Handbook](https://www.techinterviewhandbook.org/algorithms/trie/)
2. [Medium 1](https://medium.com/basecs/trying-to-understand-tries-3ec6bede0014)
3. [Compressing radix trees](https://medium.com/basecs/compressing-radix-trees-without-too-many-tears-a2e658adb9a0)