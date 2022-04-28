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

## References
1. [Survey](https://link.springer.com/content/pdf/10.1007/s13042-017-0762-9.pdf)
2. https://www.sciencedirect.com/science/article/pii/S0950705113001044#b0940
3. https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9354169&tag=1


#### Tags
#evaluation_metrics
