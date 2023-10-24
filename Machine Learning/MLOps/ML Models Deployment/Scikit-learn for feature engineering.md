Created: 2023-03-02 15:34
#quicknote

It offers a wide range of ML algorithms and data transformations. Most of them follows the same functionality -> it is easy to implement new algorithms.

There are three classes of algorithms:
- Estimators;
- Transformers;
- Pipeline

### Estimators 
A class with fit() and predict() methods. It fits and predicts. Examples: Lasso, Decision trees, SVMs etc.
```python
class Estimator(object):

	def fit(self, X, y=None):
		"""
		Fits the estimator to data.
		"""
		return self
	
	def predict(self, X):
	"""
	Compute the predictions
	"""
	return predictions
```

### Transformers
A class that has fit() and transform() methods. It transform data. Examples: scalers, feature selectors, transformers etc.
```python
class Transformer(object):

	def fit(self, X, y=None):
		"""
		Learn the parameters to engineer the features.
		"""
	
	def transform(self, X):
	"""
	Transform the input data
	"""
	return X_transformed
```

It can handle:
- Missing data imputation;
- Categorical variable encoding;
- Scaling;
- Discretization;
- Variable Transformtion;
- Combining feature;
- Extract features from text.

### Pipeline
Class that allows to run transformers and estimators in sequence. Most steps are Transformers and then the last step is an Estimator.
```python
class Pipeline(Transformer):
	
	@property
	def name_steps(self):
		"""
		Sequence of transformers
		"""
		return self.steps
	@property
	def _final_estimator(self):
	"""
	Estimator
	"""
	return self.steps[-1]
```

Example:
![[sklearn_pipeline.png]]


#### Tags
#mlops #course #featureengineering