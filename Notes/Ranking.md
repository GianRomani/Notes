# Ranking
Created: 2022-06-16 18:23
#note

When ranking documents (or, more in general, items), depending on how many of them we consider at a time in the loss, we can define several approaches:
- Pointwise approach -> one document at a time is considered. The single document is taken and its relevancy for the actual query is computed. This means that the score for each document is independent of the other documents. The final result is given by the sorting og the scores;
- Pairwise approach -> a pair of documents at a time is considered. The goal is to find the optimal ordering for such pair and compare it to the ground truth, i.e. minimizing the number of inversions in ranking. This approach is usually better than pointwise ranking. Some pairwise approaches are: RankNet, LambdaRank ad LambdaMART (comparison [here](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/MSR-TR-2010-82.pdf), simple explanation [here](https://www.quora.com/What-is-the-intuitive-explanation-of-Learning-to-Rank-and-algorithms-like-RankNet-LambdaRank-and-LambdaMART-In-what-types-of-data-variables-can-these-techniques-be-used-What-are-their-strengths-and-limitations/answer/Nikhil-Dandekar));
- Listwise approach -> in this approach we directly loook at the entire list of documents. There are two main sub-techniques:
	- Direct optimization of IR measures as NDCG -> [SoftRank](https://www.microsoft.com/en-us/research/publication/softrank-optimising-non-smooth-rank-metrics/), AdaRank;
	- Minimize a loss function that is defined based on understanding the unique properties of the kind of ranking you are trying to achieve -> ListNet, [ListMLE](http://auai.org/uai2014/proceedings/individuals/164.pdf).


## References
1. [Medium](https://medium.com/@nikhilbd/pointwise-vs-pairwise-vs-listwise-learning-to-rank-80a8fe8fadfd)
2. [Paper on learning to rank](https://www.microsoft.com/en-us/research/publication/learning-to-rank-from-pairwise-approach-to-listwise-approach/)

## Code
1. 

#### Tags
#ranking