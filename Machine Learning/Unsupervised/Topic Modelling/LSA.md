Created: 2022-05-09 15:54
#note

Latent Semantic Analysis is a method for topic modelling whose algorithm can be described as follows:
1. Convert the text corpus into a document-term matrix;
2. Implement truncated singular value decomposition;
3. Encode the words/documents with the extracted topics

Step **1** is done with TF-IDF.
Step **2**: applye SVD to the document-term matrix and obtain three matrices, one (U) representing the *document-topic matrix*, one for the "strength" of each topic in the collection of documents and the last one (V) that represents the *word-topic matrix*.
Step **3**: use **U** and **V** matrices to decide what each derived topic represents.

LSA is fast and efficient but using SVD causes some information loss and this method is also unable to account for homonymy and polysemy. It is also difficult to draw insights from the topics (we don't know what the opics are).

## References
1. [TowardsDataScience](https://towardsdatascience.com/topic-modeling-with-latent-semantic-analysis-58aeab6ab2f2)
2. [Comparison of topic model methods](https://medium.com/nanonets/topic-modeling-with-lsa-psla-lda-and-lda2vec-555ff65b0b05)

## Code
1. 

#### Tags