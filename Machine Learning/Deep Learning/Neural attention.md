Created: 2022-03-24 10:18

Attention = vector of importance weights that predicts the next item -> the system can focus on a particular element to make recommendations by avoiding noisy or uninformative content.
It can be integrated with [[CNN]].

Types:
- vanilla attention models use parametrized context vector to learn to attend. In this [paper](https://cseweb.ucsd.edu/classes/fa17/cse291-b/reading/Attentive%20Collaborative%20Filtering%20Multimedia%20Recommendation%20with%20Item-%20and%20Component-Level%20Attention.pdf) attention is used in two levels: an item-level to select the most representative items to characterize users and a component-level level that captures the most informative features from multimedia auxiliary information for each user;
- co-attention model learn attention weights from two-sequences (self-attention is a type of co-attention). It performs better than [[CNN]] and [[RNN]] in sequential recommendation task. Example is [this paper](https://arxiv.org/pdf/1808.06414.pdf).


## References
1. https://medium.com/sciforce/deep-learning-based-recommender-systems-b61a5ddd5456


#### Tags
#neural_attention