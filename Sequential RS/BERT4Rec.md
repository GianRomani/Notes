# BERT4Rec
Created: 2022-06-20 17:23
#paper
## Main idea
BERT4Rec is a lot like regular BERT for NLP. In this case the Transformer network is trained to predict masked items (Cloze Task) from a user’s history. Then, the self-attention is what allows this architecture to model long-range dependencies between elements of the input sequence.
To use the Cloze task in a sequential recommender the authors added the special masked token to the end of each input sequence to represent the item that has to be recommended and then made recommendations base on its final hidden vector.
## In deep

## References
1. [Paper](https://arxiv.org/pdf/1904.06690.pdf)
2. [Towards Data Science](https://towardsdatascience.com/build-your-own-movie-recommender-system-using-bert4rec-92e4e34938c5)

## Code
1. [GitHub](https://github.com/FeiSun/BERT4Rec?utm_source=catalyzex.com)
