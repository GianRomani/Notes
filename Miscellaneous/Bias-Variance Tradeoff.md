# Bias-Variance Tradeoff
Created: 2022-12-02 14:23
#note

**Bias:** it is the difference between the average prediction of our model and the correct value which we are trying to predict. High bias indicates an oversimplified model. It is evident in case of high error on training data and test data.

**Variance:** it refers to the variability of the predictions on the data points. High variance indicates that the model has trained very well on the training data, but it did not generalize on the unseen data. This is the case of [[Overfitting]].

![[bias_variance.png]]

**Underfitting:** it happens when the model is unable to capture the underlying pattern of the data. These models usually have high bias and low variance.

**Overfitting:** it happens when our model captures the noise along with the underlying pattern in data, i.e. models has great performance on training data but not on test data.

We need a good balance between bias and variance to have a good model.

Total error = Bias^2 + Variance + Irreducible error
![[bias_variance_tradeoff.png]]

## References
1. [Towards Data Science](https://towardsdatascience.com/understanding-the-bias-variance-tradeoff-165e6942b229)

## Code
1. 

#### Tags
#ml 
