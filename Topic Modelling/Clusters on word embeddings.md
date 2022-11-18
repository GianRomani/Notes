# Tired of Topic Models? Clusters of Pretrained Word Embeddings Make for Fast and Good Topics too!
Created: 2022-05-04 13:58
#paper

## Main idea

Clustering pretrained word embeddings while incorporating document information for weighted clustering and reranking top words. Results obtained with this method are comparable to the ones of classical topic models, but there are improvements regarding running time and computational complexity.

The goal of the paper is to benchmark (centroid-based) clustering of embedding methods against [[LDA]]. 
To perform as well as LDA, corpus frequency statistics are directly incorporated into the clustering algorithm and two methods are used: 1) terms are weighted during clustering, 2) reranking of terms to obtain the top J representative words. To further speedup the algorithm, PCA is used on the embeddings.

Problem: outliers could form their own cluster.

## In deep

Text is preprocessed (lowercased, stopwords, punctuation, digits, rare words etc) and then converted to embeddings vectors, then the clustering methods are applied to obtain k clusters, using weighted or unweighted word types. After that, we get the top J words from each cluster.
The top J words in centroid based clusters algorithms are those closest to the cluster center or  with the highest probability under the cluster parameters.

**Note**: to obtain the top topics given a document, compute similarity scores between learned topic cluster centers and all word embeddings from that particular document and normalize them using softmax to obtain a probability distribution.

Weighting is based, similarly to LDA, on the frequency of occurrences of the words. TF, TF-DF and TF-IDF were tried and surprisingly TF was the best one.

Reranking is used because there is no guarantee that words closest to cluster centers are important word types. Normalized [[Mutual Information]] is used.

The best results are obtained from BERT with GMM (with no need for reranking). Methods with centroid based k-means improved consistently their performance if dimensionality reduction is used.

Compared to LDA, the diversity within topics is greater while the coherence score is similar. BERT resulted as more sensitive to noisy vocabulary than LDA, but weighting helps to alleviate this phenomenon.

## References
1. [Paper](https://arxiv.org/pdf/2004.14914.pdf)

## Code
1. [GitHub](https://github.com/adalmia96/Cluster-Analysis)
