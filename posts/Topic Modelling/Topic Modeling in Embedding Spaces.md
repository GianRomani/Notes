Created: 2022-08-18 17:04
#paper

## Main idea
ETM marries [[LDA]] and word embeddings. It is particularly suited for large and heavy-tailed vocabularies.

## In deep
Consider a corpus of *D* documents and a vocabulary *V*. Let $w_{dn} \in {1,...,V}$ denote the $n^{th}$ word in the $d^{th}$ document.

ETM considers two notions of latent dimension: the first one refers to the L-dimensional embeddings of the terms in the vocabulary, the second to the representation of each document in terms of K latent topics.
While in traditional topic modeling each topic is a full distribution over the vocabulary, in ETM, the $k^{th}$ topic is a vector $\alpha_k \in R^L$ in the embedding space. $\alpha_k$ is called topic embedding.

**Generative process:** The ETM model uses the topic embedding to form a per-topic distribution over the vocabulary. It uses a log-linear model that takes the inner product of the word embedding matrix and the topic embedding -> a high probability is assigned to a word *v*  in topic *k* is there is a high agreement between the word's embedding and the topic's embedding.

Given the word embedding matrix $L \times V$, the column $\rho_v$ is the embedding of the term *v*. The generative process of the $d^{th}$ document is the following:
1. Draw topic proportions $\theta_d \sim LN(0,I)$;
2. For each word *n* in the document:
	1. Draw topic assignment $z_{dn} \sim Cat(\theta_d)$;
	2. Draw the word $w_{dn} \sim softmax(\rho^T \alpha_{z_{dn}})$ 

LN() denotes the logistic-normal distribution. A draw $\theta_d$ from such distribution is obtained as $\delta_d \sim N(0,I); \theta_d=softmax(\delta_d)$. Cat() denotes the categorical distribution.
The step that is significantly different from standard topic modeling is the 2.2: in this step the embeddings of the vocabulary $\rho$ an the assigned topic embedding $\alpha_{z_{dn}}$ are used to draw the observed word from the assigned topic, as given by $z_{dn}$.
ETM uses the topic embedding $\alpha_{z_{dn}}$ as the context vector, where the assigned topic $z_{dn}$ is drawn from the per-document variable $\theta_d$.

ETM uses a matrix of word embeddings $\rho$, but in practice it can either rely on previously fitted embeddings or learn them as part of its overall fitting procedure. When the ETM uses previously fitted embeddings, it learns the topics of a corpus in a particular embedding space. This strategy is particularly useful when there are words in the embedding that are not used in the corpus.

## References
1. [Paper](https://aclanthology.org/2020.tacl-1.29.pdf)

## Code
1. [Ufficial Repository](https://github.com/adjidieng/ETM)
2. [Another Repo](https://github.com/lffloyd/embedded-topic-model)
