Created: 2023-03-06 09:30
#quicknote

Cross-entropy is a measure of the difference between two probability distributions for a given random variable or set of events.

In information theory it is interesting to describe how much information an event contains -> a *low probability event* carries more information compared to an *higher probability event*.

Information $h(x)$ can be calculated for an event $x$, given the probability of the event $P(x)$
 as follows: $h(x)=-log(P(x))$.

**Cross-entropy** builds upon the idea of [[Entropy]] from information theory and calculates the number of bits required to represent or transmit an average event from one distribution compared to another distribution.

The ==intuition== for this definition comes if we consider a target or underlying probability distribution P and an approximation of the target distribution Q, then the cross-entropy of Q from P is the number of additional bits to represent an event using Q instead of P.

Cross -entropy can be computed as follows: $H(P,Q) = – \sum_{x \in X}P(x) log(Q(x))$, where P(x) is the probability of the event x in P, Q(x) is the probability of event x in Q and log is the base-2 logarithm, meaning that the results are in bits. If the base-e or natural logarithm is used instead, the result will have the units called nats.

The result will be a positive number measured in bits and will be equal to the entropy of the distribution if the two probability distributions are identical.

___
Cross-entropy is related to divergence measures, such [[Kullback-Leibler divergence]], that quantifies how much one distribution differs from another. Specifically, the KL divergence measures a very similar quantity to cross-entropy. It measures the average number of extra bits required to represent a message with Q instead of P, not the total number of bits:

-   **Cross-Entropy**: Average number of total bits to represent an event from Q instead of P.
-   **Relative Entropy** (_KL Divergence_): Average number of extra bits to represent an event from Q instead of P.

We can calculate the cross-entropy by adding the entropy of the distribution plus the additional entropy calculated by the KL divergence. This is intuitive, given the definition of both calculations; for example: $H(P,Q) = H(P) + KL(P||Q)$, where H(P, Q) is the cross-entropy of Q from P, H(P) is the entropy of P and KL(P || Q) is the divergence of Q from P.

**NOTE:** like KL divergence, cross-entropy is not symmetrical.

___
Cross-entropy is widely used as a loss function when optimizing classification models.
Two examples that may be encountered include the logistic regression algorithm, and artificial neural networks that can be used for classification tasks.

For example, in a classification problem, each example has a known class label with a probability of 1.0, and a probability of 0.0 for all other labels. Then a model can estimate the probability of an example belonging to each class label. Cross-entropy can then be used to calculate the difference between the two probability distributions:
-   **Expected Probability** ($y$): The known probability of each class label for an example in the dataset (P).
-   **Predicted Probability** ($\hat{y}$): The probability of each class label an example predicted by the model (Q).

When calculating cross-entropy for classification tasks, the base-e or natural logarithm is used. This means that the units are in nats, not bits.
We are often interested in minimizing the cross-entropy for the model across the entire training dataset. This is calculated by calculating the average cross-entropy across all training examples.

___
**NOTE:** Cross-Entropy is not [[Log Loss]], but they calculate the same quantity when used as loss functions for classification problems.


## Resources
1. [Machine Learning Mastery](https://machinelearningmastery.com/cross-entropy-for-machine-learning/)
2. [Wikipedia](https://en.wikipedia.org/wiki/Cross_entropy)
3. [Towards Data Science](https://towardsdatascience.com/cross-entropy-for-classification-d98e7f974451)

#### Tags
#measure #ml