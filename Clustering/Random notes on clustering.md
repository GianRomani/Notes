# Random notes on clustering
Created: 2022-05-21 17:36
#note

- [[Top2Vec]] embedds documents and words together. Document are assigned to a single topic;
- [[BERTopic]] embedds documents, reduces the dimensionality and clusters documents. Then it uses TF-IDF to extract topic representation from each cluster. Documents are assigned to a single topic;
- [[Clustering/WEClustering]] is similar to [[BERTopic]] but it clusters the embeddings, it defines a topic as a cluster obtained in the previous step and then it clusters the documents based on the class TF-IDF (sum of the TF-IDFs of the words of the embedding that are in a cluster);
- [[Combined Topic Modelling]] uses [[Autoencoder]] on embeddings which have been concatenated to BoW.


## References
1. 

## Code
1. 

#### Tags