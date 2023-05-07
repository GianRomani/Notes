Created: 2022-12-20 16:38
#note

Invented by Geoffrey Hinton, a Restricted Boltzmann machine is an algorithm useful for dimensionality reduction, classification, regression, collaborative filtering, feature learning and topic modelling.
RBMs are shallow, two-layer neural nets that constitute the building blocks of _deep-belief networks_. The first layer of the RBM is called the visible, or input, layer, and the second is the hidden layer. 
**Note:** While RBMs are occasionally used, most practitioners in the machine-learning community have deprecated them in favour of generative adversarial networks or variational autoencoders. 

A hidden node's result is computed by multiplying each input by a separate weight, summing such products, adding a bias and the by passing the result through an activation layer.

Since inputs from all visible nodes are being passed to all hidden nodes, an RBM can be defined as a symmetrical bipartite graph.

Training is obtained thanks to backward passes, during which the model tries to reconstruct the inputs. To measure the distance between its estimated probability distribution and the ground truth distribution of the input, RBMs use [[Kullback-Leibler divergence]].

An RBM model, combined with a [[Collaborative filtering]] one, won the [Netflix Prize](https://en.wikipedia.org/wiki/Netflix_Prize).

## References
1. [RBM guide](https://wiki.pathmind.com/restricted-boltzmann-machine)
2. [RBM for collaborative filtering](https://dl.acm.org/doi/10.1145/1273496.1273596)
3. [LInkedin course on RecSys](https://www.linkedin.com/learning/building-recommender-systems-with-machine-learning-and-ai/restricted-boltzmann-machines-rbms?autoSkip=true&autoplay=true&resume=false)
4. [Recommender system with DL methods](https://medium.com/sciforce/deep-learning-based-recommender-systems-b61a5ddd5456)

## Code
1. 

#### Tags
#dl