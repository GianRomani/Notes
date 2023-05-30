A tree is a widely used abstract data type that represents a hierarchical structure with a set of connected nodes. Each node in the tree can be connected to many children, but must be connected to exactly one parent, except for the root node, which has no parent.

A tree is an undirected and connected acyclic graph. There are no cycles or loops. Each node can be like the root node of its own subtree, making [[Recursion]] a useful technique for tree traversal

Trees are commonly used to represent hierarchical data, e.g. file systems, JSON, and HTML documents. Do check out the section on [[Trie]], which is an advanced tree used for efficiently storing and searching strings.

**Terminology:**
- Neighbour: parent or child of a node;
- Ancestor: a node reachable by traversing its parent chain;
- Descendant: a node in the node's subtree;
- Degree: number of children of a node;
- Degree of a tree: maximum degree of nodes in the tree;
- Distance: number of edges along the shortest path between two nodes;
- Level/Depth: number of edges along the unique path between a node and the root node;
- Width: number of nodes in a level.
- Binary tree: nodes in a binary tree have a maximum of two children;
- Complete binary tree: every level, except the last, is completely filled;
- Balanced binary tree: left and right subtrees of every node differ in height by no more than 1.
- Traversals:
	-   **In-order traversal** - Left → Root → Right
	-   **Pre-order traversal** - Root → Left → Right
	-   **Post-order traversal** - Left → Right → Root

**Binary search tree (BST):** In-order traversal of a BST will give all elements in order. When dealing with problems that involve BST, the solution is usually faster than O(n).
| Operation | Big-O       |
| --------- | ----------- |
| Access    | $O(log(n))$ |
| Search    | $O(log(n))$ |
| Insert    | $O(log(n))$ |
| Remove    | $O(log(n))$ | 
Space complexity for the traversal of balanced tress is O(h) where h is the height of the tree, while traversing very skewed trees has a cost of O(n).

**Things to look out for during interviews:** You should be very familiar with writing pre-order, in-order, and post-order traversal recursively. Interviewers sometimes ask candidates to write them iteratively.

**Corner cases:**
- Empty tree;
- Single node;
- Two nodes;
- Very skewed tree (similar to linked list).

**Common routines:**
-   Insert value
-   Delete value
-   Count number of nodes in tree
-   Whether a value is in the tree
-   Calculate height of the tree
-   Binary search tree
    -   Determine if is binary search tree
    -   Get maximum value
    -   Get minimum value

## Techniques
**Recursion:** Recursion is the most common approach for traversing trees. When you notice that the subtree problem can be used to solve the entire problem, try using recursion.

When using recursion, always remember to check for the base case, usually where the node is `null`.

**Summation of nodes:** If the question involves summation of nodes along the way, be sure to check whether nodes can be negative.


## Resources
1. [Tech Interview Handbook](https://www.techinterviewhandbook.org/algorithms/tree/)
2. [Video](https://www.coursera.org/lecture/data-structures/trees-95qda)
3. [Trees](https://medium.com/basecs/how-to-not-be-stumped-by-trees-5f36208f68a7)
4. [Binary Trees](https://medium.com/basecs/leaf-it-up-to-binary-trees-11001aaf746d)
5. [AVL](https://medium.com/basecs/the-little-avl-tree-that-could-86a3cae410c7)
6. [B-Trees](https://medium.com/basecs/busying-oneself-with-b-trees-78bbf10522e7)
7. [Red-Black Trees](https://medium.com/basecs/painting-nodes-black-with-red-black-trees-60eacb2be9a5)