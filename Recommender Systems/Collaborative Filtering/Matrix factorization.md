# Matrix factorization
Created: 2022-04-25 11:25
#note

It consists in a representation of user-item as a vector of latent features which are projected into a shared feature space. User-item interactions are modeled using inner product of user-item latent vectors.
It can be enhanced by integrating it with neighbour based models, by combining it with topic models of item content and by extending it to factorization machines for general modeling of features.
Performance can be improved by incorporating user-item bias terms into the interaction function -> to capture the complex structure of user interaction data we need something more than inner product.

Mathematical speaking, MF is represented as: $\hat{y}_{ui}=f(u,i|p_u,q_i)=p_u^Tq_i=\sum_{k=1}^{K}p_{uk}q_{ik}$, where $p_u$ is the latent vector for user *u*, $q_i$ is the latent vector for item *i*, $K$ is the dimension of the latent space. 

A limitation of MF approach is show in the following image:
![[matrix_factorization.png|Let us first focus on the first three rows (users) in the figure. It is easy to have s23(0.66) > s12(0.5) > s13(0.4). As such, the geometric relations of p1, p2, and p3 in the latent space can be plotted as in Figure 1b. Now, let us consider a new user u4, whose input is given as the dashed line in Figure 1a. We can have s41(0.6) > s43(0.4) > s42(0.2), meaning that u4 is most similar to u1, followed by u3, and lastly u2. However, if an MF model places p4 closest to p1 (the two options are shown in Figure 1b with dashed lines), it will result in p4 closer to p2 than p3, which unfortunately will incur a large ranking loss.]]

## References
1. [Toward Data Science](https://towardsdatascience.com/recommendation-system-matrix-factorization-d61978660b4b)
2. [Google developers](https://developers.google.com/machine-learning/recommendation/collaborative/matrix)

## Code
1. 

#### Tags
#matrix_factorization 