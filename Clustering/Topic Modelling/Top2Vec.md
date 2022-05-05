# Top2Vec
Created: 2022-04-29 16:53
#paper

Top2Vec is an algorithm for topic modeling and semantic search. It can automatically detect topics present in documents and generates jointly embedded topics, documents, and word vectors.
Once trained it can:
-   (Automatically) Get number of detected topics.
-   Get topics.
-   Get topic sizes.
-   Get hierarchichal topics.
-   Search topics by keywords.
-   Search documents by topic.
-   Search documents by keywords.
-   Find similar words.
-   Find similar documents.

It doesn't need stop words lists or stemming/lemmatization.
## Main idea
Main idea: many semantically similar documents are indicative of an underlying topic. The first thing to do is to create a joint embedding of document and word vectors, then we compute (dense) clusters of the documents and we identify which words attracted those documents together. Each dense area is a topic and the words that attracted the documents to the dense area are the topic words.
## In deep

The first step consists in build the semantic space, that is the spatial representation of words and documents as embeddings. To learn jointly embeddings for document and words, [Doc2Vec](https://cs.stanford.edu/~quocle/paragraph_vector.pdf) is used. In particular the DBOW (it uses the document vector to predict words within a context window in the document) model is chosen. 

### DBOW
The DBOW doc2vec model learns document vectors using a martix $D_{c,d}$ where *c* is the number of documents in the corpus and *d* is the size of the vectors to be learned for each document. Each row of the matrix contains a document vector $i \in R^d$. It is also required a context word matrix $W_{n,d}$, from which the context vector $w_c \in W_{n,d}$ of each word in the document is used to predict the document's vector $d \in D_{c,d}$. The prediction is given by $softmax(w_c D_{c,d})$ that generates a probability distribution over the corpus for each document being the document the word is from. The model learns using back propagation and stochastic gradient descent (to update each document vector in $D_{c,d}$ and $w_c$ from $W_{n,d}$). This learning process causes the document vectors to be close to word vectors of words that occur in them. 

### Number of topics

In the space defined above, each document vector can be seen as the topic of the document. That means that the words that are closer to a document vector are the most important to describe the document's topic. Dense areas of documents can be seen as indicative of an underlying common topic and the words that are closer to the topic vector (i.e. the centroid) are the words that best describes it. To cluster the space, [[HDBSCAN]] is used. Before computing the clustering, we need to use dimensionality reduction and [[UMAP]] is chosen in this case.

### Calculate topic vectors



## References
1. [Paper](https://arxiv.org/pdf/2008.09470.pdf)
2. [Towards data science](https://towardsdatascience.com/how-to-perform-topic-modeling-with-top2vec-1ae9bb4e89dc)
3. [Topic modeling comparison](https://medium.com/nlplanet/two-minutes-nlp-topic-modeling-and-semantic-search-with-top2vec-87855a973c8d)

## Code
1. [GitHub](https://github.com/ddangelov/Top2Vec)
