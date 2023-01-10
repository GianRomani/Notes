# Losses
Created: 2022-04-25 11:50
#note

We often use "cost function" and "loss function" as synonymous, but they are different:
- loss function: it is for a single training example/input;
- cost function: it is the average loss over the entire training dataset.

### Regression
#### Mean Squared Error
Also called squared loss or L2 loss.
It is the simplest and most common loss function: $MSE = \frac{1}{N}\sum_i^N(y_i-\hat{y_i})^2$.
**Advantages**:
- Easy to interpret;
- Always differential because of the square;
- Only one local minima
**Disadvantages**:
- Error unit in the square;
- Not robust to outlier

#### Mean Absolute Error
Also called L1 loss. It is also very simple: $MAE = \frac{1}{N}\sum_{i=1}^N|y_i-\hat{y_i}|$.
**Advantage**:
- intuitive and easy;
- robust to outlier
**Disadvantages**:
- Not differential

#### Huber Loss
It is used because it is less sensitive to outliers than squared error loss.
$\begin{cases}Huber=\frac{1}{n}\sum_{i=1}^n\frac{1}{2}(y_i-\hat{y_i})^2 \quad |y_i-\hat{y_i}|\leq \delta\\ Huber= \frac{1}{n}\sum_{i=1}^n\delta(|y_i-\hat{y_i}|-\frac{1}{2}\delta)\quad |y_i-\hat{y_i}|>\delta\end{cases}$
Where $n$ is the number of data points, $y$ is the ground truth, $\hat{y}$ is the predicted value, and $\delta$ defines the point where the Huber loss function transitions from a quadratic to linear.
**Advantages**:
- Robust to outliers;
- It is considered as in the middle between MAE and MSE
**Disadvantages**:
- It is complex and also $\delta$ has to be optimized (in addiction to the other parameters).

### Classification Loss


### Other losses
**Pointwise loss**: minimization of the squared loss between predicted score $y_{u,i}$ and target value $y(u,i)$. To use negative feedback, all unobserved entries are considered as negative examples or some unobserved entries are sampled to be negative instances.

**Pairwise loss**: aims to rank observed entries higher than the unobserved ones by maximizing the margin between observed entries and unobserved entries.

## References
1. [Overview](https://www.analyticsvidhya.com/blog/2022/06/understanding-loss-function-in-deep-learning/)

#### Tags
#loss