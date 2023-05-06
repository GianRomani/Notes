DBSCAN does not work for any method (TF-IDF, embeddings and Declutr) -> all the points are considered as noise.

I tried with several values for $\epsilon$ (from 0.001 to 0.5) and also with small values for the minimum amount of points to form a cluster (<10).

Inter cluster from YellowBrick does not work because there is no cluster_centers_ attribute in Sklelearn DBSCAN.

Calinski Harabasz and Davies Bouldin cannot work since there are not clusters (they need at least 2 clusters, we have just noisy points).

Topic diversity makes no sense with these results.

Results for coherence (just putting them here, but they are useless):
c_npmi: 0.04249863595081498 
c_uci: -0.38558608414327483 
c_umass: -2.9300286095726666

c_npmi for each topic: [0.04249863595081498] 
c_uci for each topic: [0.04249863595081498] 
c_umass for each topic: [0.04249863595081498]