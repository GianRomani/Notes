# Kernel trick
Created: 2023-01-10 12:03
#note

The kernel trick avoids the explicit mapping that is needed to get linear learning algorithms to learn a nonlinear function or decision boundary.

A kernel is a function that takes as inputs vectors in the original space and returns the dot product of the vectors in the feature space, i.e. if we have data $x,z \in X$ and a map $\phi:X \rightarrow R^n$ then $k(x,z)= \langle \phi(x), \phi(z) \rangle$ is a kernel function.

Our kernel function accepts inputs in the original lower dimensional space and returns the dot product of the transformed vectors in the higher dimensional space.

Kernel trick is often used for [[Support Vector Machine]], because it allows us to operate in the original feature space without computing the coordinates of the data in a higher dimensional space. One critical thing to keep in mind is that when we map data to a higher dimension, there are chances that we may overfit the model. This means that choosing the right kernel function and regularization are of great importance.

## References
1. [TDS](https://towardsdatascience.com/the-kernel-trick-c98cdbcaeb3f)
2. [Wikipedia](https://en.wikipedia.org/wiki/Kernel_method#Mathematics:_the_kernel_trick)
3. [Medium](https://medium.com/@zxr.nju/what-is-the-kernel-trick-why-is-it-important-98a98db0961d)
4. [Quora](https://www.quora.com/What-are-kernels-in-machine-learning-and-SVM-and-why-do-we-need-them/answer/Lili-Jiang?srid=oOgT)

#### Tags
#ml #nonlinearity