Created: 2023-03-02 11:46
#quicknote

Various problems:
- missing data;
- labels -> transform in right format (e.g. from straings to categorical) and deal with high number of labels or rare categories;
- distribution -> better spread of values may benefit performance;
- outliers;
- magnitude -> feature scale can affect some types of models

By selecting the features, we can obtain:
- simpler models;
- overfitting less probable;
- easier to implement things for software development:
	- smaller json messages sent over to the model;
	- less lines of code for error handling;
	- less information to log;
	- less feature engineering code
- variable are less redundant

Methods for feature selection:
- **filter methods:**
	- pros: 
		- quick feature removal;
		- model agnostic;
		- fast computation
	- cons:
		- does not capture redundancy;
		- does not capture feature interaction;
		- poor model performance;
- **wrapper methods**:
	- pros:
		- considers feature interaction;
		- best performance;
		- best feature subset for a given algorithm;
	- cons:
		- not model agnostic;
		- computation expensive
		- often impractible
- **embedded methods**:
	- pros:
		- good model performance;
		- capture feature interaction;
		- better than filter;
		- faster than wrapper;
	- cons:
		- not model agnostic

**Tools:**
- scikit-learn;
- Category encoders;
- Featuretools;
- Imbalance learn;
- Feature-engine;
- MLxtend


Add feature selection in the pipeline, if we re-train our model frequently has several pros/cons:
- Pros:
	- we can quickly retrain a model on the same input data;
	- no need to hard-code the new set of predictive features after each re-train;
- Cons:
	- lack of data versatility;
	- no additional data can be de through the pipeline;

This means that feature selection is suitable if the model is built and trained on same (and small) dataset.

## Resources
1. [Feature engineering](https://trainindata.medium.com/feature-engineering-for-machine-learning-a-comprehensive-overview-a7ad04c896f8)
2. [Feature Engineering 2](https://towardsdatascience.com/practical-code-implementations-of-feature-engineering-for-machine-learning-with-python-f13b953d4bcd)
3. [Feature Selection](https://trainindata.medium.com/feature-selection-for-machine-learning-a-comprehensive-overview-bd571db5dd2d)

#### Tags
#mlops #course #deployment