Created: 2023-01-10 11:23
#note

ML model used for linear and non-linear classification, regression, and even outlier detection.

In SVM, a data point is viewed as a p-dimensional vector, and we wanted to know whether we can separate such points with a (p-1)-dimensional hyperplane. This is called a linear classifier.

There are many hyperplanes that classify the data. To choose the best hyperplane that represents the largest separation or margin between the two classes. Maximizing the margin distance provides some reinforcement so that future data points can be classified with more confidence. If such a hyperplane exists, it is known as a maximum-margin hyperplane and the linear classifier it defines is known as a maximum margin classifier.
The Support Vectors are the points that are the closer to the dividing hyperplane.

Any Hyperplane can be written as the set of points $x$ satisfying: $w^Tx-b=0$, where $w$ is the normal vector to the hyperplane.

If the training data is **linearly separable**, we can use Hard-margin and hyperplanes can be described by the equations: $w^Tx-b=1$ (everything above this boundary belong to the class labelled as 1) and $w^Tx-b=-1$ (everything below belongs to class -1).

When data is **not linearly separable**, we use the Hinge loss: $max(0,1-y_i(w^Tx_i-b))$, where $y_i$ is the target. Then the goal is to minimize: $\lambda \lVert w \rVert^2 + [\frac{1}{n}\sum_{i=1}^n \max(0,1-y_i(w^Tx_i-b))]$, where the parameter $\lambda>0$ determines the trade-off between increasing the margin size and ensuring that the $x_i$ lie on the correct side of the margin.

**Nonlinear classifiers** can be used thanks to the [[Kernel trick]]. The resulting algorithm is formally similar, except that every dot product is replaced by a nonlinear kernel function.

Some common kernels include:

-   [Polynomial (homogeneous)](https://en.wikipedia.org/wiki/Homogeneous_polynomial "Homogeneous polynomial"):  $k(x_i,x_j)=(x_i\cdot x_j)^d$. Particularly, when $d=1$, this becomes the linear kernel.
-   [Polynomial](https://en.wikipedia.org/wiki/Polynomial_kernel "Polynomial kernel") (inhomogeneous): $k(x_i,x_j)=(x_i \cdot x_j + r)^d$
-   Gaussian [radial basis function](https://en.wikipedia.org/wiki/Radial_basis_function_kernel "Radial basis function kernel"): $k(x_i,x_j)=\exp (-\gamma \lVert x_i-x_j \rVert^2)$ for $\gamma>0$. Sometimes parametrized using $\gamma=1/(2\sigma^2)$.
-   [Sigmoid function](https://en.wikipedia.org/wiki/Sigmoid_function "Sigmoid function") ([Hyperbolic tangent](https://en.wikipedia.org/wiki/Hyperbolic_tangent "Hyperbolic tangent")): $k(x_i,x_j)=\tanh(kx_i \cdot x_j +c)$ for some (not every) $k>0$ and $c<0$.

 
## References
1. [ml questions](https://www.interviewbit.com/machine-learning-interview-questions/)
2. [Wikipedia](https://en.wikipedia.org/wiki/Support_vector_machine)
3. [TDS](https://towardsdatascience.com/support-vector-machine-introduction-to-machine-learning-algorithms-934a444fca47)

## Code
1. [Sklearn](https://scikit-learn.org/stable/modules/svm.html)

#### Tags
#ml #algorithm #regression #classification #supervised