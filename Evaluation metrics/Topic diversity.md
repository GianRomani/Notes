# Topic diversity
Created: 2022-09-15 12:38
#note

# RBO (Ranked-Biased Overlap)
RBO is based on the concept of overlap at depth h between two lists, which is the number of elements that the lists share when only the first h words are considered. For example, the overlap at depth 2 between the lists l1 = {cat, animal, dog} and l2 = {animal, kitten, animals} is 1. The average overlap is defined as the proportion of the overlap at depth h over h. Therefore, the RBO measure when evaluating two topics is computed as the expected value of the average overlap that the user observes when comparing two lists.
# Inversed RBO
We define $\rho$ as the reciprocal of the standard RBO. RBO compares the 10-top words of two topics. It allows disjointedness between the lists of topics (i.e., two topics can have different words in them) and uses weighted ranking. I.e., two lists that share some of the same words, albeit at different rankings, are penalized less than two lists that share the same words at the highest ranks. $\rho$ is 0 for identical topics and 1 for completely different topics.

# Word Embedding-Based similarity
To overcome the absence of semantics in the traditional similarity measures
available in the state of the art, one can resort to the use of word embeddings to capture conceptual relationships between words. In the word embedding spaces, the vector representations of the words appearing in similar contexts tend to be close to each other. We can therefore exploit the nature of word embeddings and define new metrics to estimate how much two topic descriptors are similar.

## Word Embedding-Based Centroid Similarity (WECS). 
The most simple strategy, originally designed for a cross-lingual task, consists of computing the centroids of two topic descriptors ti and tj and then estimating their similarity. Let be ti the vector centroid of the topic descriptor ti computed as the average of word embeddings considering all the words belonging to the topic i.
The Word Embedding-based Centroid Similarity between two topics is estimated as WECS(ti, tj ) = sim(ti, tj ), where sim is a measure of similarity
between vectors, i.e. cosine similarity.

## Word Embedding-Based Pairwise Similarity (WEPS). 
An alternative to WECS consists of averaging the pairwise similarity between the embedding vectors of the words composing the topic descriptors. We define the similarity between two topic descriptors ti and tj as follows:
$WEPS(t_i, t_j)= \dfrac{1}{t^2} \sum_{v \in t_i} \sum_{u \in t_j} sim(w_v,w_u)$ where t represents the number of words of each topic, and wv and wu denote the word embeddings associated with words v and u respectively.

## Word Embedding-Based Weighted Sum Similarity (WESS). 
A simple way to combine the probability distributions and the word embeddings is to
compute the sum of the word embeddings of the words in the vocabulary, where
the sum is weighted by the probability of each term in the topic. Then, we compute the similarity between the resulting word embeddings.
More formally, let be $b_i= \sum{v \in V} \beta_i(v) · w_v$ the weighted sum of the word embeddings of the vocabulary for the topic i. Therefore, the WESS for the topic i and j is defined as sim(bi, bj).

## Word Embedding-Based Ranked-Biased Overlap (WERBO). 
We can extend RBO and define a new metric of similarity that is top-weighted and
makes use of word embeddings. Given the lists l1 = {cat, animal, dog} and l2 = {animal, kitten, animals}, the words cat and kitten are similar, even though they are lexicographically different. It follows that their overlap at depth 2 should be higher than 1. We therefore generalize the concept of overlap to handle word embeddings instead of simple word tokens.
## References
1. [RBO](https://dl.acm.org/doi/pdf/10.1145/1852102.1852106?casa_token=oKu_SItzVa0AAAAA:HCtnFDz99wg9XYDz-_3HLlXkEIkZMivH4w6BxJdm-Hqd0vxuPTiIg8YTMsWyjnGdiu91Yvlu)
2. [RBO and other metrics](https://link.springer.com/content/pdf/10.1007/978-3-030-80599-9.pdf)

## Code
1. [GitHub TD](https://github.com/silviatti/topic-model-diversity#irbo)
2. [OCTIS](https://github.com/mind-Lab/octis)

#### Tags