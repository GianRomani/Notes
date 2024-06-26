Created: 2024-06-24 15:58
#paper
## Main idea
The paper shows how to 'steal' closed-sourced embeddings model served via API by training local [[BERT]]-based models with text/embedding pairs obtained from those services. The authors also show how distilling from several providers could help to train stronger models.
The assumption is that the attacker has only black-box access to the model, meaning they are unaware of the model’s initialization, architecture, or training process. The attacker could use some public information about the model.

The tested APIs are *text-embedding-3-large* from OpenAI and *embed-english-v3.0* from Cohere.
## In deep
### Models
Cohere's model is likely based on the BERT architecture, while the OpenAI one is not (but we do not have any info about it, only that they used Matryoshka Representation Learning during training).

The models used in these paper to replicate the performance of the stolen ones are:
1. Contriever;
2. BERT base uncased.

**NOTE**: Contriever is based in BERT base uncased and further trained to be able to perform dense retrieval in an unsupervised setting.

When distilling both from OpenAI’s and Cohere’s models, the authors prepends “Query: ” or “Document: ” to the text depending on whether they are embedding a query or a document (Cohere API has the parameter *input_type* that is used to specify the task of the retriever, OpenAI does not have this feature).

One issue with the distillation to BERT is that both APIs produce embeddings with too many dimensions (more than 768) for BERT. To solve this, a linear transformation using a learnable linear layer is used to produce embeddings of the right dimension.
### Data
The data used to train the distilled model comes from *MSMARCO v1* passage ranking dataset. The 8.8 million passages in the corpus and the 809k queries in the training set are used as training set. Some preprocessing was done to remove duplicates and to build a development set.

From this set of data several subset are created to establish the improvements over time of the thief model. In total there are 4 subsets (100k, 200k, 400k, full data).
### Loss
To distill the embeddings from the teacher model to the student model, a simple cosine distance loss is used: $l = 1-\frac{1}{n}\sum_{i=1}^{n}\frac{t_i \cdot s_i}{\lVert t_i \rVert_2 \cdot \lVert s_i \rVert_2}$, where $t_i$ is the embedding from the attacked model (i.e. Cohere or OpenAI) and $s_i$ is the output of the thief model (both for the same text).

### Experiments
Some details for the trainings:
- dropout of 10%;
- *AdamW* with weight decay of 0.01 and linear warmup of 500 steps;
- learning rate of 1.5e-4 for datasets smaller than 400k samples, 1e-4 for bigger ones.

Hyper-parameters are indicative and the authors did not optimize them. They also noticed that the models continuously improve (for <400k samples they trained for more than 150 epochs, for the biggest datasets they stopped after 50).

## Results
Evaluations were done on *TREC 2019 and 2020*  Deep Learning Tracks from the *MSMARCO v1* passage ranking task and on *BEIR* (to evaluate the generalization on out-of-domain data).

The tasks used for evaluation are the followings:
1. thief model is used to encode the queries and retrieval is done on passages encoded by the API
2. thief model encodes both the queries and the corpora for retrieval

The evaluation metrics are: **nDCG@10** (Normalized Discounted Cumulative Gain at rank cutoff 10) and **R@100** (Recall at rank cutoff 100).

Employing thief models for just encoding search queries typically results in superior information retrieval performance compared to using them for encoding both queries and the text corpus. This is likely attributed to the fact that these thief models are imperfect substitutes for the more powerful API models, which are specifically optimized for generating embeddings for effective retrieval. By limiting the use of thief models to query encoding alone, there is less opportunity for errors to arise compared to when they are used for encoding both queries and passages.

About the usage of subsets of data with different sizes, the obvious observation to be made is that as the amount of training data is increased, the thief models better approximate the embedding models that they steal from.

Another observation is that it is easier to steal the model from Cohere, compared to OpenAI, probably because the first one was initialized with a BERT model as the thief one.

A final set of tests was done for a case in which we want to use both APIs to distill a local model. The approach consists in concatenating the vectors from Cohere’s and OpenAI’s embedding models and attempt to distill these concatenated embeddings into the model. The results seem promising, but the tests are not very detailed.

At the end, stealing data from both APIs has a cost of ~$216.

## Defense
The main proposed idea are about secrecy of the models: do not share too many details about the backbone used (as results in this paper were better when thief models shared the backbone with the attacked model) or other aspects of the system (authors are inferring the backbone of Cohere's model by a tokenizer in Hugging Face and using a dataset of MSMarco embeddings released by Cohere).

## References
1. [Paper](https://arxiv.org/pdf/2406.09355)
## Tags
#aisecurity #llm 
