A matrix is a 2-dimensional array. They are often used for [[Dynamic programming]] and [[Graph]] problems.

**Corner cases:**

- Empty matrix. Check if none of the arrays have 0 as length;
- 1x1 matrix;
- matrix with just one row or column.

## Techniques:
**Creating an empty NxM matrix**: for questions involving traversal or [[Dynamic programming]], you almost always want to work on a matrix that has the same size/dimensions and initialized to empty values. Python code:

```python 
zero_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
```

Then to copy the matrix:
```python
copied_matrix = [row[:] for row in matrix]
```

**Transposing a matrix:** the transpose of a matrix is obtained  by interchanging its rows into columns and vice versa. Python code:
```python
transposed_matrix = zip(*matrix)
```


## Resources
1. [Tech Interview Handbook](https://www.techinterviewhandbook.org/algorithms/matrix/)
L