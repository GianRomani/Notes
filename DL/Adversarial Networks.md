Created: 2022-03-24 16:15

There are two schools of thinking in #ir:
- generative retrieval assumes that there is a common generative process between documents and queries, so a retrieval task can be performed by generating the relevant document *i* given the query *q*;
- discriminative retrieval learns to predict the relevance score given labelled relevant query-document pairs.


[IRGAN](https://arxiv.org/pdf/1705.10513.pdf) is the first model which applies GAN to RecSys (and other IR tasks, such as web search and question answering). It combine the two approaches above by generating relevant documents similar to the ground truth to fool the discriminative retrieval model.

## References
1. https://arxiv.org/pdf/1707.07435.pdf
2. https://arxiv.org/pdf/1705.10513.pdf


#### Tags
#adversarial_networks #gan