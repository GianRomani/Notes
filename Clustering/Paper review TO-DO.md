# TO-DO Template
Created: 2022-04-01 09:05
#to-do 

# Goals
Be on the same page with Maryam about the approaches used and the metrics used to evaluate the approaches.

# Action items
- [ ] WEClustering with sentence transformer and HDBSCAN: BERT with sentence transformer -> I think that the mothod used by Maryam is more similar to [[BERTopic]] than [[Clustering/WEClustering]] -> check this
- [x] Evaluation metrics:
	- [x] PMI
	- [x] inter/intra cluster
	- [x] topic coherence ([paper](https://arxiv.org/pdf/2004.14914.pdf))
	- [x] topic diversity and predictive accuracy ([paper](https://arxiv.org/pdf/2103.00498.pdf))
- [x] AlBERT and XLNet
- [ ] Other approaches:
	- [ ] NMF ([here](https://towardsdatascience.com/topic-modeling-articles-with-nmf-8c6b2a227a45) and [here](https://medium.com/voice-tech-podcast/topic-modelling-using-nmf-2f510d962b6e))
	- [ ] LDA2Vec
	- [ ] Neural topic modeling [here](https://aclanthology.org/2021.findings-acl.382.pdf)


For topic coherence -> [gensim]([Hyperparameters tuning — Topic Coherence and LSI model | by Eleonora Fontana | Betacom | Medium](https://medium.com/betacom/hyperparameters-tuning-topic-coherence-and-lsi-model-d31701f8aeec#:~:text=Topic%20Coherence%20in%20Python%20As%20stated%20in%20the,in%20order%20to%20choose%20the%20best%20num_topics%20value.))

We should not preprocess data before fed it to BERT models:
- [here](https://www.researchgate.net/post/Do_you_need_to_preprocess_text_for_BERT)
- [here](https://towardsdatascience.com/part-1-data-cleaning-does-bert-need-clean-data-6a50c9c6e9fd) and [here](https://towardsdatascience.com/does-bert-need-clean-data-part-2-classification-d29adf9f745a)
- [here](https://stackoverflow.com/questions/63979544/using-trained-bert-model-and-data-preprocessing)
- [here](https://stackoverflow.com/questions/62578609/data-preprocessing-for-bert-base-german)