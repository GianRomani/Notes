Created: 2022-12-02 15:32
#note

It is a method to reduce the dimensionality of the feature space. In particular, it consists in feature extraction, instead of feature elimination (we drop some features, but we still retain the most valuable parts of all the variables).

The main is that when our data has a higher variance, it holds more information. So, we want that the greatest variance by some projection of the data comes to lie on the first coordinate, the second-greatest variance on the second coordinate and so on. We keep just the N greatest components.

Reducing dimensions with PCA changes the distances of our data, especially the smallest (pairwise) ones. This could be one **drawback** of PCA.

## References
1. [Towards Data Science](https://towardsdatascience.com/a-one-stop-shop-for-principal-component-analysis-5582fb7e0a9c)
2. [Towards Data Science 2](https://towardsdatascience.com/principal-component-analysis-pca-explained-visually-with-zero-math-1cbf392b9e7d#:~:text=Principal%20component%20analysis%20(PCA)%20is%20a%20technique%20that%20transforms%20high,and%20third%20principal%20components%2C%20respectively.)