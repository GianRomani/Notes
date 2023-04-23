Created: 2022-05-03 09:13
#note

 Text analysis method that analyzes "bags" of words together, instead of counting them individually, in order to capture how the meaning of words is dependent upon the broader context in which they are used in natural language.
 The idea consists in the fact that documents tipically concerns several topics in different proportions, so we expect that words related to such topics will happear in different proportions.
 
 An advantage of topic models over some other forms of cluster analysis is given by the fact that topic models are mixture models, i.e. to each document is assigned the probability of belonging to latent topic.
 
 The most famous topic model is [[LDA]] and in the past a lot of vaiants based on this algorithm were proposed.
 A new approach is based on [Stochastic block model](https://en.wikipedia.org/wiki/Stochastic_block_model).
 
## References
1. [Wikipedia](https://en.wikipedia.org/wiki/Topic_model)
2. [Theory+Tutorial](https://cbail.github.io/SICSS_Topic_Modeling.html)

## Code
1. [Topic model based RS](https://towardsdatascience.com/topic-model-based-recommendation-systems-a02d198408b7)

#### Tags
#topic_modeling