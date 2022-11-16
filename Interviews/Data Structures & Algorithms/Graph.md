A graph is a structure containing a set of objects (nodes or vertices) where there can be edges between these nodes/vertices. Edges can be directed or undirected, and can optionally have values (a weighted graph). [[Tree]]s are undirected graphs in which any two vertices are connected by exactly one edge and there can be no cycles in the graph.
Graphs are commonly used to model relationship between unordered entities, such as

-   Friendship between people - Each node is a person and edges between nodes represent that these two people are friends.
-   Distances between locations - Each node is a location and the edge between nodes represent that these locations are connected. The value of the edge represent the distance.

**Graph representation:** You can be given a list of edges and you have to build your own graph from the edges so that you can perform a traversal on them. The common graph representations are:

-   Adjacency matrix
-   Adjacency list
-   Hash table of hash tables

Using a hash table of hash table would be the simplest approach during algorithm interviews. It will be rare that you have to use adjacency matrix or list for graph questions during interviews.

In algorithm interviews, graphs are commonly given in the input as 2D matrices where cells are the nodes and each cell can traverse to its adjacent cells (up/down/left/right). Hence it is important that you be familiar with traversing a 2D matrix. When traversing the matrix, always ensure that your current position is within the boundary of the matrix and has not been visited before.

**Time complexity**
$|V|$ is the number of vertices and $|E|$ is the number of edges.
| Algorithm        | Big-O |
| ---------------- | ----- |
| DFS| O(\|V\| +\|E\|)  |
| BFS              | O(\|V\| + \|E\|) |
| Topological sort | O(\|V\| + \|E\|)      |

**Things to look out for during interviews:**
-   A tree-like diagram could very well be a graph that allows for cycles, and a naive recursive solution would not work. In that case, you will have to handle cycles and keep a set of visited nodes when traversing.
-   Ensure you are correctly keeping track of visited nodes and not visiting each node more than once. Otherwise, your code could end up in an infinite loop.

**Corner cases:**
-   Empty graph
-   Graph with one or two nodes
-   Disjoint graphs
-   Graph with cycles

## Algorithms

**Depth first search:** Depth-first search is a graph traversal algorithm which explores as far as possible along each branch before backtracking. A stack is usually used to keep track of the nodes that are on the current search path. This can be done either by an implicit [[Recursion]] stack, or an actual [[Stack]] data structure.

```python
def traverse(i,j):
	if (i, j) in visited:  
		return 
		
	visited.add((i, j))  
	# Traverse neighbors.  
	for direction in directions:  
		next_i, next_j = i + direction[0], j + direction[1]  
		if 0 <= next_i < rows and 0 <= next_j < cols:  
			# Add in question-specific checks, where relevant.  
			traverse(next_i, next_j)

def dfs(matrix):  
	# Check for an empty matrix/graph.  
	if not matrix:  
		return []  
	  
	rows, cols = len(matrix), len(matrix[0])  
	visited = set()  
	directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
	
	for i in range(rows):  
		for j in range(cols):  
			traverse(i, j)
```

**Breadth first search:** Breadth-first search is a graph traversal algorithm which starts at a node and explores all nodes at the present depth, before moving on to the nodes at the next depth level. A [[Queue]] is typically used to keep track of the nodes that were encountered but not yet explored. It is important to use double-ended queues because in this way enqueuing is O(1) instead of O(n).
```python
from collections import deque

def traverse(i, j):  
	queue = deque([(i, j)])  
	while queue:  
		curr_i, curr_j = queue.popleft()  
		if (curr_i, curr_j) not in visited:  
			visited.add((curr_i, curr_j))  
			# Traverse neighbors.  
			for direction in directions:  
				next_i, next_j = curr_i + direction[0], curr_j + direction[1]  
				if 0 <= next_i < rows and 0 <= next_j < cols:  
					# Add in question-specific checks, where relevant.  
					queue.append((next_i, next_j))  
  
def bfs(matrix):  
	# Check for an empty matrix/graph.  
	if not matrix:  
		return []  
  
	rows, cols = len(matrix), len(matrix[0])  
	visited = set()  
	directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
	for i in range(rows):  
		for j in range(cols):  
			traverse(i, j)
```

**Topological order:** A topological sort or topological ordering of a directed graph is a linear ordering of its vertices such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering. Precisely, a topological sort is a graph traversal in which each node v is visited only after all its dependencies are visited.

Topological sorting is most commonly used for job scheduling a sequence of jobs or tasks which has dependencies on other jobs/tasks. The jobs are represented by vertices, and there is an edge from x to y if job x must be completed before job y can be started.

## Resources
1. [Tech Interview Handbook](https://www.techinterviewhandbook.org/algorithms/graph/)
2. [Medium](https://medium.com/basecs/from-theory-to-practice-representing-graphs-cfd782c5be38)
3. [DFS](https://medium.com/basecs/deep-dive-through-a-graph-dfs-traversal-8177df5d0f13)
4. [BFS](https://medium.com/basecs/going-broad-in-a-graph-bfs-traversal-959bd1a09255)
5. [Dijkstra](https://medium.com/basecs/finding-the-shortest-path-with-a-little-help-from-dijkstra-613149fbdc8e)
6. [Directed acyclic graphs](https://medium.com/basecs/spinning-around-in-cycles-with-directed-acyclic-graphs-a233496d4688)