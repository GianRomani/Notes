# kNN
Created: 2022-03-23 11:35

[[Collaborative filtering]] method based on [[Similarity]] measures.
Simple and quite accurate, but suffers of low scalability and has problems in case of sparse databases -> not good for [[Cold-start]].

User to user approach:
1. using the selected similarity measure, we produce a set of *k* nearest neighbors for the user;
2. aggregation phase: compute the average (or weighted sum) on item *i*;
3. take the best *n* items

Item to item approach:
1. produce the *k* items that are neighbors for each item in the database;
2. for each item *i* not rated by user *a*, compute its prediction using the ratings of *a* of the *k* neighbors of *i*;
3. select the top *n* recommenddations.

The two approaches (item-item and user-user) can be combined ([paper](https://www.researchgate.net/publication/221299518_Unifying_user-based_and_item-based_collaborative_filtering_approaches_by_similarity_fusion))

## References
1. https://www.sciencedirect.com/science/article/pii/S0950705113001044


#### Tags
#knn