# Ideas
Created: 2022-03-28 10:42
#note 

My RecSys could work in the following way:
- documents and pictures are embedded using [[Data2Vec - A General Framework for Self-supervised Learning in Speech, Vision and Language]];
- User embedding is obtained using data2vec on the history of liked and/or created posts;
- topic modeling ([[Top2Vec]] or [[BERTopic]]) is used to extract the most important features of the documents, i.e. the topics. Do the same for the user embedding;
- Extract the recommended posts using FAISS or NMSLib;
- Rank the pictures of the posts.

I need to compare results of two scenarios:
- using topic modeling to reduce number of features;
- without using topic modeling.

## References
1. [LDA and LSA for recommender systems](https://link.springer.com/chapter/10.1007/978-3-319-27030-2_16)
2. [Paper recommendation](https://boa.unimib.it/bitstream/10281/195641/2/phd_unimib_799490.pdf)
3. [ANN for RecSys](https://www.benfrederickson.com/approximate-nearest-neighbours-for-recommender-systems/)

## Code
1. 

#### Tags
#to-do #ideas