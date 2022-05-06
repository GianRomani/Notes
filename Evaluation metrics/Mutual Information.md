# Mutual Information
Created: 2022-05-06 14:05
#note
In probability theory and information theory, the mutual information of two random variables is a measure of the mutual dependence between the two variables, i.e. it quantifies the amount of information obtained about one random variable by observing the other random variable.
MI determines how different the joint distribution of the pair (X,Y) is from the product of the marginal distributions of X and Y.
MI is the expected value of the poinwise mutual informatoin (PMI).

### PMI
It is a measure of association.
The PMI of a pair of outcomes x and y belonging to discrete random variables X and Y quantifies the discrepancy between the probability of their coincidence given their joint distribution and their individual distributions, assuming independence.
$pmi(x,y)=\log(\dfrac{p(x,y)}{p(x)p(y)})=\log(\dfrac{p(x|y)}{p(x)})=\log(\dfrac{p(y|x)}{p(y)})$

#### Normalized pointwise mutual information (npmi)
 Pointwise mutual information can be normalize between [-1;+1] resulting in -1 (in the limit) for never occurring together, 0 for independence, and +1 for complete co-occurrence.
 $npmi(x;y)= \dfrac{pmi(x;y)}{h(x;y)}$
## References
1. [Wikipedia](https://en.wikipedia.org/wiki/Mutual_information)

## Code
1. 

#### Tags