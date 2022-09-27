# Coherence
Created: 2022-09-06 14:38
#note

Topic Coherence measures score a single topic by measuring the degree of semantic similarity between high scoring words in the topic. These measurements help distinguish between topics that are semantically interpretable topics and topics that are artifacts of statistical inference.

Let’s take quick look at different coherence measures, and how they are calculated:

1.  **_C_v_** measure is based on a sliding window, one-set segmentation of the top words and an indirect confirmation measure that uses normalized pointwise mutual information (NPMI) and the cosine similarity. It ranges from 0 to 1 with 1 being perfectly coherent topics;
2.  **_C_p_** is based on a sliding window, one-preceding segmentation of the top words and the confirmation measure of Fitelson’s coherence,
3.  **_C_uci_** measure is based on a sliding window and the pointwise mutual information (PMI) of all word pairs of the given top words. The higher, the better;
4.  **_C_umass_** is based on document co-occurrence counts, a one-preceding segmentation and a logarithmic conditional probability as confirmation measure. It stays in the range [-inf,0], the bigger, the better;
5.  **_C_npmi_** is an enhanced version of the C_uci coherence using the normalized pointwise mutual information (NPMI). The higher, the better;
6.  **_C_a_** is baseed on a context window, a pairwise comparison of the top words and an indirect confirmation measure that uses normalized pointwise mutual information (NPMI) and the cosine similarity.

C_v is not recommended since there are some know [issues](https://github.com/dice-group/Palmetto/issues/12) associated with it.
The higher the scores obtained for the metrics the better is our topic model.

## References
1. [Paper](http://svn.aksw.org/papers/2015/WSDM_Topic_Evaluation/public.pdf)
2. [Towards Data Science](https://towardsdatascience.com/evaluate-topic-model-in-python-latent-dirichlet-allocation-lda-7d57484bb5d0)
3. [Umass and UCI](http://qpleple.com/topic-coherence-to-evaluate-topic-models/)
4. [Which coherence score is better?](https://www.baeldung.com/cs/topic-modeling-coherence-score)
5. [Descriptions](https://palmetto.demos.dice-research.org/)
6. [Understanding topic coherence measures](https://towardsdatascience.com/understanding-topic-coherence-measures-4aa41339634c)

## Code
1. [Gensim](https://radimrehurek.com/gensim/models/coherencemodel.html)

#### Tags
#coherence #topicmodeling