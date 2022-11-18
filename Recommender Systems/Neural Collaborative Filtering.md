# Neural Collaborative Filtering
Created: 2022-03-24 12:03
#paper

## Main idea
[[Multilayer Perceptron]] Technique based on #neural_network  to tackle [[Collaborative filtering]] 's problems on basis of implicit feedback.
To improve performances pairwise ranking loss can be used.

One of the most used variation of Collaborative filtering is [[Matrix factorization]], which uses a fixed inner product of the user-item matrix to learn user-item interactions. NCF replaces the inner product with a neural architecture to generalize Matrix factorization. In particular it uses [[Multilayer Perceptron]] as MLP can (theoretically) learn any continuous function thanks to a high level of nonlinearities.

It is generally used with #implicit_data (but it can also be used with explicit data).

## In deep

![[NCF_layers.png]]

From the image above:
1. Input is divided into two sparse vectors, one to identify the user and the other one that tells us if the user *u* has interacted with item *i*;
2. The embedding layer is a fully connected layer that project the sparse representation into a dense one;
3. Neural CF layers: MLP that maps the latent vectors to prediction scores;
4. Final output layer that returns the predicted score by minimizing the loss.

User-item interaction is modeled by the following formula: $\hat{y}_{ui}=f(P^Tv_u^U,Q^Tv_i^I|P,Q,\theta_f)$, where P is the latent factor matrix for users (of dimension K), Q is the latent factor matrix for items (of dimension K) and $\theta_f$ represents the model parameters.

The pointwise squared loss ([[Losses]]) is represented as $L_{sqr}=\sum_{(u,i)\in O\cup O^-}w_{ui}(y_{ui}-\hat{y}_{ui})^2$, where $O$ is the set of observed interaction in Y, $O^-$ are the samples of unobserved interactions, $w_{ui}$ is the weight of the training instance.

Since we need a probabilistic approach for learning the pointwise NFC, the likelihood function is defined as: $\hat{y}_{ui}=f(P^Tv_u^U,Q^Tv_i^I|P,Q,\theta_f) = \prod_{(u,i)\in Y}\hat{y}_{u,i} \prod_{(u,j)\in Y^{-}}(1-\hat{y}_{uj})$. That we need to take the negative log of the likelihood function $L=-\sum_{(u,i)\in O} \log (\hat{y}_{ui}) - \sum_{(u,j) \in O^{-}} \log(1-\hat{y}_{uj})$ which is simply the cross entropy loss.

### Generalized Matrix Factorization (GMF)
The predicted output of the NCF can be expressed as $\hat{y}_{ui}=a_{out}(h^T(p_u \otimes q_i))$, where $a_{out}$ is an activation function and $h$ are the edge weights of the output layer.
By playing with this two parameters we obtain several variations of GMF, as shown in the following table: ![[NCF_GMF.png]]The one used in NCF is the last one with sigmoid as activation function.

### MLP
NCF is considered as a multimodal DL method as it contains data of two kinds (users and items). To combine data we use a concatenation plus hidden layers on top of it.
ReLU is used as activation function.

## NeuMF
Recap:
1. GMF applies a linear kernel to model user-item interactions;
2. MLP uses MLP to layer nonlinear interactions.

The output of these two parts are concatenated and then fed into a NeuMF layer.

![[NCF.png]]

In more details:
1.  GMF/MLP have separate user and item embeddings. This is to make sure that both of them learn optimal embeddings independently.
2.  GMF replicates the vanilla MF by element-wise product of the user-item vector.
3.  MLP takes the concatenation of user-item latent vectors as input.
4.  The outputs of GMF and MLP are concatenated in the final NeuMF(Neural Matrix Factorisation) layer.

The score function is then modeled as follows: $\phi^{GMF}=p_u^G \otimes q_i^G$, $\phi^{MLP}=a_L(W^T_L(a_{L-1}(\cdots a_2(W^T_2 
\left[ \begin{array}{c}
    p_u^M \\
	q_i^M
       \end{array} \right] 
+b_2
)\cdots))+b_L)$,
$\hat{y}_{ui}= \sigma(\left [\begin{array}{c}\phi^{GMF}\\ \phi^{MLP}\end{array}\right])$,

G:GMF, M:MLP, p:User embedding, q:Item embedding
Due to the non-convex objective function of NeuMF,gradient-based optimization methods can only find locally-optimal solutions. This could be solved by good weight initializations, using random initialisation or from "scratch" (using Adam).

## References
1. [Paper](https://arxiv.org/pdf/1708.05031.pdf)
2. [Towards Data Science](https://towardsdatascience.com/neural-collaborative-filtering-96cef1009401)


## Code
1. [Official GitHub](https://github.com/hexiangnan/neural_collaborative_filtering)
2. [Example](https://towardsdatascience.com/modern-recommendation-systems-with-neural-networks-3cc06a6ded2c)
3. [Pytorch](https://github.com/yihong-chen/neural-collaborative-filtering)

#### Tags
#mlp #neural_collaborative_filtering #ncf  #implicit_data #matrix_factorization 