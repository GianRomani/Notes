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

Coherence has some limitations, according to some [people](https://highdemandskills.com/topic-model-evaluation/):
-   **Variability**—The aggregation step of the coherence pipeline is typically calculated over numerous word-group pairs. While this produces a metric (e.g., mean of the coherence scores), there’s no way of estimating the variability of the metric. This means that there’s no way of knowing the degree of confidence in the metric. Hence, although we can calculate aggregate coherence scores for a topic model, we don’t really know how well that score reflects the actual coherence of the model (relative to statistical noise).
-   **Comparability**—The coherence pipeline allows the user to select different methods for each part of the pipeline. This, combined with the unknown variability of coherence scores, makes it difficult to meaningfully compare different coherence scores or coherence scores between different models.
-   **Reference corpus**—The choice of reference corpus is important. In cases where the probability estimates are based on the reference corpus, then a smaller or domain-specific corpus can produce misleading results when applied to a set of documents that are quite different from the reference corpus.
-   **“Junk” topic**—Topic modeling provides no guarantees about the topics that are identified (hence the need for evaluation) and sometimes produces meaningless, or “junk”, topics. These can distort the results of coherence calculations. The difficulty lies in identifying these junk topics for removal—it usually requires human inspection to do so. But, involving humans in the process defeats the very purpose of using coherence, ie. to automate and scale topic model evaluation.
- 
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