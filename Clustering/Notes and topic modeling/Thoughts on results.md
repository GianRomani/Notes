# Thoughts on results
Created: 2022-09-07 11:03
#note

# Results for each model
Metrics scores for **easytour**:
- **LDA** -> topic diversity decreases when the number of cluster is bigger and has better results if we consider 10 words for each topic instead of 25, coherence is not regular and I cannot find a relation between number of clusters and this score (furthermore the results can vary a lot in separate tests because of the probabilistic nature of the algorithm). It is possible to see a pattern in coherenc plots:
	- u_mass tends to decrease;
	- u_npmi and c_uci tend to increase;
	- c_v is quite stable;
	- all the metrics have a spike around 20-25 topics;
	- using 10 words for topic the results are (by a little) better;
	- irbo increases over time
- **NMF** -> both topic diversity and coherence seem to decrease when the number of clusters increases. Using top 10 words the results are better than 25 words. IRBO increaeses and then stabilizes after 30 topics;
- **BERTopic** (sentence transformer) -> diversity increases when number of topics increases, coherence on the other hand is inversely proportional to the number of topics. Sentence transformer has the best results, roberta is in second place;
- **ETM** -> diversity decreases, while coherence behaviour is not regular, sometimes it seems it gets better when the number of topics is increased. IRBO is better with a big number of topics. Top10 is better than top25;
- **CTM** -> for top10 diversity descreases, coherence irregular. For top25 coherence seems to improve when number of topics increases. Diversity is much better for top10, coherence is a bit better for top25. IRBO is not regular (as coherence), but thia makes more sense compared to diversity;
- **Top2Vec** -> Doc2Vec with chunking is the best.


Metrics scores for **tourpedia**:
- **LDA** -> metric scores decreases when number of topics is increased;
- **NMF** -> metrics scores decreases, c_v is not regular;
- **CTM** -> u_mass and c_v are not regular;
- **ETM** -> as CTM;
- **BERTopic** (sentence transformer)  -> all metrics decreases expect topic diversity that seems to increases a lot when the number of topics increases (maybe because the clusters are composed by few documents) Top10 and top25 get similar results;
- **Top2Vec** -> diversity decreases, while coherence is quite irregular. Top10 is quite better for diversity and (just a bit) worse for coherence. The best single results (and also the best average). Average results are quite good, but there are a lot of tests that are not good enough -> do several tests and choose the best. Dov2Vec is the best embedding model.


**Other notes**: 
- C_v score gets results that are very different from the other coherence scores (which plots are generally quite similar one to another), plus is not suggested to use it (see [[Coherence]]);
- Instead of plain topic diversity, use Inverted RBO (from [here](https://link.springer.com/chapter/10.1007/978-3-030-80599-9_4)). Plain diversity scores just decreases when th enumber of topics is incremented but this is unlikely to happen every time, With inverted RBO instead I got variable results that are comparable to the onew obtained from coherence. 
- For NMF, Frobenius norm is better than [[Kullback-Leibler divergence]] by a little

## References
1. [[Study topic parameters]]

## Code
1. [My code](https://colab.research.google.com/drive/1J31orWn8I8hgv0K5YV40mFcAzTSVRIxl?authuser=0#scrollTo=59Iek9o-AXd4&uniqifier=1)

#### Tags

# Thoughts
NMF seems to be the best method for several metrics → I think that it performs very well for c_v because this metric is based on cosine similarity and NMF's goal is to quantify the distance between the elements ([here](https://www.analyticsvidhya.com/blog/2021/06/part-15-step-by-step-guide-to-master-nlp-topic-modelling-using-nmf/)). The other metrics consider just co-occurrence or [[Mutual Information]].

Now [[Top2Vec]] is a bit better than NMF for c_v (in some configurations).

Doc2Vec (with chunking) seems to be the best embedding model for Top2Vec → Doc2Vec, unlike sentence transformer models, is primarily based on co-occurrence and apparently this is good in our work. 

Sometimes [[Top2Vec]] gives strange results, e.g. it finds just two topics.

Top2Vec with deep-learn should get even better results.

I noticed that when models get better in topic diversity they lose points in coherence, coincidence?

Top2Vec is superior to NMF, because by twerking the parameters we can improve the metric we are more interested in, while in NMF the results are static.