# Amazon DSSTNE
Created: 2022-12-23 14:22
#note

DSSTNE (pronounced "Destiny") is an open source software library for training and deploying recommendation models with sparse inputs, fully connected hidden layers, and sparse outputs. Models with weight matrices that are too large for a single GPU can still be trained on a single host. DSSTNE has been used at Amazon to generate personalized product recommendations for our customers at Amazon's scale. It is designed for production deployment of real-world applications which need to emphasize speed and scale over experimental flexibility.

DSSTNE was built with a number of features for production recommendation workloads:
-   **Multi-GPU Scale**: Training and prediction both scale out to use multiple GPUs, spreading out computation and storage in a model-parallel fashion for each layer.
-   **Large Layers**: Model-parallel scaling enables larger networks than are possible with a single GPU.
-   **Sparse Data**: DSSTNE is optimized for fast performance on sparse datasets, common in recommendation problems. Custom GPU kernels perform sparse computation on the GPU, without filling in lots of zeroes.

It can be used in addiction of [[Apache Spark]].

## References
1. [LinkedIn course on RecSys](https://www.linkedin.com/learning/building-recommender-systems-with-machine-learning-and-ai/amazon-dsstne?autoSkip=true&autoplay=true&resume=false)

## Code
1. [GitHub](https://github.com/amazon-archives/amazon-dsstne)

#### Tags
#ml #scaling #recsys