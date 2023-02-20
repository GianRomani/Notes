Created: 2022-05-19 12:51
#note

[[Statistical distance]] for information theory that quantifies how much one probability distribution differs from another.
For discrete probability distributions *P* and *Q* defined on the same probability space *X*, the relative entropy from *Q* to *P* is defined as: $KL(P||Q) = \sum_{x \in X}P(x)\log({\dfrac{P(x)}{Q(x)}})$. The intuition for the KL divergence score is that when the probability for an event from P is large, but the probability for the same event in Q is small, there is a large divergence. When the probability from P is small and the probability from Q is large, there is also a large divergence, but not as large as the first case.

The [Jense-Shannon divergence](https://en.wikipedia.org/wiki/Jensen%E2%80%93Shannon_divergence) is a normalized and symmetrical version of KL divergence. 

## References
1. [Wikipedia](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence)
2. [KL](http://hanj.cs.illinois.edu/cs412/bk3/KL-divergence.pdf)
3. [ML mastery](https://machinelearningmastery.com/divergence-between-probability-distributions/)

## Code
1. 

#### Tags
#metric