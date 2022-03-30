# Text-based collaborative filtering for cold-start soothing and recommendation enrichment
Created: 2022-03-29 11:43

The main idea behind this paper is to build a unified vector space where both users and items are mapped. In this way similar items and users are mapped close together (if they use similar words), so that a classical neighborhood-based [[Collaborative filtering]] scheme can be used to recommend items. The model is called Conceptual Skip-Gram (CSG).
![[CSG.png]]

Objectives:
- words co-occurring in the reviews should be close to each other;
- concepts (users and items) should be close to their words;

In a [[Cold-start]] setting, any textual content can be used to create a profile by simply optimizing the objective functions for each wird from the data.

A review (in our case a #post) can be extracted as the sum of the representation of its words.

Another feature of this system is the ability to justify each recommendation by extracting the nearest words of an item.
## References
1. [Paper](https://www.archives-ouvertes.fr/hal-01640268/document)
2. [Word2Vec](https://arxiv.org/pdf/1301.3781.pdf)

## Code
1. 

#### Tags
#word2vec #csg #embedding #cold_start 