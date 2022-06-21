# Evaluate Clustering
Created: 2022-04-29 15:26
#note

We need metrics that work when the truth labels are not known.


### External validation
The methods used to implement this measure need ground truths.
Examples:
- Measures based on matching:
	- Purity: Cluster $C_i$ contains points only from one ground truth partition;
	- Maximum matching: based on the assumption that only one cluster can match one partition, in this case pairwise matching is used, i.e. one element belongs to only one cluster;
	- F-measures: Precision, Recall;
- Entropy measures: it represents the amount of orderness of the information in all the partitions -> $H(C)=-\sum_{i=1}^r PC_i\log PC_i$, where $PC_i =\dfrac{n_i}{n}$. Some examples are:
	- Conditional entropy: given that $PC_i$ represents the probability of cluster $C_i$, the entropy of partitioning *T* for ground truth *j* for k groups is given by $H(T)=-\sum_{j=1}^k PT_i\log PT_j$. Then the entropy of *T* w.r.t. cluster $C_i$ (how ground truths are distributed among each cluster) is represented by $H(T|C_i)=-\sum_{j=1}^r (\dfrac{n_{ij}}{n_i})\log(\dfrac{n_{ij}}{n_i})$ and *T*'s conditional entropy with respect to C clustering: $H(T|C)=-\sum_{i=1}^r (\dfrac{n_i}{n})H(T|C_i)$;
	- Normalized [[Mutual Information]];
- Pairwise measures -> TN, TP, FN, FP, Jaccard coefficient, Rand statistic ((TP+TN)/N) and Fowlkes Mallow measure (geometric mean of precision and recall).

### Internal measures
Ground truths are not needed, based on the ideas of intra-cluster compactness and inter-cluster separation.
Let's define $W(S,R)$ as the summation of weights on all edges having one vertex in cluster S and other vertex in cluster R. 
The summation of overall intra-cluster weights over the clusters is: $W_{in}=\dfrac{1}{2} \sum_{i=1}^k W(C_i, C_i)$.
The summation of all the inter-clusters weights is: $W_{out}=\sum_{i=1}^{k-1}\sum_{j>1}W(C_i,C_j)$.
The number of distinct intra-cluster edges is given by: $N_{in}=\sum_{i=1}^k(2^{n_i})$.
The number of distinct inter cluster edges is given by: $N_{out}=\sum_{i=1}^{k-1}\sum_{j=i+1}^{k}n_i n_j$.
Some measures are:
- Beta-CV measure: it is the ratio of the average intra-cluster distance to the average inter-cluster distance. The smaller the clustering, the better it is. $Beta CV=\dfrac{W_{in}/N_{in}}{W_out/N_{out}}$.
- Normalized cut: $N_{cut}(A,B) = cut(A,B)(\dfrac{1}{vol(A)}+\dfrac{1}{vol(B)})$, where $vol(A)=\sum_{i \in A}d_i$, $cut(X,Y)=\sum_{i \in A, j \in B}W_{ij}$ where X and Y are sets that divide a graph, the weight of edges connecting vertices in X to Y is minimum, the size of X and Y is very similar and $W_{ij}$ control the neighborhood (and it is equal to $e^{\dfrac{|x_i=x_j|^2}{2\sigma ^ 2}}$). The higher the normalized cut, the better the clustering.

### Relative measures
Used to compare disparate clustering usually obtained from the same algorithm changed in some parameters.
Silhouette Coefficient is the most used (it can be also considered as internal measure):
Silhouette coefficient as internal measure -> it checks cluster cohesion and separation. For each point $x_i$ its score $s_i$ is defined as: $s_i=\dfrac{\mu_{out}^{min}(x_i)- \mu_{in}(x_i)}{max\{\mu_{out}^{min}(x_i),\mu_{in}(x_i)\}}$, where $\mu_{in}(x_i)$ is the mean distance measure from $x_i$ to points in it closest cluster and $\mu_{out}^{min}$ is the mean distance measure from $x_i$ to points in its closest cluster. Then the Silohouette Coefficient is the mean value of s_i across all the points. We have a good cluster for a score close to +1.


### Improve Diversity

Greedy algorithm: https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.8.5232&rep=rep1&type=pdf

[ClusDiv](https://akademik.bahcesehir.edu.tr/~tevfik/papers/diversity.pdf) algorithm

### Improve reliability

### User interest change over time

### Data sparsity
To asses similarity between users in case of a sparse matrix, use clustering, dimensionality reduction or advanced similarity measures
[Bi-clustering](https://link.springer.com/article/10.1007/s00521-018-3959-2)

### Consistency

### Other metrics
From [this](https://arxiv.org/pdf/2010.12626.pdf) paper.

**Word Entropy**: to evaluate the specificity of a topic, we measure a topic's word diversity using the conditional entropy of word types given a topic: $-\sum_i Pr(w_i|z)\log Pr(w_i|z)$. Topics composed of tokens from a small set of types will have low entropy, while topics more evenly spread out across the whole vocabulary will have high entropy. Extreme entropy scores indicate bad topics, extremely low entropy are overly specialized, while those with extremely high entropy are overly general.
**Coherence**: to measure the semantic quality of a topic using two word-cooccurrence-based coherence metrics -> it measures whether a topic's words actually occur together (in the working collection or an external collection). Internal coherence : $\sum_i \sum_{j<1} \log \dfrac{D(w_i,w_j)+ \epsilon}{D(w_i)}$, where *D* refers to the number of documents that contain a word or word-pair. External coherence: $\sum_i \sum_{j<1} \log \dfrac{Pr(w_i,w_j)+ \epsilon}{Pr(w_i)Pr(w_j)}$, where the probabilities are estimated from the number of 25-word sliding windows that contain a word or word-pair in an external corpus. Higher scores are better (for both internal and external metrics). Words that do not appear in the external corpus are ignored and topics with less than 10 attested words are skipped (the presence of skipped topics ia an indicator of model failure).
**Exclusivity**: a topic model can reach high coherence by repeating a single high-quality topic multiple times, so we can define a metric that consider how exclusive a word *w* is to a specific topic *z*: $\dfrac{Pr(w_i|z)}{\sum_{z'} Pr(w_i|z')}$. A word prelevant in many topics will have a low exclusivity score near 0, while a word occurring in a few topics will have a score near 1.
## References
1. [Review-Clustering of high dimensional data](https://dl.acm.org/doi/pdf/10.1145/3132088)

## Code
1. [Sklearn](https://scikit-learn.org/stable/modules/clustering.html#clustering-performance-evaluation)

#### Tags
#clustering 