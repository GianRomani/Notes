# Today's agenda
Created: 2022-03-30 11:20


# Goals / agenda
1. Implement method \#2 for the RS -> recommend posts of users that have posted similar things; 

# Thoughts 
- Cluster of users based on their posts -> recommend posts from users in the same cluster;
- Cluster of posts -> use [[Cluster Consensus]] to define most similar users;
- hierarchical clustering -> most similar posts to the latest one made by the user

# Action items
- [ ] Start from [[Cluster Consensus]] -> how to cluster posts?
	- [ ] Check professor code;
	- [ ] Tf-Idf or Word2Vec (if word2vec consider the average for a post);
	- [ ] k-means;
	- [ ] Use also other [[Ideas#Ideas for Posts]]?
- [ ] For each user count the number of her posts in each cluster;
- [ ] similarity of users is given by the number of common partition they happear in:
	- [ ]  Intersection over union -> number of posts in same cluster divided by the total number of posts made by both users;
- [ ]  which posts recommend from the most similar user?
	- [ ]  start from the ones in the cluster which has more posts in common

