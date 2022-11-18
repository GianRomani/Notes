# Collaborative Topic Modeling
Created: 2022-05-03 10:41
#paper

## Main idea

Collaborative Topic Modeling (CTM) is a recommender system for text-based items buildt upon Probabilistic Matrix Factorization (PMF) and [[LDA]].

CTM is superior compared to PMF approach because it is able to do out-of-matrix predictions, i.e. it can derive latent vector of qualities for unrated items.

## In deep

A latent qualities vector for a document *i*, $Q_i$ is represented as: $Q_i=\theta_i+\epsilon_i$, where $\theta_i$ is the (Kx1) vector of topic proportions for item *i* obtained from traditional LDA estimates, and $\epsilon_i$ is a (Kx1) offset vector that adjust topic proportions by considering ratings. 

The generative process for CTm is shown in the following image:
![[CTM_algorithm.png]]

Where $\sigma^2_P$ and $\sigma^2_Q$ represent the variance we impose a priori on the distribution of the elements of the vectors in P and Q. Similarly, $\sigma^2_u$ represents the variance we impose a priori on the distribution of the ratings. $Dir(\alpha)$ is the [Dirichlet](https://en.wikipedia.org/wiki/Dirichlet_distribution) distribution.

So we are interested into learning the paramenters $\theta_i$, $Q_i$ and $P_u$. We can do this using Maximum Likelihood, where the likelihood od our data is defined as: $p(P,Q,\theta, R|\sigma_P,\sigma_Q,\sigma, \beta,\alpha)=p(P|\sigma^2_P)p(Q|\theta,\sigma^2_Q)p(\theta,w|\alpha,\beta)p(R|P,Q,\sigma^2)$

As often happen, it is more convenient to work with the log-likelihood. 
By working on each component independently:

**First Component**:
![[CTM_log1.png]]

**Second Component**:
![[CTM_log2.png]]

**Third Component**:
![[CTM_log3.1.png]]
That, after imposing $\alpha=1$ for convenience, becomes:
![[CTM_log3.2.png]]

**Fourth Component**:
![[CTM_log4.png]]

Then, by riassemblying everything:
![[CTM_final_log.png]]

To estimate the parameters, we obtaine $\theta$ using standard LDA and then optimize for [P, Q] via gradient ascent (originally in the paper  they used [Coordinate Ascent](https://en.wikipedia.org/wiki/Coordinate_descent) method for optimization, but this is computationally heavier).
The gradient of the log-likelihood with respect to [P,Q] is:
![[CTM_gradient.png]]

## References
1. [Paper](http://www.cs.columbia.edu/~blei/papers/WangBlei2011.pdf)
2. [TowardsDataScience](https://towardsdatascience.com/a-guide-to-collaborative-topic-modeling-recommender-systems-49fd576cc871)
3. [Probabilistic Matrix Factorization](https://towardsdatascience.com/probabilistic-matrix-factorization-b7852244a321)
4. [LDA](https://towardsdatascience.com/light-on-math-machine-learning-intuitive-guide-to-latent-dirichlet-allocation-437c81220158)

## Code
1. 
