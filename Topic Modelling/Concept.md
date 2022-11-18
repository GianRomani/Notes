# Concept
Created: 2022-07-01 08:50
#note
![[Concept_model.png]]

Steps:
1. Both images an documents are both embedded into the same vector space using OpenAI's CLIP model;
2. Using [[UMAP]]+[[HDBSCAN]] the image embeddings are clustered to create clusters of visually and semantically similar images. Clusters are called concepts;
3. To pick representative images of clusters (exemplars), the most related images to each concept are taken. [[Maximal Marginal Relevance]] is used for this taask. The selected images are then combined into a single image to create a single visual representation;
4. Textual embeddings are compared with the created concept cluster embeddings. Cosine similarity or c-TF-IDF can be used to select the embeddings that are most related to one another.


## References
1. [Documentation](https://maartengr.github.io/Concept/algorithm/algorithm.html)
2. [CLIP](https://www.kdnuggets.com/2021/03/beginners-guide-clip-model.html)

## Code
1. [GitHub](https://github.com/MaartenGr/Concept)

#### Tags