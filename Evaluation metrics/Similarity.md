# Similarity
Created: 2022-03-23 12:24

# Word Embedding-Based similarity
To overcome the absence of semantics in the traditional similarity measures
available in the state of the art, one can resort to the use of word embeddings to capture conceptual relationships between words. In the word embedding spaces, the vector representations of the words appearing in similar contexts tend to be close to each other. We can therefore exploit the nature of word embeddings and define new metrics to estimate how much two topic descriptors are similar.

## Word Embedding-Based Centroid Similarity (WECS). 
The most simple strategy, originally designed for a cross-lingual task, consists of computing the centroids of two topic descriptors $t_i$ and $t_j$ and then estimating their similarity. Let be $t_i$ the vector centroid of the topic descriptor $t_i$ computed as the average of word embeddings considering all the words belonging to the topic i.
The Word Embedding-based Centroid Similarity between two topics is estimated as $WECS(t_i, t_j ) = sim(t_i, t_j )$, where sim is a measure of similarity
between vectors, i.e. cosine similarity.

## Word Embedding-Based Pairwise Similarity (WEPS). 
An alternative to WECS consists of averaging the pairwise similarity between the embedding vectors of the words composing the topic descriptors. We define the similarity between two topic descriptors $t_i$ and $t_j$ as follows:
$WEPS(t_i, t_j)= \dfrac{1}{t^2} \sum_{v \in t_i} \sum_{u \in t_j} sim(w_v,w_u)$ where t represents the number of words of each topic, and $w_v$ and $w_u$ denote the word embeddings associated with words v and u respectively.

## Word Embedding-Based Weighted Sum Similarity (WESS). 
A simple way to combine the probability distributions and the word embeddings is to
compute the sum of the word embeddings of the words in the vocabulary, where
the sum is weighted by the probability of each term in the topic. Then, we compute the similarity between the resulting word embeddings.
More formally, let be $b_i= \sum{v \in V} \beta_i(v) · w_v$ the weighted sum of the word embeddings of the vocabulary for the topic i. Therefore, the WESS for the topic i and j is defined as $sim(b_i, b_j)$.

## Word Embedding-Based Ranked-Biased Overlap (WERBO). 
We can extend RBO and define a new metric of similarity that is top-weighted and
makes use of word embeddings. Given the lists l1 = {cat, animal, dog} and l2 = {animal, kitten, animals}, the words cat and kitten are similar, even though they are lexicographically different. It follows that their overlap at depth 2 should be higher than 1. We therefore generalize the concept of overlap to handle word embeddings instead of simple word tokens.

## References
1. [RBO](https://dl.acm.org/doi/pdf/10.1145/1852102.1852106?casa_token=oKu_SItzVa0AAAAA:HCtnFDz99wg9XYDz-_3HLlXkEIkZMivH4w6BxJdm-Hqd0vxuPTiIg8YTMsWyjnGdiu91Yvlu)
2. [RBO and other metrics](https://link.springer.com/content/pdf/10.1007/978-3-030-80599-9.pdf)
3. [Article](https://www.sciencedirect.com/science/article/pii/S0950705113001044#b0940)
4. [Basic similarity measures](http://ijetsr.com/images/short_pdf/1498555415_619-626-ieteh326_ijetsr.pdf)

## Code
1. [OCTIS](https://github.com/mind-Lab/octis)

#### Tags
#similarity
