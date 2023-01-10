# Curse of dimensionality
Created: 2022-12-02 15:14
#note

It is a phenomenon that happens when data increases in dimensions and, by consequence, the computational effort required to process the data increases.

It would be normal to think that by adding more information to the data, the quality of the data itself would increase, but practically it is the noise that increases. In fact, as the dimensionality increases, the number of data points required for good performance of any machine learning algorithm increases exponentially.
Also, for a d-dimensional space, any two given points are equidistant to each other ($lim_{dim \rightarrow \infty}(dist_{max(A)}-dist_{min(A)})/(dist_{min(A)})\rightarrow 0$). So, any ML algorithm based on distance measure tend to fail when the number of dimensions in the data is very high.

**Solutions:**
- use different measure of distance rather than the Euclidean one. Cosine similarity is generally better with higher dimensional data;
- Forward-feature selection: select the most useful subset of features;
- Dimensionality reduction: [[PCA]], t-SNE, SVD, [[UMAP]] can reduce the dimensionality while preserving data characteristics and geometry.


## References
1. [Towards Data Science](https://towardsdatascience.com/curse-of-dimensionality-a-curse-to-machine-learning-c122ee33bfeb)
2. [TDS 2](https://towardsdatascience.com/why-and-how-to-get-rid-of-the-curse-of-dimensionality-right-with-breast-cancer-dataset-7d528fb5f6c0)

## Code
1. 

#### Tags