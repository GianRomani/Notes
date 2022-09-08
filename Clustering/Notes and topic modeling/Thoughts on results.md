# Thoughts on results
Created: 2022-09-07 11:03
#note

Metrics scores for **easytour**:
- **LDA** -> topic diversity decreases when the number of cluster is bigger and has better results if we consider 10 words for each topic instead of 25, coherence is not regular and I cannot find a relation between number of clusters and this score (furthermore the results can vary a lot in separate tests because of the probabilistic nature of the algorithm). It is possible to see a pattern in coherenc plots:
	- u_mass tends to decrease;
	- u_npmi and c_uci tend to increase;
	- c_v is quite stable;
	- all the metrics have a spike around 20-25 topics;
	- using 10 words for topic the results are (by a little) better
- **NMF** -> both topic diversity and coherence seem to decrease when the number of clusters increases. Using top 10 words the results are better than 25 words;
- **BERTopic** (sentence transformer) -> diversity increases when number of topics increases, coherence on the other hand is inversely proportional to the number of topics;
- **ETM** -> diversity decreases, while coherence behaviour is not regular, sometimes it seems it gets better when the number of topics is increased. Top10 is better than top25.


Metrics scores for **tourpedia**:
- **LDA** -> metric scores decreases when number of topics is increased (25 top words),
- **BERTopic** (sentence transformer)  -> all metrics decreases expect topic diversity that seems to increases a lot when the number of topics increases (maybe because the clusters are composed by few documents) Top10 and top25 get similar results;
- **Top2Vec** -> diversity decreases, while coherence is quite irregular. Top10 is quite better for diversity and (just a bit) worse for coherence;


## References
1. [[Study topic parameters]]

## Code
1. [My code](https://colab.research.google.com/drive/1J31orWn8I8hgv0K5YV40mFcAzTSVRIxl?authuser=0#scrollTo=59Iek9o-AXd4&uniqifier=1)

#### Tags