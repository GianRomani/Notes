Created: 2022-05-19 11:11
#paper #survey

## Main idea
Survey on neural [[Topic modelling]] (NTM).

Historically the most used topic modelling techniques were Bayesian probabilistic topic models (BPTM), with [[LDA]] as the most know representative. In BPTM models topics are caught by latent variables sampled from pre-specified distributions (connected by Bayes' theorem).
These models were great until the advent of Big Data and Depp Learning, when they showed their limits:
- the inference complexity grows significantly as the model complexity grows -> difficult if not impossible to scale efficiently;
- not convenient to integrate BPTM models with [[DL models]].

## In deep
Given the corpus *D*, the collections of topic distributions of all the documents *Z* and the collections of words distributions of all the topics *T*, a topic model has to learn *T* and *Z* from D by learning a set of global variables for the word distributions of the topics and a projection parameterised by $\theta$ from a document's data to its topic distribution -> $z=\theta(b)$, where *b* is a vector of word counts. To learn these parameters we need to reconstruct a document's BoW data from its topic distribution using another projection -> $\phi: \tilde{b}=\phi(z,T)$.
Note that the majority of topic models belong to the category of probabilistic generative models, where z and b are latent and observed random variables assumed to be generated from certain distributions respectively.
The generative process, then, is the projection from the latent variables to the observed ones -> $\tilde{b}\simeq p^b_\phi(z,T)$ where *z* is sampled from the prior distribution $z \simeq p^z$. The inference process is denoted as $z \simeq q^z_\theta(b)$ where $q^z$ is the posterior distribution of *z*.

### Evaluation
The most commonly used metrics are:
- **Predictive accuracy**: log-likelihood of a model, in particular perplexity (i.e. how a model perform on new data, inversely proportional to average log-likelihood per word). Problems: goal of topic modelling is to represent seen data, we should not care too  much about new data; topic quality != predictive accuracy; difficult to use same metric for different methods.
- **Topic coherence**: much more useful than predictive accuracy. There are several formulations ([see here](https://dl.acm.org/doi/pdf/10.1145/2684822.2685324?casa_token=BLP_AKiZbTEAAAAA:cm8giYGltjBL7Cv0pv6c3oDzNPO4bSGdo4vOZqR-d8Cik3_TBDXnphJmIWV0Q75-nm4Ra6Q4c6il)), but most of them rely on the idea of computing the coherence of two words as the number of co-occurrence in the corpus. TC scores can vary a lot depending on the formulation -> use several of them and take the average. Also the choice of the corpus can affect the TC score.
- **Topic diversity**: measure of the diversity of the discovered topics -> it can be considered as the percentage of unique words in the top 25 words.
- **Downstream application performance**: performance can be measured considering the results on the final task for which we need to cluster the data -> for example in document classification we can compare performance of classifications in which fetures are the topic distributions learned by topic modelling approaches.

### VAE-NTM
[[Autoencoder]]s can be used to extend the generative and the inference process of BPTMs.  Generative and inference processes are modelled by the decoder and the encoder respectively. A VAE model can be learned by maximising the Evidence Lower Bound (ELBO) of the marginal likelihood of the BoW data *b* in terms if $\theta$, $\phi$ and *T* -> $E_{z \simeq q^z}[\log p(b|z)-KL[q^z||p^z]]$, where the right hand size term is the [[Kullback-Leibler divergence]]. 
When using VAE for topic modelling several things have to be considered:
- *b* is a high-dimensional, sparse vector and the length of the documents is variable;
- interpretability of topics is also very important -> incorporate word distributions of topics to interpret the latent representations.

A solution for the first problem is given by developing the decoder by specifying the data distribution $p^b$ as: $p^b=Multi(softmax(T^Tz+c))$, where $z \in R^K$ models the topic distribution of a document, $T \in R^{K\times V}$ models the words distribution of the topics and $c \in R^V$ is the bias. For the encoder the original VAE is followed. 
To face the problems listed above, several configurations for $p^z,p^b,q^z$ and architectures for $\phi,\theta,T$ have been proposed.

## References
1. [Paper](https://arxiv.org/pdf/2103.00498.pdf)

## Code
1. 
