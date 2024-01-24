# Paper's Sections
Created: 2022-09-12 14:07
#note

## 2) Background
**Topic modeling** methods can be applied to a great variety of fields and data types, including information retrieval ([paper](https://maroo.cs.umass.edu/getpdf.php?id=850)), bioinformatics ([review](https://springerplus.springeropen.com/articles/10.1186/s40064-016-3252-8)) and topic discovery in images ([paper](https://ieeexplore.ieee.org/abstract/document/1541280.?casa_token=CuY86UvTQWwAAAAA:Mh1AaYah3cD5a6lZVorn2Qj_OXvg76RosG1rSdVW5INWzq3NWIVYwWdMRZcVZnrxuJDH)). Our work focuses on approaches that can be used for text-based data.

### 2.1) Definition of Terms

In this section, we provide definitions on terms and basic concepts involved in topic modeling.
A typical text-based dataset is made of “documents” which are strings of variable length composed of *N* words, where a “word” (or “term”) is considered as the fundamental unit of a sample. The set of distinct words presents in a dataset forms a “vocabulary” and a “topic” is then viewed as a probability distribution over this fixed vocabulary.
Obviously, the way in which we represent words and documents has a great impact on topic modeling. We will then present the ideas that are useful to understand the approaches we are analysing in this work. We will refer to the classification of word representation's techniques proposed by [S. Selva Birunda and R. Kanniga Devi](https://link.springer.com/chapter/10.1007/978-981-15-9651-3_23).

Category 1: Traditional word embedding, or Count-based embedding [here](https://arxiv.org/pdf/1901.09069.pdf). In this class fall all those methods that use frequency of words on the whole document, co-occurrence of words, and rarity of words in documents. Traditionally, text documents are represented as a bag of words, i.e. each document is described by a vector of dimension equal to the vocabulary size, where each dimension represents the number of times a certain word appears in a document. The limits of such text representation are known: the vectors are very sparse, if we add a new document with words never used before the length of the vocabulary, and so of the vectors, will increase, and the context is not considered. 
A first improvement is given by TF-IDF, which measures how frequent a word is in a document (TF) and how much information it provides (IDF). 
The well-known formula for TF-IDF is: $tfidf_{t,d}=tf(t,d) \cdot idf(t,D)$, with $tf(t,d)=\dfrac{f_{t,d}}{\sum_{t' \in d}f_{t',d}}$ and $idf(t,D)=\log \dfrac{|D|}{1+|\{d \in D : t \in d\}|}$ where $f_{t,d}$ is the raw count of term *t* in the document *d* and *D* is the dataset. The i-th document is then represented as $d_i=[tfidf_{0,i},...,tfidf_{N,i}]$, where N is the number of words in the vocabulary.

Category 2: Static Word Embedding. These prediction-based methods compute probabilities to the words and map them into fixed-size vectors. These embedding do not consider context, i.e. a word embedding does not change if the word appear in a different sentence. If two words often appear together, then their embeddings will be similar.
This class of techniques gained in popularity after the release of Word2Vec [here](https://www.cambridge.org/core/journals/natural-language-engineering/article/word2vec/B84AE4446BD47F48847B4904F0B36E0B). This model can utilize either of two architectures: continuous bag-of-words (CBOW), which predicts one word from the surrounding words, or Skip-gram, that, on the other end, uses one word to predict all surrounding words. Word2Vec's idea has been used to design Doc2Vec ([paper](https://arxiv.org/pdf/1405.4053.pdf)), an algorithm that can create a numeric representation of a document, regardless of its length.

Category 3: Contextualized Word Embedding. Since context is considered in these models, the word representation dynamically varies based upon the surrounding words.
Models that use this kind of representation, like Transformers, are SOTA for most NLP tasks.These approaches are context-dependent, i.e. they can disambiguate polysemes, thanks to the [attention](https://arxiv.org/abs/1706.03762?context=cs) mechanism. This means that these models can compute different embeddings for a word depending on the context.
There are tons of models based on this architecture, but the most famous one is certainly [BERT](https://arxiv.org/pdf/1810.04805.pdf) which has been used in several applications in [NLP](https://arxiv.org/pdf/2103.11943.pdf) [NLP](https://arxiv.org/pdf/2010.00854.pdf) and in many [flavours](https://aclanthology.org/2020.emnlp-demos.6.pdf). An interesting variation of BERT for our work is [SBERT](https://arxiv.org/pdf/1908.10084.pdf), which, thanks to siamese and triplet network structures, can better derive sentences similarities. Since most of the proposed Transformer architectures have a limit on the number of tokens they can handle, document embeddings can be computed by dividing the text in chunks, finding the average of all the word embeddings in every chunk, and then averaging the chunks embeddings.

### 2.2) Review of Recent Studies
Topic modelling has its roots in the 1980s ([paper](https://www.sciencedirect.com/science/article/pii/S0306437920300703?casa_token=nJDJ5Nlh9T4AAAAA:2LmMdid6ESJ6R7T6UL5MlAkBP_b3kagZy9PgUQUTlNvAZFgqKvzpvHf5Z7jFOKyFbCyKXg#b14)), but really took off in the late 1990s thanks to methods such as [LSI](https://asistdl.onlinelibrary.wiley.com/doi/epdf/10.1002/%28SICI%291097-4571%28199009%2941%3A6%3C391%3A%3AAID-ASI1%3E3.0.CO%3B2-9?saml_referrer=) and especially [LDA](https://www.jmlr.org/papers/volume3/blei03a/blei03a.pdf?ref=https://githubhelp.com). Many methods based on LDA were designed over the last two decades ([cells](https://www.sciencedirect.com/science/article/pii/S0002929718301150) [hierachical](https://ieeexplore.ieee.org/abstract/document/8607040) [bioinformatics](https://d-nb.info/1116751054/34)). Despite their success, conventional Bayesian probabilistic topic models started to show signs of fatigue in the era of big data and deep learning [here](https://www.bing.com/search?q=topic+modelling+meets+deep+learing&cvid=99e100f4d08d4b0ba5f77714870cd94a&aqs=edge..69i57.7129j0j4&FORM=ANAB01&PC=U531).  Instead, models based on the use of Deep Learning techniques are becoming more and more popular ([survey](https://arxiv.org/abs/2103.00498)).
DL methods have been applied to topic modeling for document representation [LSTM](https://www.sciencedirect.com/science/article/abs/pii/S0950705119301182), for computing semantic representations of topics ([ATM](https://www.sciencedirect.com/science/article/abs/pii/S0306457319300500)) and to deal with short texts ([Attention](https://www.sciencedirect.com/science/article/pii/S1877050919306283) [survey](https://www.mdpi.com/1424-8220/22/3/852)).

The scientific community did not focus just on designing different methods that are then applied on traditional data (text), but in the years there has been a great effort in the application of topic modeling to different fields and for many purposes([LDA in various fields](https://link.springer.com/article/10.1007/s11042-018-6894-4)). Some interesting fields in which topic modeling has been used are: Marketing and Business management([AI](https://www.sciencedirect.com/science/article/pii/S0148296320307165?casa_token=CTXuKVFl_D4AAAAA:pO1BI9qqL7GEI3taA8mMPBaUwoDBryzpdBwzNjyL9rmDDt5hmbImS3xrm0lX6Q05XY1dybJ_xA) [Brands](https://journals.sagepub.com/doi/full/10.1177/10949968221088275) [marketing](https://link.springer.com/article/10.1007/s11573-018-0915-7) [Business analytics](https://www.sciencedirect.com/science/article/pii/S0378720617309254?casa_token=EtcTboz2mvEAAAAA:BR5vVJd4bRrnfAyxNOTMc6PllQ-oBSjpZBc4Pwv0gyNro0CYQhHaIpEXEM1HLqNJqkjzCnKdKw) [TM in Management research](https://journals.aom.org/doi/abs/10.5465/annals.2017.0099)), analysis of scientific publications ([COVID-19](https://www.jmir.org/2020/11/e21559) [Collaborative filtering](https://dl.acm.org/doi/abs/10.1145/2020408.2020480?casa_token=F_2xHH541asAAAAA:r-0r-Zigz5iZa8KgomJCP5tJG3jOBYvdXMePCg_MYr0HL_sOmkkSf8WMrhl1aUjh-iMhDekN1SjD) [Korea](https://koreascience.kr/article/JAKO201312855326461.page)), biology and medicine ([bioinformatics](https://springerplus.springeropen.com/articles/10.1186/s40064-016-3252-8) [biological and medicL datasets](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-15-S11-S11) [proteins](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-7-58)), [Software traceability](https://ieeexplore.ieee.org/abstract/document/6062077?casa_token=1fXi-6Dlo5gAAAAA:6259L_R_-_FReFTKM0KJztI60eJmKCxD_eQ5k34sVB8IHc4tJzC6unvRmF5Ol6dx64W-). 

In the tourism field there are publications in which topic modeling is used to discover preferences in travel itineraries ([here](https://www.sciencedirect.com/science/article/pii/S0261517719301268?casa_token=UpNSl5Bfl_sAAAAA:qzQVBCYYQf92agcRLozvZswTDS3Fo8zMsjaQRoCLHIegXNwFchyeYJM3Y-XovZw33gUYotVw6w)), to study customers opinions ([sentiment](https://www.tandfonline.com/doi/full/10.1080/19368623.2017.1310075?casa_token=C1gkPjUtESsAAAAA%3ACkoQnodjVC-2XNpop-F-CTXjGJ4g5Yyh31lIHqWlXLARpfcZTa1SGOruy_eBkwO2IaTy31Nt91vP) [hotel](https://www.sciencedirect.com/science/article/pii/S0261517719300020?casa_token=sKr7C-F5geUAAAAA:6P5kjPe36i5uT1EbZ1VU_w5AXeNWkN5UoqLlKIYqMZNX_Y5iNnrp17BySkt-OWj8zbRvG6BxFA)  [reviews](https://link.springer.com/article/10.1007/s40558-015-0035-y) [tripadvisor]([Mining meaning from online ratings and reviews: Tourist satisfaction analysis using latent dirichlet allocation - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0261517716301698?casa_token=rNu7wIeK6ZYAAAAA:udcc5pDK_g8AADXGTJouOYMTTxpLvlXdMPZWG2Xl9LXMOo85EdgfK8CJeOj_t1be-Zawmg))), bikesharing ([bike](https://link.springer.com/article/10.1007/s11067-017-9366-x#Tab1)) and to make recommendations ([geo topic model](https://dl.acm.org/doi/abs/10.1145/2433396.2433444?casa_token=ct2kPmAiUSQAAAAA:yihk4f46hwxdYcLqLE6jImF5ZZL7gFSII83VwZrovT0zaW1x4tt_LUPgmMu67IZ02cc0XhSWFrhv) [Collaborative filtering](https://link.springer.com/chapter/10.1007/978-3-319-14442-9_45)).



[Evaluation](https://link.springer.com/chapter/10.1007/978-3-030-80599-9_4#chapter-info)

# Usage of different embedding methods
Points:
- doc2vec should be better for large datasets with very unique vocabulary;
- doc2vec is language agnostic, but multiple language will not be aligned;
- universal sentence encoder is suggested for smaller and multilingual datasets;
- Doc2vec performs better;
- Results are really similar, except for universal-sentence-encoder which is way worse;
- Universal-sentence-encoder often finds just 2-3 topics and is really unstable in several tests;
- Chunking improves coherence but decreases diversity;
- With tourpedia, chunking reduces performances (by a lot) and the number of topics is small apart from universal-sentence-encoder which has 63.4 topics in average (against 10-12), diversity is 0.4 point worse, and coherence is a bit better. distiluse finds 23.1 topics and has a good diversity score, just 0.04 worse than the best test and best coherence scores.

Even if Top2Vec was initially designed to use Doc2Vec architecture to generate the embeddings of the documents and words, its framework offers other options. We tried these other models because they can handle multilingual datasets, and they are also suggested for smaller data sets by Top2Vec's authors. The models we tried are the following: universal-sentence-encoder-multilingual and distiluse-base-multilingual-cased. Also, we did some tests where the documents embeddings were computed by chunking the texts, obtaining the embeddings from such chunks, and then averaging the embeddings into one final representation. This should help in case of long texts and when the embedding model has a token limit. 
All the tests were done on the easytour dataset, because it is the only one not in English. The results of the tests we made are shown in the table []. Those were obtained by averaging the results of 10 iterations of the same test.
Using universal-sentence-encoder often leads to find just 2-3 topics and the test are really unstable (several tests with same parameters can give results that are really different from each other). The fact that this version has high scores for diversity are given by the fact that it find just a couple of topics.
Even if the results are generally quite similar, we can definitely say that Doc2Vec is the best performing model and universal-sentence-encoder is (by far) the worst one. Chunking improves coherence but decreases diversity.

## References
1. [[Background for Topic Modeling]]

## Code
1. 

#### Tags
#paper #topicmodeling 

# Datasets
Since the dataset is, of course, the main factor that influences the quality of the topics, in this work we do not compare the models using just some quantitative and qualitative metrics, but we also use datasets with very different characteristics to highlight the strengths and the weaknesses of the models in several situations.
The statistics of the datasets are shown in table [].

## Tourpedia
TourPedia (TP) is a publicly available dataset related to tourism places and reviews about those sites extracted from several social media (Facebook, Foursquare, Google Places and Booking). The places include accommodations, restaurants, points of interest, and attractions. TourPedia was born within the project OpeNER, funded by the 7th Framework Program of the European Commision. 
At the moment eight places are covered: Amsterdam, Barcelona, Berlin, Dubai, London, Paris, Rome and Tuscany. We extracted 8000 reviews, 1000 for each location through the provided Web API.


## Easytour
EasyTour (ET): To analyze the multi-lingual aspect of the topic models, we have considered a unique dataset based on Italian Language. It has 5724 entries, each having 30 attributes such as id, document type, title, description, locations, duration, images, distance, publishing date and more. The dataset consists of data related to tourist services and POIs, for the Italian touristic experiences. The dataset is obtained from the beta testing phase of the app KuriU for the EasyTour project, which is in the development phase. 

## Preprocessing
Some of the models considered in this work need preprocessed documents to work properly. The steps we did are the following:
- removal of stopwords, digits, words that are shorter than three letters (nltk);
- removal of emojis using the demojize function from the emoji library;
- hashtags removal using regular expressions;
- punctuation removal;
- removal of verbs, adjectives and adverbs (spacy)

The statistics of the preprocessed datasets are shown in table [].



# Open Issues and Future Research Directions
- Metrics that consider semantic [here](https://anjiefang.github.io/papers/fang_sigir_2016_we.pdf) or [here](https://link.springer.com/content/pdf/10.1007/978-3-030-80599-9.pdf);
- How embedding method influences the topic model;
	- neural topic modeling approaches are not perfect in case of short texts or small datasets. Some solutions:
		- [here](https://aclanthology.org/2020.emnlp-main.138.pdf)
		- [here](https://arxiv.org/abs/1809.03664)
	- which embedding method use?
- Issues in Tourism field [here](https://www.mdpi.com/2076-3417/9/16/3300)[here](https://www.sciencedirect.com/science/article/pii/S0261517720301679?casa_token=2cACzkbhoCYAAAAA:YRkqpAinlh4JphpnWF2wJOgnPOBO9kpdPOI9bKFzQo1PHokMPELET5uEjTJeaquvCe6VCFJ3bY0):
	- Lack of standard touristic datasets;
	- need of large and labelled data for neural topic modeling approaches;
	- languages;
	- knowledge transfer (Transfer learning?);
	- Deep learning approaches are black box → explainability and new metrics;
	- cold start problem (use transfer learning or multi modality)
- Future direction of our study:
	- dynamic topic modeling
	- mining of touristic attractions
	- neural topic modeling with short texts

1) Issues in touristic topic modeling [here](https://www.mdpi.com/2076-3417/9/16/3300)[here](https://www.sciencedirect.com/science/article/pii/S0261517720301679?casa_token=2cACzkbhoCYAAAAA:YRkqpAinlh4JphpnWF2wJOgnPOBO9kpdPOI9bKFzQo1PHokMPELET5uEjTJeaquvCe6VCFJ3bY0):
2) datasets [here](https://www.mdpi.com/2076-3417/9/16/3300):
	1) lack of standards;
	2) large and labelled data for neural TM [here](https://aclanthology.org/2020.emnlp-main.138.pdf) [here](https://arxiv.org/abs/1809.03664);
	3) languages [here](https://www.researchgate.net/publication/220895498_Knowledge_Transfer_across_Multilingual_Corpora_via_Latent_Topics)
3) NTM are black boxes:
	1) transfer learning [here](https://arxiv.org/abs/1301.5686);
	2) knowledge transfer;
	3) knowledge graphs [here](https://aclanthology.org/N19-1099/) [here](https://ojs.aaai.org/index.php/AAAI/article/view/10951);
	4) new metrics [here](https://anjiefang.github.io/papers/fang_sigir_2016_we.pdf) or [here](https://link.springer.com/content/pdf/10.1007/978-3-030-80599-9.pdf)
4) cold start:
	1) transfer learning;
	2) multi modality

The issues for topic modeling applied to the touristic field are several and known, as reported by different works [here](https://www.mdpi.com/2076-3417/9/16/3300)[here](https://www.sciencedirect.com/science/article/pii/S0261517720301679?casa_token=2cACzkbhoCYAAAAA:YRkqpAinlh4JphpnWF2wJOgnPOBO9kpdPOI9bKFzQo1PHokMPELET5uEjTJeaquvCe6VCFJ3bY0)[here](https://www.longdom.org/open-access/big-data-in-tourism-general-issues-and-challenges-83559.html).
Foremost, there is a lack of standards about the datasets compared to other fields [here](https://arxiv.org/abs/2101.03020). New topic modeling approaches based on deep learning needs large and often labelled data, which are often not available for this field. Furthermore, most of the time, the documents are particularly short, and this aspect can heavily influence the performances. There have been attempt [here](https://aclanthology.org/2020.emnlp-main.138.pdf) [here](https://arxiv.org/abs/1809.03664) to deal with this last issue, but the problem is still open.
A general problem for Neural Topic Models is that they are to be considered as black boxes, and so the use of such models leads to a loss of interpretability of the results. As we did in our work, there are metrics in topic modeling that can help to evaluate the results, but new metrics that consider word embeddings [here](https://anjiefang.github.io/papers/fang_sigir_2016_we.pdf) [here](https://link.springer.com/content/pdf/10.1007/978-3-030-80599-9.pdf) could be used to better evaluate this new kind of approaches.
A last issue regards cold start, especially in fields that does not have a variety of public available datasets, like the touristic one. There could be several methods that can help alleviate this problem, as the usage of knowledge graphs [here](https://aclanthology.org/N19-1099/) [here](https://ojs.aaai.org/index.php/AAAI/article/view/10951), transfer learning [here](https://arxiv.org/abs/1301.5686) for the approaches based on deep learning and the usage of side information [here](https://proceedings.mlr.press/v51/hu16c.html) or multimodal data [here](https://dl.acm.org/doi/abs/10.1145/2783258.2783293?casa_token=Hfv3ulD6cfoAAAAA:S3XP8Y5TZPdE1H7YpvGq7_M_5ZjEOO7u7ks7YtV6Nd70XbAqtpPGkciUUobAwk2yDfimdiSRbMfkVg).

An aspect that is certainly important for the touristic field and that is not considered in our work is the strong connection between data consumed by the users and the period in which such content is used. An interesting continuation of our work could consider the dynamic aspect of the data to detect which topics are important in a determined period of time.
