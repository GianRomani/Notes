# 2nd phase
Created: 2022-06-11 10:14
#note

New features:
- users actions are profiled;
- initial questions to define 80 different types of users (distinction on two levels) -> we already have an initial list of recommended items.

Will the user be able to follow/be friends with other users (similarly to any social network)?

### Clustering
Survey on clustering/topic modelling methods for Italian texts on Airbnb and Tripadvisor data -> Airbnb has more topic than Tripadvisor, where reviews are more similar to each others. **Goal**: compare and find best approaches for each dataset, given their unique aspects.

- Add more evaluation methods ([[Evaluate Clustering]]);
- Other approaches:
	- GANs;
	- Graphs [list of papers](https://github.com/wusw14/GNN-in-RS);
	- non-parametric models -> [[DeepDPM.pdf]]

Right now, non-parametric models based on Embeddings seem to be the best choices -> is this going to be valid for the other datasets?

### Recommender system
Ideas:
- Based on clustering methods I tried -> Top2Vec seems to be the best model;
- Multi layered graphs -> one for users, one for documents and one for words (check [entity2rec](https://enricopal.github.io/publications/entity2rec_Property_specific_Knowledge_Graph_Embeddings_for_Item_Recommendation.pdf) and [path recommendations](https://enricopal.github.io/publications/Knowledge_Graph_Embeddings_For_Recommender_Systems_main_contributions.pdf));
- Hybrid approach -> different smaller methods combined together

### Real time

#### Real time clustering
**Goal**: find a way to update clusters in real time given new data.
[[BERTopic]] considers the evolution in time of the dataset.

#### Real time  recommendations
[[Session based recommenders]] -> predict documents that could be interesting for user based on interaction in a given session.
RNNs, Transformers, word2Vec-liked algorithms

Do we have enough data for the sessions?

[ig2Vec](https://ai.facebook.com/blog/powered-by-ai-instagrams-explore-recommender-system/?utm_source=datarootlabs&utm_medium=blog) -> given an interaction on a document, get users similar to the owner of the document we liked (check [FAISS](https://engineering.fb.com/2017/03/29/data-infrastructure/faiss-a-library-for-efficient-similarity-search/?utm_source=datarootlabs&utm_medium=blog)), filter them and rank.

A session can be seen as a language modelling problem in which we want to predict the next item (like in [this](https://openreview.net/pdf?id=hFx3fY7-m9b) paper from Amazon Science).

## References
1. [A reading list](https://github.com/DeepGraphLearning/RecommenderSystems)
2. [List of papers, tools, libraries for RS](https://github.com/grahamjenson/list_of_recommender_systems)
3. [Session rs, PapersWithCode](https://paperswithcode.com/task/session-based-recommendations)

## Code
1. [LightFM](https://github.com/lyst/lightfm?utm_source=datarootlabs&utm_medium=blog)
2. [session-rec](https://github.com/rn5l/session-rec)

#### Tags
#clustering #dl #real_time #session_based