It is a form of regression, that constrains/ regularizes or shrinks the coefficient estimates towards zero. This technique is used to discourage learning a more complex model.

### Ridge Regression
$R=\lambda \sum^{p}_{j=1}\beta_j^2$ is the formula that shows ridge regression, where the loss is modified by adding the shrinkage quantity. Here, $\lambda$ is the tuning parameter that decides how much we want to penalize the flexibility of our model.
When $\lambda = 0$, the penalty term has no effect, and the estimates produced by ridge regression will be equal to loss. However, as $\lambda→∞$, the impact of the shrinkage penalty grows, and the ridge regression coefficient estimates will approach zero. As can be seen, selecting a good value of $\lambda$ is critical. Cross validation comes in handy for this purpose. The coefficient estimates produced by this method are also known as the **L2 norm**.
One disadvantage of ridge regression is that it shrinks the coefficients for least important features, but it does not reduce them to zero, i.e. they will be included in the final model.

### Lasso Regression
$R=\lambda \sum^{p}_{j=1}|\beta_j|$ is the formula for lasso regression, which consists in penalizing the high coefficients. It is also known as **L1 norm**.


### References
1. [Medium](https://towardsdatascience.com/regularization-in-machine-learning-76441ddcf99a)