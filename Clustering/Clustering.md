# Clustering
Created: 2022-03-23 11:51

Used to improve predictions and reduce [[Cold-start]]  problem in [[Hybrid Filtering]]. Clustering is used in [[Social information]] to improve #tagging, explicit #social_link and explicit #trust_information.

### College Library Personalized Recommendation System

In this [Paper](https://www.sciencedirect.com/science/article/pii/S2212827119307401) an hybrid algorithm ([[Collaborative filtering]] + [[Content-based filtering]]) to recommend books is proposed.
Steps:
- Collaborative filtering: given the matrix R=UxI where U is the set of users and I is the set of categories, $R_{i,j}$ is the number of books borrowed by user *i* in category *j*. The similarity can be computed using Person correlation or cosine similarity. From the set of *k* most similar users we get the books (after deleting the books the target has already read). Since the matrix is very sparse (99.9% is empty) use k-means before calculating similarity; 
- Content-based: build books' features and users' profiles -> for each user create a list of borrowed books and importance feature (?)
- Hybrid approach -> obtain lists of recommendations from the previous apporaches and mix them -> how? It is not explained

### Improve Diversity

Greedy algorithm: https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.8.5232&rep=rep1&type=pdf

[ClusDiv](https://akademik.bahcesehir.edu.tr/~tevfik/papers/diversity.pdf) algorithm

### Improve reliability

### User interest change over time

### Data sparsity
To asses similarity between users in case of a sparse matrix, use clustering, dimensionality reduction or advanced similarity measures
[Bi-clustering](https://link.springer.com/article/10.1007/s00521-018-3959-2)

### Consistency

## References
1. https://www.sciencedirect.com/science/article/pii/S0950705113001044
2. [Survey](https://arxiv.org/ftp/arxiv/papers/2109/2109.12839.pdf)

#### Tags
#clustering