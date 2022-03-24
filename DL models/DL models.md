# DL models
Created: 2022-03-23 12:53

Pros:
- they can deal with non linear transformations;
- good for sequence modeling, next basket recommendation or session based recommendations (for example #click-logs);
- representation learning [[Autoencoder]][[Restricted Boltzmann machine(RBM)]];
- easier to build hybrid systems

Cons:
- interpretability -> black boxes;
- they need a big amount of data;
- hyperparameter tuning can take longer time;

Types:
- [[Multilayer Perceptron]] (MLP) -> feed-forward neural network with multiple hidden layers, i.e. stacked layers of nonlinear transformations;
- [[CNN]] can capture global and local features, good for grid-like data;
- [[RNN]] for sequential data;
- [[Autoencoder]] are unsupervised models that use bottleneck layer to learn salient features;
- [[Restricted Boltzmann machine(RBM)]]are two layers models (visible and hidden layer);
- [[Neural attention]]that use attention mechanism;
- [[Neural Autoregressive Distribution Estimation]] (NADE) are unsupervised neural networks built on top of a autoregressive model and feedforward neural networks;
- [[Adversarial Networks]] (AN) consist of a discriminator and a generator which compete against each other;
- [[Deep Reinforcement Learninig]] (DRL) operate on a trial-and-error paradigm;
- [[Transformer]] for sequential and session-based recommendation

Obviously a DL-based RecSys can use just one DL model or a combination of several DL models ( #deep_hybrid_models ). 
Some combinations of models that have been proved to be effective are:
- CNN + Autoencoder;
- CNN + RNN;
- RNN + Autoencoder;
- Rnn + DRL


## References
1. https://arxiv.org/pdf/1707.07435.pdf
2. https://medium.com/sciforce/deep-learning-based-recommender-systems-b61a5ddd5456

## Code
1. https://github.com/microsoft/recommenders
2. https://github.com/PaddlePaddle/PaddleRec/blob/master/README_EN.md

#### Tags
#dl #rnn #cnn #mlp #rbm #drl #nade #autoencoder #an #neural_attention #transformer 