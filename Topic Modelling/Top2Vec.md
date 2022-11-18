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
The DBOW doc2vec model learns document vectors using a matrix $D_{c,d}$ where *c* is the number of documents in the corpus and *d* is the size of the vectors to be learned for each document. Each row of the matrix contains a document vector $i \in R^d$. It is also required a context word matrix $W_{n,d}$, from which the context vector $w_c \in W_{n,d}$ of each word in the document is used to predict the document's vector $d \in D_{c,d}$. The prediction is given by $softmax(w_c D_{c,d})$ that generates a probability distribution over the corpus for each document being the document the word is from. The model learns by using back propagation and stochastic gradient descent (to update each document vector in $D_{c,d}$ and $w_c$ from $W_{n,d}$). This learning process causes the document vectors to be close to word vectors of words that occur in them. 

### Number of topics
In the space defined above, each document vector can be seen as the topic of the document. That means that the words that are closer to a document vector are the most important to describe the document's topic. Dense areas of documents can be seen as indicative of an underlying common topic and the words that are closer to the topic vector (i.e. the centroid) are the words that best describes it. To cluster the space, [[HDBSCAN]] is used. Before computing the clustering, we need to use dimensionality reduction and [[UMAP]] is chosen in this case.

### Calculate topic vectors and words
Once dense clusters of documents and noise documents are identified by HDBSCAN and UMAP we can calculate the topic vectors in many ways. The authors of the paper tried several techniques and found out that the results were always very similar, so they decided to just use the simplest one (topic vector = arithmetic mean of all the document vectors in the same dense cluster).

Word vectors that are closest to a topic vector are those that are most representative of it semantically. They can also be used to summarize the common topic of the documents in the dense area.
Common words appear in most document, and this implies that they are often in a region of the semantic space that is equally distant from all documents.

The size of a topic is given by the number of documents that belong to it.

An advantage of top2vec is the possibility of merging small topics. This is done by taking a weighted arithmetic mean of the topic vector of the smallest topic and its nearest topic vector, each weighted by their topic size. 

### Results
Obviously, to evaluate topic models, we need to score how much the topics describe the documents. The evaluation metric used here is [[Mutual Information]].
The mutual information about all documents D when described by all words W (words nearest to their topic vector), is given by: $I(D,W)=\sum_{d \in D}\sum_{w \in W}P(d,w)\log(\dfrac{P(d,w)}{P(d)P(w)})$, where the term inside the two sums can be seen as the *probability-weighted amount of information (PWI)*.
In order to evaluate topics' usefulness to a user, we use just the top *n* words of the topic, so, given each topic $t \in T$, a set of *n* words $W_t \subset W$ and documents $D_t \subset D$, the information gained about all documents when described by their corresponding topic is given by: $PWI(T)= \sum_{t \in T}\sum_{d \in D_t}\sum_{w \in W_t}P(d,w)\log(\dfrac{P(d,w)}{P(d)P(w)})= \sum_{t \in T}\sum_{d \in D_t}\sum_{w \in W_t}P(d|w)P'(w)\log(\dfrac{P(d,w)}{P(d)P(w)})$, where P(w) is the marginal probability of the word w across all documents D and P'(w) is the probability of topic word w (It is the same as I(D,W) so it can be omitted). If topics contain stop-words, the information gain will be low because the probability of any specific document given a very common word is very low.

Using this metric, top2vec performs much better than [[LDA]] and [[PLSA]].

## References
1. [Paper](https://arxiv.org/pdf/2008.09470.pdf)
2. [Towards data science](https://towardsdatascience.com/how-to-perform-topic-modeling-with-top2vec-1ae9bb4e89dc)
3. [Topic modeling comparison](https://medium.com/nlplanet/two-minutes-nlp-topic-modeling-and-semantic-search-with-top2vec-87855a973c8d)

## Code
1. [GitHub](https://github.com/ddangelov/Top2Vec)
