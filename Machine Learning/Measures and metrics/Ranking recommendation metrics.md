Created: 2022-03-23 12:32

Average Precision at k (AP@K) s a measure of the average relevance scores of a set of the top-K recommendations presented. Its formula is $$AP@K = \dfrac{1}{m}\sum_{i=1}^{K}P(i)rel(i)$$ where rel(i) is just an indicator that says if the i-th item was relevant.

MAP@K tells us how relevant the list of recommended items are. It consists in the mean of the Average Precision
MAR@K tells us how well the recommender is able to recall all the items the user has rated positively in the test set. It consists in the mean of the Average Recall.

## References
1. https://www.sciencedirect.com/science/article/pii/S0950705113001044#b0940
2. http://sdsawtelle.github.io/blog/output/mean-average-precision-MAP-for-recommender-systems.html
3. https://jonathan-hui.medium.com/map-mean-average-precision-for-object-detection-45c121a31173

## Code
1. https://github.com/benhamner/Metrics
2. https://github.com/statisticianinstilettos/recmetrics

#### Tags
#ranking_metrics #precision #map #mar #recall #recsys 