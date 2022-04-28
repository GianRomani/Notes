# Metrics
Created: 2022-03-23 12:22

Use validation techniques (k-fold cross validation or leave one out cross validation in case of [[Cold-start]])

There are several aspects to consider:
- [[Accuracy]];
- [[Similarity]];
- [[Ranking recommendation metrics]];
- [[Set recommendation metrics]];
- [[Diversity metrics]];
- [[Stability and reliability]];

This [survey](https://link.springer.com/content/pdf/10.1007/s13042-017-0762-9.pdf) on evaluation methods for RS define 6 concepts for assessment of RSs:
- utility;
- novelty;
- diversity;
- unexpectedness;
- serendipity;
- coverage.

### Utility
It represents the value that users receivesin being recommended -> if the user enjoys the recommended items, he/she received useful recommendations. One way to measure utility is by evaluating the rating the user gives to predicted items after consuming them, but this could be costly for an online evaluation. In offline evaluation we can use predictive accuracy metrics like:
- Mean absolute error (**MAE**), which consists in the difference between the ratings predicted by the recommender and given by the users;
- Root mean squared error (**RMSE**), average RMSE, average MAE, mean squared error;
- **Precision** (number of consumed or rated items in the recommendation list) and **recall** (number of consumed items in the recommendation list out of the total number of items the user consumed). Precision@N and Recall@N stands for the size of the recommendation list.
- **ROC** curves measure the rate of items that the user likes in the recommendation list. Differently from error, precision and recall, this method accentuate items that were suggested but the user disliked.
- Ranking metrics -> they considere the fact that the users don't browse through all the recommended items. **R-score** metric for example consider a deduction in the value of recommendations according to the rank position (top ranked items are valued more), its formula is: $util(R_u)= rank(R_u)= \sum_{j=1}^{|R_u|} \dfrac {max(r(i_j)-d,0)}{2^{\dfrac{j-1}{a-1}}}$. Other ranking scores are Kendall and Spearman rank correlation and Normalized Distance-based Performance Measure;
- Online evaluation: Click-through-rate (**CTR**) is calculated as the ration of clicked/interacted recommended items out of the number of items recommended. **Retention** measures the impact of the recommender system in keeping users consuming items or using the system, it is often used with A/B testing.

### Novelty
It involves the idea if having novel items in the recommendation. Since there are several definitions for novelty (and so metrics), we can classify it into three levels:
1. Life level novelty -> a recommended item is novel in the life of the user, i.e. the user has never heard of the item in his/her life. This is the hardest level to evaluate, since we could have to consider information out of the system's context in order to measure what the user knows and do not know.
2. System level novelty -> recommended item is unknown for the user according to the user's history consumption. A classic metric was proposed by Nakatsuji et al., which calculates novelty in the recommendation list as the similarity between the items in the recommendation list and in the history of the user ($H_u$), $nov(R_u)= \sum_{i \in R_u} min_{j \in H_u} d(class(i), class(j))$. Another metric considers the sum of the popularity of the items in the recommendation list of the user, where popularity (*pop*) is the number of users that consumed the item, $nov(R_u)= \sum_{i \in R_u} \dfrac{\log_2pop(i)}{|R_u|}$.
3. Recommendation list level novelty -> non redundant items in the recommendation list. No users' information is required in this level. One metris is given by: $nov(R_u)= \dfrac{1}{|R_u|-1} \sum_{j \in R_u} 1-d(i,j)$ where d(i,j) means the distance between items i and j. In [this](https://dl.acm.org/doi/pdf/10.1145/2043932.2043955?casa_token=DOY1g0lsqp0AAAAA:dHLeA2RB8SxzBL_Nt34YfP6jW10spU_pd9vosmuqLQ_6XRVb2SA4IXCBQ3Bw_6mR6xMEnsv-Qw) paper the following metric is proposed: $nov(R_u)= \sum_{k=1}^{|R_u|} disc(k)(1-p(seen|i_k))$, where $disc(i_k)$ is a discount of browsing through the list and $p(seen|i_k)$ is the probability of the user has seen the item while browsing.

### Diversity
Diversity means balancing recommendation lists to cover the user's whole set of interests. One way to compute the diversity is using: $div(R_u)= \sum_{i \in R_u} \sum_{j \in R_u, i!=j}d(i,j)$, where $d(i,j)$ measures the distance between two items (cosine distance can be used). Another approach is given by [this](https://dl.acm.org/doi/pdf/10.1145/2043932.2043955?casa_token=kUsCAgf5kWQAAAAA:pVl1Uxnx_lyUAaC5xAjpQLL0OHDCLzzIRJ9q4MyObUagn7q3J8rT-xfPncql5bU8Rbfk_ipOjg) paper, in which a relative rank discount function of each pair of items is used (disc(k) and disc(l|k)); moreover the metric uses a distance function between the items (cosine), the formula is: $div(R_u)= \sum_{k=1}^{|R_u|} \sum_{l=1}^{|R_u|} disc(k)disc(l|k)d(i_k,i_l) \forall i_k \neq i_l$.

### Unexpectedness
Originally it was stated as a component of serendipity. It has been defined as *divergence from expected recommendations* Two sets of metrics have been proposed:
1. Primitive recommender based unexpectedness: unexpectedness can be considered as a deviation from expected recommendations -> $unexp(R_u)=R_u - PM_u$, where $PM_u$ is a set of recommendations made by a primitive recommender (a recommedner that predicts items taht the user expects to consume). The rate of such unexpected items can be measured by the following metric: $unexp(R_u) = \dfrac{R_u - PM_u}{|R_u|}$. The main problem consists into finding the right primitive recommender;
2. Non primitive recommender based unexpectedness: we could use the Point-wise mutual information function ($PMI(i,j)=\dfrac{\log_2{\dfrac{p(i,j)}{p(i)p(j)}}}{-\log_2{p(i,j)}}$) which calculates the probability of two items *i* and *j* be rated by the users. Using PMI we can compute unexpectedness as: $unexp(R_u)= \sum_{i \in R_u} \sum_{j \in H_u} PMI(i,j)$ or $unexp(R_u)= \sum_{i \in R_u} max_{j \in R_u}PMI(i,j)$. There are also unpersonalized metric for unexpectedness that does not consider the users' information, instead they use the idea of co-occurence.

### Serendipity
It is related to lucky findings or satisfying surprises. There are two kinds of metrics for serendipity:
1. Primitive recommender based: a first metric is given by: $ser(R_u) = \sum_{k=1}^{|R_u|}max(R_u[k] - PM_u[k],0)rel(i_k)\dfrac{count_k(k)}{k}$, where PM is the primitive recommender and *rel* is a function that calculates if the predicted items are relevant to the user or not. This other metric uses $UNEXP_u = R_u - PM_u$, which represents the surprising items for the user *u*, but not the ranking of the items : $ser(R_u) = \dfrac{\sum_{i \in UNEXP_u}utility(i)}{|R_u|}$. A third metric is: $ser(R_u)= \dfrac{(R_u - E_u) \cap USEFUL_u}{|R_u|}$ where *USEFUL* is the set of useful items and *E* is the set of expected items.
2. Non primitive recommender based: one metric used is the following: $ser(R_u)= \dfrac{1}{|H_u|} \sum_{i \in H_u} \sum{j \in R_u} \dfrac{cossim(i,j)}{|R_u|}$, where we are considering the cosine similarity between the recommended items and the history of consumption of the user (*H*). This metric does not consider the usefulness of the recommendations.

The first group of metrics is really sensitive to the choice of the primitive recommender -> the second group could be useful if associated with metrics that consider usefulness of recommended items.

### Coverage
Three kinds of coverage are considered:
1. Item space coverage: it refers to the extent of items that a recommender system is able to make predictions -> set of items that the RS is capable of working with. There are few metrics since coverage is not really used.
2. User space coverage: it refers to the proportion of users that a RS can predict items to. No metrics found.
3. Genre space coverage: it refers to the number of distinct genres of items that are effectively recommended to users.


## References
1. [Survey](https://link.springer.com/content/pdf/10.1007/s13042-017-0762-9.pdf)
2. https://www.sciencedirect.com/science/article/pii/S0950705113001044#b0940
3. https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9354169&tag=1


#### Tags
#evaluation_metrics
