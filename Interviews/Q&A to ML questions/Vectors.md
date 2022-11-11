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


**How do norm and metric differ? Given a norm, make a metric. Given a metric, can we make a norm?**

