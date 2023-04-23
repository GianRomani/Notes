[Recursion](https://www.techinterviewhandbook.org/algorithms/recursion/) is a method of solving a computational problem where the solution depends on solutions to smaller instances of the same problem.
All recursive functions contain two parts:
1.  A base case (or cases) defined, which defines when the recursion is stopped, otherwise it will go on forever!
2.  Breaking down the problem into smaller sub-problems and invoking the recursive call.

**Things to look out for during interviews**
-   Always remember to always define a base case so that your recursion will end.
-   Recursion is useful for permutation, because it generates all combinations and tree-based questions. You should know how to generate all permutations of a sequence as well as how to handle duplicates.
-   Recursion implicitly uses a stack. Hence, all recursive approaches can be rewritten iteratively using a stack. Beware of cases where the recursion level goes too deep and causes a stack overflow (the default limit in Python is 1000). You may get bonus points for pointing this out to the interviewer. Recursion will never be O(1) space complexity because a stack is involved, unless there is [tail-call optimization](https://stackoverflow.com/questions/310974/what-is-tail-call-optimization) (TCO). Find out if your chosen language supports TCO.
-   Number of base cases. In the Fibonacci example, note that one of the recursive calls invoke `fib(n - 2)`. This indicates that you should have 2 base cases defined so that your code covers all possible invocations of the function within the input range. If your recursive function only invokes `fn(n - 1)`, then only one base case is needed.

**Note:** in some cases, you may want to compute results for previously computed inputs. In this scenario, if such values are memoized and used again, the efficiency of the algorithm can be greatly improved, and the time complexity becomes O(n).

# Resources
1. [Readings](https://www.cs.utah.edu/~germain/PPS/Topics/recursion.html)
2. [Video](https://www.coursera.org/lecture/programming-languages/tail-recursion-YZic1)
