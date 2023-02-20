Created: 2022-04-21 16:28
#note

I'll try to use this clustering method with [[UMAP]] for dimensionality reduction.

It is a density-based clustering approach, so it is applied in three steps:
1. Estimate of the densities;
2. Pick regions of high density;
3. Combine points in these selected regions

## Estimating densities

It is simply based on the concept of **core distance**, which is just the distance of a point to its K-th nearest neighbor. Points that are in dense regions have smaller core distances -> density is given by the inverse of core distances.
[[core_distance.png]]

## Cluster selection

In DBSCAN, we use a global threshold and group points with a higher density together -> ok, but we could have clusters with varying densities as in [[HDBSCAN_varying_density.png]] -> on the left of the image, are there a mountain with two peaks or two different mountains? To solve this mistery, plot the cluster hierarchy and compute the volume of the peaks and their base, if the sum of the peaks' volume is bigger than the one of the volume, then the two peaks are actually two montains. Example: [[peaks_or_mountain.jpeg]]

## References
1. [HDBSCAN](https://towardsdatascience.com/a-gentle-introduction-to-hdbscan-and-density-based-clustering-5fd79329c1e8)
2. [UMAP + HDBSCAN](https://towardsdatascience.com/clustering-sentence-embeddings-to-identify-intents-in-short-text-48d22d3bf02e)

## Code
1. 

#### Tags