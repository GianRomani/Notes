# Topic diversity
Created: 2022-09-15 12:38
#note

# RBO (Ranked-Biased Overlap)
RBO is based on the concept of overlap at depth h between two lists, which is the number of elements that the lists share when only the first h words are considered. For example, the overlap at depth 2 between the lists l1 = {cat, animal, dog} and l2 = {animal, kitten, animals} is 1. The average overlap is defined as the proportion of the overlap at depth h over h. Therefore, the RBO measure when evaluating two topics is computed as the expected value of the average overlap that the user observes when comparing two lists.
# Inversed RBO
We define $\rho$ as the reciprocal of the standard RBO. RBO compares the 10-top words of two topics. It allows disjointedness between the lists of topics (i.e., two topics can have different words in them) and uses weighted ranking. I.e., two lists that share some of the same words, albeit at different rankings, are penalized less than two lists that share the same words at the highest ranks. $\rho$ is 0 for identical topics and 1 for completely different topics.

## References
1. [RBO](https://dl.acm.org/doi/pdf/10.1145/1852102.1852106?casa_token=oKu_SItzVa0AAAAA:HCtnFDz99wg9XYDz-_3HLlXkEIkZMivH4w6BxJdm-Hqd0vxuPTiIg8YTMsWyjnGdiu91Yvlu)
2. [RBO and other metrics](https://link.springer.com/content/pdf/10.1007/978-3-030-80599-9.pdf)

## Code
1. [GitHub TD](https://github.com/silviatti/topic-model-diversity#irbo)
2. [OCTIS](https://github.com/mind-Lab/octis)

#### Tags