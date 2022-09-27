# Paper review TO-DO
Created: 2022-08-08 09:05
#to-do 

# Goals
Be on the same page with Maryam about the approaches used and the metrics used to evaluate the approaches.

# Action items
- [x] WEClustering with sentence transformer and HDBSCAN: BERT with sentence transformer -> I think that the mothod used by Maryam is more similar to [[BERTopic]] than [[Clustering/WEClustering]] -> check this
- [x] Evaluation metrics:
	- [x] PMI
	- [x] inter/intra cluster
	- [x] topic coherence ([paper](https://arxiv.org/pdf/2004.14914.pdf))
	- [x] topic diversity and predictive accuracy ([paper](https://arxiv.org/pdf/2103.00498.pdf))
- [x] AlBERT and XLNet
- [x] Other approaches:
	- [x] NMF ([here](https://towardsdatascience.com/topic-modeling-articles-with-nmf-8c6b2a227a45) and [here](https://medium.com/voice-tech-podcast/topic-modelling-using-nmf-2f510d962b6e))
	- [x] LDA2Vec
	- [x] Neural topic modeling [here](https://aclanthology.org/2021.findings-acl.382.pdf)
- [x] Test Top2Vec with deep-learn
- [x] Add section about tests on Top2Vec with several embedding models and chunking, with graphic comparison
- [x] update results table
- [x] Test n-gram vs no n-gram
- [ ] results divided in qualitative results and quantitative results
- [x] improve plots
- [ ] write sections on paper
- [ ] datasets statistics
- [x] Study IRBO formula
- [ ] tests on raw data:
	- [ ] tourpedia
		- [x] bert
		- [x] roberta
		- [x] sentence-tr
		- [x] top2vec
	- [ ] easytour:
		- [x] bert
		- [x] roberta
		- [x] sentence-tr
		- [ ] top2vec
- [x] add embedding coherence


For topic coherence -> [gensim]([Hyperparameters tuning — Topic Coherence and LSI model | by Eleonora Fontana | Betacom | Medium](https://medium.com/betacom/hyperparameters-tuning-topic-coherence-and-lsi-model-d31701f8aeec#:~:text=Topic%20Coherence%20in%20Python%20As%20stated%20in%20the,in%20order%20to%20choose%20the%20best%20num_topics%20value.))

We should not preprocess data before fed it to BERT models:
- [here](https://www.researchgate.net/post/Do_you_need_to_preprocess_text_for_BERT)
- [here](https://towardsdatascience.com/part-1-data-cleaning-does-bert-need-clean-data-6a50c9c6e9fd) and [here](https://towardsdatascience.com/does-bert-need-clean-data-part-2-classification-d29adf9f745a)
- [here](https://stackoverflow.com/questions/63979544/using-trained-bert-model-and-data-preprocessing)
- [here](https://stackoverflow.com/questions/62578609/data-preprocessing-for-bert-base-german)


Evaluation parameters:
- Calinski-Harabasz -> [survey (1000+ citations)](https://ieeexplore.ieee.org/abstract/document/1114856?casa_token=mDgHc0AQe6EAAAAA:HH9lYhDeJfcl98aUIB0ZBR0VNOL0NmKTHsGfS4Lq6G2m_F8PrJ6wK4kpJFVhEGaL925A9mE) [new survey](https://www.sciencedirect.com/science/article/abs/pii/S095219762200046X) most of the papers are about clustering, but there are some that are about topic modeling (most of them have less of 30 citations and regards the medical field)
- Davies-Bouldin -> [number of topics optimization](https://www.mdpi.com/2504-4990/1/1/25)  with 26 citations [LDA](https://d1wqtxts1xzle7.cloudfront.net/49319774/FLAIRS09-Millar-with-cover-page-v2.pdf?Expires=1660144734&Signature=Y7S01s0I4TNEm0XPu~YpG~54Ika9Mto9v68~kCVfKU60a2JdijGmTMuCbMvd2lFZMy8sXG4B~klRMsPAn6p-x~yIZ0oNGwbjqx7G8XkOO1xuDh3FHTR7mSFNtWBYawvpYsQ4gh71Qi~ERDRQS6Cl0lLqh~e8Nk3jL7kEEyexXsJkFyH75-dGZC7AHcdJw2RCWX1Ozfh7lAhbYBrA4yOHSWXO0w7icyWPrz5Qkz-t76WwEz7jq-kDqTHeIgrGuPmHHkjILOO4mPFP7OJA3~f9xAAqNvbP2YoYUL02VUpt9-x1eYMBtDe-LWtvt~jpGlG4TM3VyW8DR3bN~LH122o7lw__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA) similar to Calinski-Harabasz but less used
- Perplexity -> it needs labels
- Inter/intra cluster distance [topic modeling for twitter](https://www.cs.toronto.edu/~jstolee/projects/topic.pdf) 32 citations, there are also other papers
- Topic diversity now works properly and could be interesting for our paper

Devised models:
- ETM -> [paper](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00325/96463/Topic-Modeling-in-Embedding-Spaces) [GitHub](https://github.com/adjidieng/ETM?utm_source=catalyzex.com)  232 citations