Overfitting is a phenomenon that happens when our model has very good results on the train dataset but not on the test set. We can consider it as when we learn by heart, but we do not really generalize the concepts.
Possible causes:
- the dataset is too small, so it is not enough to learn the underlying patterns;
- data is unbalanced or not really representative of the distribution of the data;
- there is a lot of noisy data;
- we let the model train for too long;
- the model is too complex.

Overfitting can be detected by using k-fold cross validation. This method consists in dividing the dataset in K subsets (called folds) and then iterate the training as follows:
- one fold is use as validation set, the others are used for training;
- test model on the fold that was not used during training;
- continue until the model is tested on all the subsets.

How to avoid incurring into overfitting:
- Early stopping -> simply stop the training before the model learns "too well";
- Delete some features of the model;
- Regularization -> see [[Regularization]]
- Ensembling -> sometimes by combining weaker models we can improve the results;
- Just get more data