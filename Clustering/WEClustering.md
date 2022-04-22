Created: 2022-04-21 18:33
#paper
## Main idea
Clutering technique based on word embeddings obtained from [[Transformer]]models (in particular BERT). It is supposed to deal with problems as synonymy, polysemy, high dimensionality and sparseness of data.
## In deep

WEClustering combines the advantages of contextual word embeddings derived from BERT with the statistical importance of each word, given by TF-IDF. 

We can identify 5 phases:
1. Preprocessing: documents are prepared for BERT. Documents are splitted based on sentences and converted to lower case for simplicity.
2. Embeddings extraction and filtration: fed the data to BERT and delete embeddings that are not semantically important (digits, stopwords etc) -> why not remove them before?;
3. Clustering of word embeddings: all the words vectors obtained from phase 2 are arranged as a matrix. Minibatch K-means clustering is used on this matrix to get clusters (called concepts) which represent unique themes contained in some document. These concepts are used as new features -> dimensionality is reduced from number of encodins to the number of clusters;
4. Generation of concept-document matrix CD: at this point each document is represented in terms of all the concepts. The document corpus is then represented in matricial form (Concept-Document matrix, CD). Each concept's score depends on the degree of relation between it and the document -> given a document $d_i$ and the concept $c_j$, $CD_{i,j} = \sum_{k}TFIDF(w_{j,k})$ where $TFIDF(w_{j,k})=freq(w_{j,k})*(\log(\dfrac{|D|+1}{doc\_count(w_{j,k})+1})+1)$ with $|D|$ is the total number of documents, $freq(w_{j,k})$ is the frequency of word $w_{j,k}$ in document $d_i$ and $doc\_count(w_{j,k})$ is the total number of documents that contain the word $w_{j,k}$;
5. Clustering the data matrix CD: apply a clustering technique (hierarchical agglomerative clustering is suggested) to the CD matrix

## Results

As shown in the paper, results are much better (up to 90%) compared to other classical clustering approaches in several aspects (Silhouette coefficient, adjusted rand index, purity and time needed) and on several datasets.

## Ideas

- Consider [[UMAP]] for further dimensionality reduction;
- Use all the documents together or divide them by category ("viaggio", "food" etc)?

## References
1. [Paper](https://link.springer.com/content/pdf/10.1007/s40747-021-00512-9.pdf)

## Code
1. 
