# Notes on Cluster RS
Created: 2022-03-31 15:36
#note 

How to build clusters:
1. just use all the posts and the features;
2. divide by category and then cluster for each of them -> I have to weight both the common category and the common cluster. 

[[Cluster Consensus]]
### Approaches
Two approaches (once I have the clusters):
- similarity based on the likes of the users -> they are similar if they liked posts that are in the same clusters;
- similarity based on the posts made -> users are similar if their posts are in the same clusters

In both cases I can compute the similarity weighted by the scores of the target user on the clusters -> Ex.: user A has \[3,2,1\] posts in the clusters, user B \[2,3,1\] and user C \[3,1,2\]. If user A is the target, both B and a C have a distance of 2 from A, but B differ from A in the most important cluster for him -> C is more similar to A. I could take inspiration from [Cumulative Gain](https://machinelearningmedium.com/2017/07/24/discounted-cumulative-gain/).

Once I have the ranked list of similar users, choose the posts in one of the following ways:
-  Consider posts with more likes;
-  Consider posts that most similar users like

How to rank the posts?
1. consider timestamp for the likes;
2. consider from which cluster they come;
3. consider just the ranking of the users

I could also weight the categories or the cluster that are more used -> cluster 0 is generally the most populated, so similarity on this cluster should be less important than another one.

Types of recommendation:
- Cluster on likes and recommendation based on users' likes -> OK but target and user could have given like to same posts
- Cluster on posts and recommendation on most liked posts -> target posts a certain kind of posts, then recommend similar posts

### Problems:
1. most of the clusters are in cluster 0 (this happen for every category) -> weight the cluster distance, small distances in other clusters are significative;
2. distance between a user that have posted a lot and one that posted few things is great, even if they have similar tastes -> instead I should show users that posts a lot (their content should be better);
3. how to rank the recommendations?

1) can be fixed as I did with the categories, but inverted:
	1) divide by the number of posts in the cluster;
	2) DCG by inverting ranking (cluster with less posts is the first);

2) weight number of posts:
	1) for each category compute the clusters' distance, then divide the obtained value by the total number of posts in the category

3) I should not show just the posts from the first ranked user, then the second and so on:
	1) use ranking of users and the distance from target to distribute the posts;
	2) consider from which clusters the posts are coming


Data has a lot of noise -> clusters are not really good, i.e. most of the data belongs to few clusters and there are lots of outliers.

### Ranking

**Problems with ranking**:
-	ranking on number of likes on recommended users' posts:
	-	to have a global ordering use a weight -> divide by the log of user's ranking;
	-	most of the posts have few likes -> similar scores;
	-	some posts with few likes can be good recommendations + newer posts have fewer likes;
	-	this approach could be good to recommend new things to users, because it could also show posts that are not very similar to the posts made from the target until now, but they are still relevant because they were made by similar uses;
-	ranking on posts liked by the recommended users:
	-	get a list of recommended users that liked a post and compute a score using such list;
	-	get fewer recommeded users (5 maybe?) and just show all the liked posts ordered by the number of likes;
	-	some problems as above with the small number of likes posts have  
-	ranking based on ranking of user, cluster, category and likes of the posts 

In [[Collaborative filtering]] we search the most similar users and then we recommend items based on their ratings -> How can I transpose this concept in my case?
Ratings = likes -> recommend posts that similar users liked (weighted by the rank of the user, number of post's likes, cluster of the post and when the posts was posted) but there are few likes in the dataset

### **Transformers**

Using [this](https://huggingface.co/dbmdz/bert-base-italian-cased) model. Texts are too long -> solutions:
- truncate the text, so that the number of tokens is 512;
- divide text in chunks, use transformer on each of them and then average the results -> better results but too slow (4-5 hours);
- use [this](https://arxiv.org/ftp/arxiv/papers/2104/2104.07225.pdf) idea ([here](https://github.com/krzysztoffiok/TextGuide) the code) and its revisitation ([here](https://www.mdpi.com/2076-3417/11/18/8554/htm)).


## References
1. 

## Code
1. 

#### Tags