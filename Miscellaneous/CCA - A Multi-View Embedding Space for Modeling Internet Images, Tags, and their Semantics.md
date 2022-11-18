# CCA - A Multi-View Embedding Space for Modeling Internet Images, Tags, and their Semantics
Created: 2022-07-09 11:08
#paper

This paper investigates the problem of modeling Internet images and associated text or tags for tasks such as image-to-image search, tag-to-image search, and image-totag search (image annotation).

## Main idea
The starting point is Canonical correlation analysis (CCA), which is an approach for mapping visual and textual features to the same latent space. A third view is added to capture high level image semantics, represented either by a single category or multiple non-mutually-exclusive concepts. The three view embedding can be trained either in a supervised or in a unsupervised way. The authors use explicit nonlinear kernel mappings to efficiently approximate kernel CCA. For the retrieval part, a special similarity function in the embedding space is used instead of the Euclidean distance.

## In deep
Given *n* training images each og which is associated with a v-dimensional visual vector and a t-dimensional tag feature vector, the respective matrices are $V \in R^{n \times v}$ and $T \in R^{n \times t}$. Each training image is also associted with semantic class or topic information, which is encoded in a matrix $C \in R^{n \times c}$, where *c* is the number of classes oor topics. It is also possible to model C as a soft indecation matrix, where the i,j-th entry indicated the degree with which image i belongs to the jth class or topic. In the unsupervised scenario, C is latent and must be obtained by clustering the tags.
Let *x*, *y* denote two points from the ith view. The similarity between these points is defined by a kernel function $K_i$ such that $K_i(x,y)= \phi_i(x)\phi_i(y)^T$, where $\phi_i()$ is a function embedding the original feature vector into a nonlinear kernel space. Practical kernel-based leraning shcemes do not work in the embedded space directly, they need to rely on the kernel function. However, the KCCA in this paper is formulated as a task consisting in the solution of a linear projection from the kernel space, since this leads directly to the scalable approximation scheme based on explicit embeddings.
In KCCA the goal is to find matrices 
$W_i$ that project the embedded vectors $\phi_i(x)$ from each view into a low-dimensional common space such that the distances in the resulting sapce between each pair of views for the same data item are minimized. The mathematical formulation for this idea is the following: $min_{W_1,W_2,W_3} \sum_{i,j=1}^3||\phi_i(X_i)W_i-\phi_j(X_j)W_j||_{F}^2$ subject to $W_i^T \sum_{ii}W_i=I, \; w_{ik}^T\sum_{ij}w_{jl}=0, \; i,j=1,...2, \; i!=j, \; k,l=1,...,d, \; k!=l$, where $\sum_{ij}$ is the covariance matrix between $\phi(X_i)$ and $\phi(X_j)$ and $w_{ik}$ is the kth column of $W_i$.
By decomposing the sum in the formula we have three terms: 
1. $min_{W_1,W_2,W_3} ||\phi_1(V)W_1-\phi_2(T)W_2||_{F}^2$ -> this part tries to align corresponding images and tags (it is the only part already persent in the original CCA objective);
2. $||\phi_1(V)W_1-\phi_3(C)W_3||_{F}^2$ -> tries to align images with their semantic topic;
3. $||\phi_2(T)W_2-\phi_3(C)W_3||_{F}^2$ -> tries to align tags  with their semantic topic.

In standard KCCA, instead of directly solving the linear projections of data explicitly mapped into the kernerl space by $\phi_i$, the **kernel trick** is applied and the coordinates of a data point in the CCA space are expressed as linear combinations of kernel values of taht point and several training points (to solve this we should solve a $3n \times 3n$ generalized eigenvalue problem, unfeasible for large-scale data).
In this paper, instead, a scalable approach is proposed, based on the idea of approximate kernel maps. Let $\hat \phi(x)$ denote an approximate kernel mapping such taht $K_i(x,x') \cong \hat \phi_i(x) \hat \phi_i(x')^T$. The dimensionality of $\hat \phi(x)$ needs to be much lower than *n* to reduce the complexity of the problem. Then, instaed of using the kernel trick, we can directly substitute $\hat \phi(x)$ into the linear CCA objective function. The solution is given by: 
$
\begin{bmatrix}
    S_{11}       & S_{12} & S_{13} \\
    S_{21}       & S_{22} & S_{23} \\
    S_{31}       & S_{32} & S_{33}
\end{bmatrix}
\begin{bmatrix}
    w_{1}  \\
    w_{2}  \\
    w_{3}  
\end{bmatrix}
=
\lambda
\begin{bmatrix}
    S_{11} & 0 & 0 \\
    0 & S_{22} & 0 \\
   0 & 0 & S_{33} 
\end{bmatrix}
\begin{bmatrix}
    w_{1}  \\
    w_{2}  \\
    w_{3}  
\end{bmatrix}
$
where $S_{ij}=\hat \phi_i(X_i)^T\hat \phi_j(X_j)$ is the covariance matrix between the ith and jth views and $w_i$ is the column of $W_i$. The size of the problem is $(d_1+d_2+d_3)\times(d_1+d_2+d_3)$, where the $d_i$ are the dimensionalities of the respective explicit mappings $\hat \phi_i()$.

In order toobtain d-dimensional embedding for different views, we form projection matrices $W_i \in R_{d_i \times d}$ from the top d eigenvectors corresponding to each $w_i$. then the projection of a data point *x* from the ith view into the latent CCA space is given by $\hat \phi_i(x)W_i$. Once they are learned, the respective projection matrices are applied to each vie individually, which means that at test time, we can compute the embedding for data for which one or two views are missing.

For what concerns the similarity function used, the one used in this approach consists in scaling the dimensions in the common latent space by the magnitude of the corresponding eigenvalues and then compute normalized correlation between projected vectors. Given two points,x and y, from the ith and jth views, the similarity function can is defined as follows: $sim(x,y)= \dfrac{(\hat \phi_i(x)W_iD_i)(\hat \phi_j(y)W_jD_j)^T}{||\hat \phi_i(x)W_iD_i||_2||\hat \phi_j(y)W_jD_j||_2}$, where $W_i$ and $W_j$ are the CCA projections for data points x and y and $D_i$ and $D_j$ are diagonal matrices whose diagonal elements are given by the p-th power of the corresponding eigenvalues. In the experiments p was fixed to 4.

In the paper, as an example, it is explained how the authors extracted the features from the dataset used.

In the unsupervised scenario, the matrix C is obtained by clustering the tags of the images by using K-means, Normalized cut, Nonnegative matrix factorization ot [[PLSA]]. Since the number of topics is not very high (at least in the experiments described in the paper), the authors used a linear kernel on C with no further dimensionality reduction.

## References
1. [Paper](http://slazebni.cs.illinois.edu/publications/yunchao_cca13.pdf)
2. [Image2Tag, Tag2Image](https://towardsdatascience.com/tag2image-and-image2tag-joint-representations-for-images-and-text-9ad4e5d0d99)

## Code
1. 
