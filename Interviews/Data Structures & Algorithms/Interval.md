Interval questions are a subset of [array](https://www.techinterviewhandbook.org/algorithms/array/) questions where you are given an array of two-element arrays (an interval) and the two values represent a start and an end value. Interval questions are considered part of the array family but they involve some common techniques hence they are extracted out to this special section of their own.

An example interval array: `[[1, 2], [4, 7]]`.

**Things to look out for during interviews:**
- Clarify with the interviewer whether `[1, 2]` and `[2, 3]` are considered overlapping intervals as it affects how you will write your equality checks;
- -   Clarify whether an interval of `[a, b]` will strictly follow `a` < `b` (`a` is smaller than `b`).

**Corner cases:**
- No intervals;
- Single interval;
- Two intervals;
- Non-overlapping intervals;
- An interval totally consumed within another interval;
- Duplicate intervals (exactly the same start and end);
- Intervals which start right where another interval ends - `[[1,2], [2,3]]`
## Techniques
**Sort the array of intervals by its starting point:** a common routine for interval questions is to sort the array of intervals by each interval's starting value.

**Checking if two intervals overlap:** 
```python 
def is_overlap(a,b):
	return a[0] < b[1] and a[1] < b[0]
```

**Merging two intervals:** 
```python
def merge_overlapping_intervals(a,b):
	return [min(a[0], b[0]), max(a[1], b[1])]
```

## Resources
1. [Tech Interview Handbook](https://www.techinterviewhandbook.org/algorithms/interval/)