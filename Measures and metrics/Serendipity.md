It is related to lucky findings or satisfying surprises. There are two kinds of metrics for serendipity:
1. Primitive recommender based: a first metric is given by: $ser(R_u) = \sum_{k=1}^{|R_u|}max(R_u[k] - PM_u[k],0)rel(i_k)\dfrac{count_k(k)}{k}$, where PM is the primitive recommender and *rel* is a function that calculates if the predicted items are relevant to the user or not. This other metric uses $UNEXP_u = R_u - PM_u$, which represents the surprising items for the user *u*, but not the ranking of the items : $ser(R_u) = \dfrac{\sum_{i \in UNEXP_u}utility(i)}{|R_u|}$. A third metric is: $ser(R_u)= \dfrac{(R_u - E_u) \cap USEFUL_u}{|R_u|}$ where *USEFUL* is the set of useful items and *E* is the set of expected items.
2. Non primitive recommender based: one metric used is the following: $ser(R_u)= \dfrac{1}{|H_u|} \sum_{i \in H_u} \sum{j \in R_u} \dfrac{cossim(i,j)}{|R_u|}$, where we are considering the cosine similarity between the recommended items and the history of consumption of the user (*H*). This metric does not consider the usefulness of the recommendations.

The first group of metrics is really sensitive to the choice of the primitive recommender -> the second group could be useful if associated with metrics that consider usefulness of recommended items.

# Tags
#recsys 