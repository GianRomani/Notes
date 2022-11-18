# PinnerSage - Multi-Modal User Embedding Framework for Recommendations at Pinterest
Created: 2022-07-04 09:54
#paper

## Main idea
In this work, the authors postulate that a single embedding is not sufficient for encoding multiple facets of a user’s interests that might have no obvious linkage between them. They can evolve, with some interests persisting long term while others span a short time period. Recommended items are also represented in the same embedding space. A good embedding must encode a user’s multiple tastes, interests, styles, etc., whereas a recommended item (a video, an image, a news article, a house listing, a pin, etc.) typically only has a single focus. Hence it becomes important to represent a user with multiple embeddings, with each embedding capturing a specific aspect of their interest.
To better understand users' preferences, PinnerSage was designed to represents eac user with mutiple embeddings. This is achieved by clustering users' actions into conceptually coherent clusters with the help of a hierarchical clustering method (Ward) and then by summarizing the clusters via representative pins (Medoids) for efficiency and interpretability.

## In deep
Main aspects:
1. Pin Embeddings are fixed -> learning user and item embeddings jointly can lead to side-effects (e.g. the mean of several interests could not be really interesting to the user, i.e. we want to recommend only items that are similar to the ones the user interacted with);
2. No restriction on number of embeddings -> a user can be represented by as many embeddings as their underlying data. This is achieved thanks to [Ward](https://en.wikipedia.org/wiki/Ward%27s_method) algorithm;
3. Medoids based representation of clusters -> medoids are used because their usage avoids topic-drift and is robust to outliers;
4. Medoid sampling for candidate retrieval -> it would be too heavy to use all the medoids simultaneously and the user would be bombarded with too many different items, so 3 medoids are chosen proportional to their importance scores and then their nearest neighboring pinsa are recommended. The importance of medoids is updated daily;
5. Two-pronged approach for handling realtime updates -> medoids are infered based on their long-term and short-term preferences;
6. Approximate nearest neighbor system -> approximate nearest neighbor is used to get the k pins closest to the query (medoid).

**Notations**: $P={P_1,P_2,...}$ is the set of pins at Pinterest and $P_i \in R^d$ is the d-dimensional PinSage embedding of the i-th pin. $A_u={a_1,a_2,...}$ is the sequence of action pins (repinned, clicked) of user u on pin $P_a$ at time $T_u[a]$. $A_u$ is sorted on action time.

The goal is to infer multiple embeddings for each user, $E={e_1,e_2,...}$, where $e_i \in R^d$ for all *i*, given  user's actions *A* and pins embeddings *P*. The number of embeddings to be retrieved can be different among users.

The approach has three components:
1. Cluster of pins;
2. Medoid representation of each cluster;
3. Compute importance score of each cluster to the user.

### Step 1: Clustering
Tha algorithm used is [Ward](https://en.wikipedia.org/wiki/Ward%27s_method), which is a hierarchical agglomerative clustering method based on minimum variance criteria that automatically determine the number of clusters. The implementation used is based on the Lance-Williams algorithm.
![[PinnerSage_clustering.PNG]]
Given a distance $d_{ij}$ between the clusters $C_i$ and $C_j$, if the two clusters are merged, the distances are updated as follows: $d(C_i \bigcup C_j, C_k)= \dfrac{(n_i+n_k)d_{ik}+(n_j+n_k)d_{jk}-n_k d_{ij}}{n_i + n_j +n_k}$, where $n_i=|C_i|$ is the number of pins in cluster i.
The computational complexity of this algorithm is $O(m^2)$, where $m=|A|^2$.

### Step 2: Medoid cluster representation
The goal of this step consists in representing in a compact way each cluster. That are several approaches that could have been chosen, but most of them could generate embeddins that lie in a very different region in the d-dimensional space. Medoid, instead, avoid this problem. The pin that minimizes the sum of squared distances with the other cluster members is elected as medoid. Another benefit of medoid is that only the index of the medoid pin has to be stored, instead of the whole embedding.

### Step 3: Cluster importance
The number of clusters for a user can be in order of tens to few hundreds. It is important to identify the importance of clusters to user to sample them. For this purpose a time decay average model is used: $Importance(C,\lambda)=\sum_{i \in C}e^{-\lambda(T_{now}-T[i])}$, where T[i] is the time of action on pin i by the user. A cluster that has been interacted with frequently and recently will have higher importance than others. Setting $\lambda=0$ puts more emphasis on the frequent interests of the user, whereas $\lambda=0.1$ puts more emphasis on the recent interests of the user. 
![[PinnerSage_algorithm.PNG]]
Since the model operates independently for each user, it can be implemented using MapReduce.
The outputs from the online and the batch version of PinnerSage are combined together and used to generate the recommendations.


### Other details
As embedding indexing scheme, HSNW is the one that performed better on cost, latency and recall.
Near duplicates and lower quality pins are filtered using some specialized models.
As already said, to reduce the cost to retrieve pins, instead of refering to the embedding itself, the queries to the ANN system refer to the id of the medoids.

## References
1. [Paper](https://arxiv.org/pdf/2007.03634.pdf)
2. [Medium](https://medium.com/pinterest-engineering/pinnersage-multi-modal-user-embedding-framework-for-recommendations-at-pinterest-bfd116b49475)

## Code
1. 
