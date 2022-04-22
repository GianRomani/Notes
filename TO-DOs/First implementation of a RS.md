# First implementation of a RS
Created: 2022-03-30 11:20
#agenda

# Goals
Implement method \#2 for the RS -> recommend posts of users that have posted similar things; 

# Thoughts 
- Cluster of users based on their posts -> recommend posts from users in the same cluster;
- Cluster of posts -> use [[Cluster Consensus]] to define most similar users;
- Each category has a set of clusters;
- Posts belong to a cluster of a category (but it can happen that some posts are assigned to multiple categories);
- Similarity:
	- Given two different users, count the common clusters for each category;
	- normalize the count by the total number of posts made by the users;
	- discount difference for categories that are less important for the target user

# Action items
- [ ] Start from [[Cluster Consensus]] -> how to cluster posts?
	- [x] Check professor code;
	- [x] Tf-Idf;
	- [ ] Word2Vec (consider the average for a post);
	- [x] k-means;
		- [x] compute clusters for each category;
	- [x] Use also other [[Ideas#Ideas for Posts]]?
- [x] For each user count the number of his/her posts in each cluster;
- [x] similarity of users is given by the number of common partition they happear in:
	- [x]  Intersection over union -> number of posts in same cluster divided by the total number of posts made by both users;
- [x]  which posts recommend from the most similar user?
	- [x]  simply recommend posts from most similar users
	- [x]  start from the ones in the cluster which has more posts in common
	- [x]  from the most similar user, recommend posts with more likes
	- [x]  recommend posts that most similar users like
- [x]  Consider the number of posts the user made -> distance of two users that have similar tastes could be great if they have posted a different amount of schede -> use [[Jaccard similarity]] or logarithm on cluster's distance?

