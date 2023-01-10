# Naive Bayes method
Created: 2023-01-10 10:45
#note

Naive Bayes classifier is a probabilistic ml model used for classification task.
It is based on the Bayes Theorem: $P(A|B)=\frac{P(B|A)P(A)}{P(B)}$, where *B* is the evidence and *A* is the hypothesis.

It is called Naive because the assumption that states that every feature is independent of each other has to be made.
So we have that $P(y|x_1,...,x_n)=\frac{P(y)P(x_1,...,x_n|y)}{P(x_1,...,x_n)}=\frac{P(y)\prod_{i=1}^nP(x_i|y)}{P(x_1,...,x_n)}$ , and since $P(x_1,...,x_n)$ is constant given the input, we can state that $\hat{y}=\arg\max_y P(y)\prod_{i=1}^n P(x_i|y)$. $P(y)$ $P(x_i|y)$ can be estimated using Maximum A Posteriori (MAP) and the former is the relative frequency of class *y* in the training set.

In spite of their apparently over-simplified assumptions, naive Bayes classifiers have worked quite well in many real-world situations, famously document classification and spam filtering. They require a small amount of training data to estimate the necessary parameters.
They are also very fast.

On the flip side, although naive Bayes is known as a decent classifier, it is known to be a bad estimator, so the probability outputs are not to be taken too seriously. Also, we cannot always have all the simple and conditioned probabilities.

Types of Naive Bayes Classifier:
- Multinomial Naive Bayes: the most used for document classification problem. The frequency of the words are used as features;
- Bernoulli Naive Bayes: similar to the multinomial naive Bayes, but the predictors are boolean variables;
- Gaussian Naive Bayes: used when the predictors take up a continuous value.


## References
1. [ML questions](https://www.interviewbit.com/machine-learning-interview-questions/)
2. [TDS](https://towardsdatascience.com/naive-bayes-classifier-81d512f50a7c)
3. [Notes on Internet](https://www.andreaminini.com/ai/machine-learning/algoritmo-naive-bayes)

## Code
1. [SKlearn](https://scikit-learn.org/stable/modules/naive_bayes.html)

#### Tags
#ml #supervised #bayes #classifier