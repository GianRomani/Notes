Created: 2022-05-09 12:13
#paper

A major problem with classic topic model methods is that any change to the topic model requires mathematically deriving a new inference algorithm. Autoencoding variational inference for topic model (AVITM) tackles this problems and matches traditional methods in accuracy with much better inference time.
It is an evolution of Autoencoding variational Bayes ([AEVB](https://arxiv.org/pdf/1401.4082.pdf)), which is a neural network that directly maps a document to an approximate posterior distribution, without the need to run further variational updates (that implicates that a small change in the document will produce only a small change in topics). AEVB has several problems: the Dirichlet prior is not a location scale family and the problem of component collapsing (i.e. inference network becomes stuck in a bad local optimum). AVITM has not the problems that AEVB had and furthermore is a black-box method that can be easily applied to new models. To show this last property, the authors present the topic model ProdLDA which produces consistently better topics than standard [[LDA]] (in much less time).

## References
1. [Paper](https://arxiv.org/pdf/1703.01488.pdf)

## Code
1. 
