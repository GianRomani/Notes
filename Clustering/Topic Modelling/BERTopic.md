# BERTopic
Created: 2022-05-03 09:08
#paper
 
 The firsts #topic_modeling  approaches used bag-of-words representations to create topics, but this method has the limit that they do not consider the semantic relationships among words. As an answer to this issue, text embedding techniques became popular in NLP. In papers such [[Clusters on word embeddings]] or [[Top2Vec]], topic representations are extracted from word embeddings. In particular, documents are clustered and then topic representations are got from finding words close to a cluster's centroid. That means that words close to a cluster's centroid are the most representative of that cluster, but in reality a cluster will not always lie within a sphere around a cluster centroid, so the assumption cannot hold for every cluster of documents.
## Main idea

BERTopic is a topic modeling technique that uses BERT embeddings and a class-based TF-IDF to create dense clusters, allowing for easily interpretable topics whilst keeping important words in the topic descriptions. 

## In deep
BERTopic can be described as a three steps approach:
1. the embeddings of the documents are created using pre-trained language models;
2. the dimensionality is reduced and clusters of semantically similar embeddings are computed;
3. the class-based TF-IDF is used to extract the topic representation from each topic.

To embed documents, [Sentence-BERT ](https://www.sbert.net/) (SBERT) is used.
Because of Curse of Dimensionality, distance measures differ little -> dimensionality reduction is needed. [[UMAP]] is the dr approach that is capable to better preserve the local and global structure of high dimensional data. 
Finally, clustering is done using HDBSCAN method.

Once we have the clusters we want the topic representations (1 cluster = 1 topic). To do so, the paper uses a modified version of TF-IDF: $W_{t,c}=tft_{t,c}\log(1+\dfrac{A}{tf_t})$ where the term frequency models the frequency of term *t* in a class *c*, which is the collection of documents cancatenated into a single document for each cluster; the inverse class frequency is calculated as the logarithm of the average number of words per class A divided by the frequency of term *t* across all classes. 
The c-TF-IDF models the importance of words among clusters.

### Dynamic topic modeling
Dynamic topic modeling models how topics might have evolved over time. By assuming that the remporal nature of topics should not influence the creation of global topics, BERTopic can model this evolution too. We have to first fit BERTopic on the entire corpus and then we can crete a local representation of each topic by simply multiplying the term frequency of socument at timestep *i* with the pre-calculated global IDF values: $W_{t,c,i}=tf_{t,c,i}\cdot\log({1+ \dfrac{A}{tf_t}})$.
### Smoothing
Topic representation over time is not linear, that means that the representation at timestep *t* is independent of timestep *t-1*. If we want a linearly evolving topics we can use the c-TF-IDF matrix by normalizing it (dividing it using the L1-norm) and taking for each topic and representation at timestep *t* the average of the normalized c-TF-IDF vectors at *t* and *t-1*. 

## Results
The evaluation consisted in Topic coherence (measured with Normalized [[Mutual Information]]) and topic diversity (percentage of unique words for all topics) as defined [here](https://aclanthology.org/2020.tacl-1.29.pdf).
The models results as competitive in all the test compared to SOTA models (it is consistently outperformed just in one case by [[Combined Topic Modelling]], which is really good in topic diversity). It is worth of notice the fact that BERTopic remains competitive independently of the SBERT language model used. This is probably given by the fact that documents embeddings and word-topic distribution are separeted processes.

Pros: competitive regardless of the model used, separation of process of embeddings documents from representing topics and possibility to model dynamic aspects of topics.

Cons: each document contains just a single topic and topic representation uses bags-of-words not the embeddings.

## References
1. [Paper](https://arxiv.org/abs/2203.05794)
2. [Documentation](https://maartengr.github.io/BERTopic/algorithm/algorithm.html)
3. [TowardsDataScience guide](https://towardsdatascience.com/interactive-topic-modeling-with-bertopic-1ea55e7d73d8)
4. [TowardsDataScience Code](https://towardsdatascience.com/topic-modeling-with-bert-779f7db187e6)

## Code
1. [GitHub](https://github.com/MaartenGr/BERTopic)
