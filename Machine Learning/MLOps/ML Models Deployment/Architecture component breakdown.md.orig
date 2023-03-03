Created: 2023-03-02 11:10
#quicknote

High level architecture:
1. Evaluation layer: it checks the equivalence of two models and it can be used to monitor production models;
2. Scoring layer: it transforms features into predictions (scikit learn is industry standard);
3. Feature layer: it is responsible for generating feature data in a transparent, reusable, and scalable manner;
4. Data layer: it provides access to all of our data sources which simplifies the challenge of data reproducibility.

Offline training phase (from the bottom):
- training data -> functions or application that load and/or transform data;
- feature extraction -> scripts that generates features;
- model builder -> it transforms model in a form that can be deployed;
- output: trained model

Prediction phase:
- feature extractor as similar as possible to the one used in the offline phase;
- trained model obtained from the offline phase

## Resources
1. [FBLearner Flow](https://engineering.fb.com/2016/05/09/core-data/introducing-fblearner-flow-facebook-s-ai-backbone/)
2. [Scaling ML as a Service: Uber](http://proceedings.mlr.press/v67/li17a/li17a.pdf)
3. [System architectures for personalization and recommendation: Netflix](https://netflixtechblog.com/system-architectures-for-personalization-and-recommendation-e081aa94b5d8)
4. [TFX: Google](https://research.google/pubs/pub46484/)

#### Tags
#mlops #deployment #course