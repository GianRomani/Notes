# Paper's Sections
Created: 2022-09-12 14:07
#note

## 2) Background
### 2.1) Definition of Terms
**Topic modeling** methods can be applied to a great variety of fields and data types, including information retrieval ([paper](https://maroo.cs.umass.edu/getpdf.php?id=850)), bioinformatics ([review](https://springerplus.springeropen.com/articles/10.1186/s40064-016-3252-8)) and topic discovery in images ([paper](https://ieeexplore.ieee.org/abstract/document/1541280.?casa_token=CuY86UvTQWwAAAAA:Mh1AaYah3cD5a6lZVorn2Qj_OXvg76RosG1rSdVW5INWzq3NWIVYwWdMRZcVZnrxuJDH)). Our work focuses on approaches that can be used for text-based data.
A typical text-based dataset is made of “documents” which are strings of variable length composed of *N* words, where a “word” (or “term”) is considered as the fundamental unit of a sample. The set of distinct words presents in a dataset forms a “vocabulary” and a “topic” is then viewed as a probability distribution over this fixed vocabulary.

Traditionally, text documents are represented as a bag of words, i.e. each document is described by a vector of dimension equal to the vocabulary size, where each dimension represents the number of times a certain word appears in a document. The limits of such text representation are known: the vectors are very sparse, if we add a new document with words never used before the length of the vocabulary, and so of the vectors, will increase, and the context is not considered. 
A first improvement is given by TF-IDF, which measures how frequent a word is in a document (TF) and how much information it provides (IDF). 
**TBD add formula for TFIDF**

Further improvements are obtained when considering semantic closeness between words. Word embeddings are a way to describe words considering their semantic meaning. These fixed-sized vectors are calculated using the context of words, i.e. the probability distribution for each word appearing before or after another. If two words often appear together, then their embeddings will be similar.
In the last years, several methods to compute vector embeddings were proposed, among them Word2Vec, FastText, ELMo and more recent and powerful methods based on the Transformer architecture.
**TBD Transformer and BERT**

### 2.2) Review of Recent Studies

Topic modelling has its roots in the 1980s ([paper](https://www.sciencedirect.com/science/article/pii/S0306437920300703?casa_token=nJDJ5Nlh9T4AAAAA:2LmMdid6ESJ6R7T6UL5MlAkBP_b3kagZy9PgUQUTlNvAZFgqKvzpvHf5Z7jFOKyFbCyKXg#b14)), but really took off in the late 1990s thanks to methods such as [LSI](https://asistdl.onlinelibrary.wiley.com/doi/epdf/10.1002/%28SICI%291097-4571%28199009%2941%3A6%3C391%3A%3AAID-ASI1%3E3.0.CO%3B2-9?saml_referrer=) and especially [LDA](https://www.jmlr.org/papers/volume3/blei03a/blei03a.pdf?ref=https://githubhelp.com). Starting from LDA, many methods were designed over the last two decades ([cells](https://www.sciencedirect.com/science/article/pii/S0002929718301150) [hierachical](https://ieeexplore.ieee.org/abstract/document/8607040) [bioinformatics](https://d-nb.info/1116751054/34)). Despite their success, conventional Bayesian probabilistic topic models started to show signs of fatigue in the era of big data and deep learning [here](https://www.bing.com/search?q=topic+modelling+meets+deep+learing&cvid=99e100f4d08d4b0ba5f77714870cd94a&aqs=edge..69i57.7129j0j4&FORM=ANAB01&PC=U531).  Instead, models based on the use of Deep Learning techniques are becoming more and more popular.
**TBD neural topic modeling**
[survey](https://arxiv.org/abs/2103.00498)
[Medium on dl for tm and various fields of application](https://medium.com/data-folks-indonesia/recent-works-in-topic-modeling-56c38da8dfc4)
**TBD non probabilistic methods -> NMF**

**TBD fields on which tm was applied**
The scientific community did not focus just on designing different methods that are then applied on traditional data (text), but in the years there has been a great effort in the application of topic modeling to different fields and type of data.
[LDA in various fields](https://link.springer.com/article/10.1007/s11042-018-6894-4)
[Software traceability](https://ieeexplore.ieee.org/abstract/document/6062077?casa_token=1fXi-6Dlo5gAAAAA:6259L_R_-_FReFTKM0KJztI60eJmKCxD_eQ5k34sVB8IHc4tJzC6unvRmF5Ol6dx64W-)
[Shot texts](https://ieeexplore.ieee.org/abstract/document/6778764?casa_token=GGNPD3nHHDUAAAAA:xBe7U5PewTVnNINmRF1fTqWhMEP7h6E8flD5PJZd0BaRiR8VkiW2KcR23stLLrW6hT0U)
[Twitter](https://dl.acm.org/doi/abs/10.1145/1964858.1964870?casa_token=lesME6RwzJgAAAAA:FvBakC1_aAJ7j_qRWdSJhREITRRaY8oNQXbKoNPdUiaC-b2vcPTh0f74SLtsk4UNHD1DfIsX)
[Scientific articles](https://dl.acm.org/doi/abs/10.1145/2020408.2020480?casa_token=iaBjyLLhaj8AAAAA:bgOgKZ2z99AQfQrA0VsQuiRLOQGLpC01yYqiYfd3zwkNsN7KDG8Hs2g9NIJMrhuvx9WEx5b1)

[Evaluation](https://link.springer.com/chapter/10.1007/978-3-030-80599-9_4#chapter-info)
## References
1. [[Background for Topic Modeling]]

## Code
1. 

#### Tags
#paper #topicmodeling 