**What’s the geometric interpretation of the dot product of two vectors?**
The dot product (or inner product) between two vector $\vec{a}$ and $\vec{b}$ is considered as the projection of $\vec{a}$ onto $\vec{b}$ multiplied by the length of $\vec{b}$, i.e. $\vec{a}\cdot\vec{b}=\lVert \vec{a} \rVert \lVert \vec{b} \rVert \cos(\theta)$. 

**Given a vector $\vec{u}$, find a vector $\vec{v}$ of unit length such that the dot product of $\vec{u}$ and $\vec{v}$ is maximum.**
Since $\vec{v}$ has unit length, $\lVert \vec{v} \rVert=1$, then $\vec{u} \cdot \vec{v} = \lVert u \rVert \cos(\theta)$ which is optimized when $\cos(\theta)=1$, i.e. when $\theta=k\pi$.

**Given two vectors a=[3,2,1] and b=[−1,0,1]. Calculate the outer product $a^Tb$?**

$\left[\begin{array}{l} 3 \\ 2 \\ 1 \end{array}\right] \otimes \left[\begin{matrix} -1 & 0 & 1 \end{matrix}\right]=\begin{bmatrix} -3 & 0 & 3 \\ -2 & 0 & 2 \\ -1 & 0 & 1 \end{bmatrix}$.

So $M_{ij}=a_i \cdot b_j$.

**Give an example of how the outer product can be useful in ML.**
[Check here](https://www.quora.com/Why-are-inner-products-and-dot-products-so-important-and-prevalent-in-machine-learning). TLDR; Outer product is used in a lot of applications for ML, e.g. in MLP the input (a vector) is multiplied with the matrix of weights using outer product.

**What does it mean for two vectors to be linearly independent?**
Two vectors are linearly independent if the only linear combination of the vectors that is equal to 0 is the trivial one (with all coefficients equal to 0).

**Given two sets of vectors $A=a_1,a_2,a_3,...,a_n$ and $B=b_1,b_2,b_3,...,b_m$, how do you check that they share the same basis?**
If we can write each vector in the second set as linear combinations of the vectors in the first, then the two sets belong to the same basis.

**Given $n$ vectors, each of $d$ dimensions. What is the dimension of their span?**
The span of a set S of vectors, denoted span(S) is the set of all linear combinations of those vectors.

**What's a norm? What is $L_0,L_1,L_2,L_{norm}$?**
A norm is a real-valued function $p:X \rightarrow R$, where $X$ is a vector space over a subfield of the Complex numbers, with the following characteristics:
1. Triangle inequality: $p(x+y) \leq p(x) + p(y) \, \forall x,y \in X$;
2. Non-negativity: $p(x) \geq 0 \, \forall x \in X$ and $\text{if} \, p(x)=0 \, then \, x=0$;
3. Absolute homogeneity: $p(sx)=|s|p(x) \, \forall x \in X \, \text{and all scalars } s$, where $|s|$ is the absolute value of a scalar $s$.

A norm can be considered as a way to measure the total length of a vector. There are several ways to measure the magnitude of a vector:
- $L_0$: it corresponds to the total number of nonzero elements in a vector;
- $L_1$: it is known as Manhattan Distance. It is the sum of thee magnitudes of the vectors in a space. Example: Given the vector X=(3,4), then $||X||_1=|3|+|4|=7$;
- $L_2$: It is known as Euclidean norm, i.e. the shortest way to go from one point to another. $||X||_2=\sqrt{\sum_{i=1}^{N}(x_i^2)}$;
- $L_{infinity}$: it gives the largest magnitude among each element of a vector. Having X=(-6,5,2), it returns 6.

**How do norm and metric differ? Given a norm, make a metric. Given a metric, can we make a norm?**
A norm measures the size of a vector, while a distance is measuring the distance between two vectors.

If we have a vector space with a norm $\rho$, it is always possible to define a metric in terms of that norm by putting $d(x,y)=\rho(x−y)$. But not every metric is defined in terms of a norm, or even can be defined in terms of a norm. An example is the metric: $d(x,y)=\begin{cases}1 \, \text{if} \, x \neq y \\ 0 \, \text{if} \, x=y\end{cases}$, this is not a norm, in fact if we take a scalar $\alpha$ such that $\alpha \neq 0$ and $|\alpha| \neq 1$, by choosing x, y such that $x \neq y$ we must have that $1 = d(\alpha x, \alpha y) = \rho(\alpha x - \alpha y) = \rho(\alpha(x-y)) = |\alpha| \rho(x-y) = |\alpha|$ which is a contradiction. (Reference: [here](https://www.physicsforums.com/threads/norm-vs-a-metric.671477/#:~:text=A%20norm%20and%20a%20metric,number))