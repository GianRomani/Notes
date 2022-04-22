# UMAP
Created: 2022-04-21 16:33
#note

UMAP (Uniform Manifold Approximation and Projection for Dimension Reduction) is much faster and more scalable than t-SNE, while also preserving the global structure of the data much better. This makes it useful for both visualization and as a preprocessing dimensionality reduction step to use before clustering.
It is based on three assumptions:
1.  The data is uniformly distributed on Riemannian manifold;
2.  The Riemannian metric is locally constant (or can be approximated as such);
3.  The manifold is locally connected.

From these assumptions it is possible to model the manifold with a fuzzy topological structure. The embedding is found by searching for a low dimensional projection of the data that has the closest possible equivalent fuzzy topological structure.

It is considered to be better than tSNE because it can scale much better for increasing sample size, it is faster and it preserves global data structure (and other reasons as explained [here](https://towardsdatascience.com/how-exactly-umap-works-13e3040e1668)).

There are points of concern about using UMAP with density-based clustering methods as [[HDBSCAN]] because UMAP, like t-SNE, does not completely preserve density. That means that we can't be sure that the clusters we obtain are "real" and not just artifats of t-SNE. A discussion on t-SNE's shortcomings this is available [here](https://stats.stackexchange.com/questions/263539/clustering-on-the-output-of-t-sne). Anyway UMAP is much better than t-SNE to preserve the data's structure and can be used as preprocessing step for clustering as shown [here](https://umap-learn.readthedocs.io/en/latest/clustering.html).

## References
1. [Paper](https://arxiv.org/pdf/1802.03426.pdf)
2. [Rienammanian geometry](https://en.wikipedia.org/wiki/Riemannian_geometry)
3. [Riemannian manifold](https://en.wikipedia.org/wiki/Riemannian_manifold)
4. [How it works](https://umap-learn.readthedocs.io/en/latest/how_umap_works.html)
5. [Math](https://towardsdatascience.com/how-exactly-umap-works-13e3040e1668)

## Code
1. 

#### Tags