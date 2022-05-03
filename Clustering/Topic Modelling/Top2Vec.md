# Top2Vec
Created: 2022-04-29 16:53
#paper

Top2Vec is an algorithm for topic modeling and semantic search. It can automatically detect topics present in documents and generates jointly embedded topics, documents, and word vectors.
Once trained it can:
-   Get number of detected topics.
-   Get topics.
-   Get topic sizes.
-   Get hierarchichal topics.
-   Search topics by keywords.
-   Search documents by topic.
-   Search documents by keywords.
-   Find similar words.
-   Find similar documents.

It doesn't need stop words lists or stremming/lemmatization.
## Main idea
Main idea: many semantically similar documents are indicative of underlying topic. The first thing to do is to create a joint embedding of document and word vectors, then we compute (dense) clusters of the documents and we identify which words attracted those documents together. Each dense area is a topic and the words that attracted teh documents to the dense area are the topic words.
## In deep

## References
1. [Paper](https://arxiv.org/pdf/2008.09470.pdf)
2. [Towards data science](https://towardsdatascience.com/how-to-perform-topic-modeling-with-top2vec-1ae9bb4e89dc)
3. [Topic modeling comparison](https://medium.com/nlplanet/two-minutes-nlp-topic-modeling-and-semantic-search-with-top2vec-87855a973c8d)

## Code
1. [GitHub](https://github.com/ddangelov/Top2Vec)
