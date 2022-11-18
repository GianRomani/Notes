# College Library Personalized Recommendation System
Created: 2022-06-03 13:14
#paper

## Main idea

In this paper an hybrid algorithm ([[Collaborative filtering]] + [[Content-based filtering]]) to recommend books is proposed.

## In deep

Steps:
- Collaborative filtering: given the matrix R=UxI where U is the set of users and I is the set of categories, $R_{i,j}$ is the number of books borrowed by user *i* in category *j*. The similarity can be computed using Person correlation or cosine similarity. From the set of *k* most similar users we get the books (after deleting the books the target has already read). Since the matrix is very sparse (99.9% is empty) use k-means before calculating similarity; 
- Content-based: build books' features and users' profiles -> for each user create a list of borrowed books and importance feature (?)
- Hybrid approach -> obtain lists of recommendations from the previous apporaches and mix them -> how? It is not explained

## References
1. [Paper](https://www.sciencedirect.com/science/article/pii/S2212827119307401) 

## Code
1. 
