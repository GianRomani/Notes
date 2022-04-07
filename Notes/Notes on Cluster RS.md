# Notes on RS
Created: 2022-03-31 15:36

How to build clusters:
1. just use all the posts and the features;
2. divide by category and then cluster for each of them -> I have to weight both the common category and the common cluster. 

[[Cluster Consensus]]
Two approaches (once I have the clusters):
- similarity based on the likes of the users -> they are similar if they liked posts that are in the same clusters;
- similarity based on the posts made -> users are similar if their posts are in the same clusters

In both cases I can compute the similarity weighted by the scores of the target user on the clusters -> Ex.: user A has \[3,2,1\] posts in the clusters, user B \[2,3,1\] and user C \[3,1,2\]. If user A is the target, both B and a C have a distance of 2 from A, but B differ from A in the most important cluster for him -> C is more similar to A. I could use some form of [Cumulative Gain](https://machinelearningmedium.com/2017/07/24/discounted-cumulative-gain/).

Once I have the ranked list of similar users, choose the posts in one of the following ways:
-  Consider posts with more likes;
-  Consider posts that most similar users like

How to rank the posts?
1. consider timestamp for the likes;
2. consider from which cluster they come;
3. consider just the ranking of the users

I could also weight the categories or the cluster that are more used -> cluster 0 is generally the most populated, so similarity on this cluster should be less important than another one.


## References
1. 

## Code
1. 

#### Tags