Created: 2023-02-13 11:34
#note

Still an evolving field -> lots of tools.

Recommendations:
- decouple tools as much as possible from the main pipelines;
- choose tools that suits the use case (classical, NLP, vision);
- test before you buy;
- if pipelines are third-party based, understand road map and support aspects;
- look for extensibility and programmability

Tools:
- for Data Engineering:
	- Apache Hadoop;
	- Spark;
	- Kafka;
	- RDBMS, NOSQL and distributed databases (MySQL, MongoDB, HDFS);
	- data versioning tools (DVC, lakeFS, Neptune);
- Experiment management:
	- [Weights and biases](https://wandb.ai/site);
	- Kubeflow;
	- MLflow;
- AutoML:
	- Kubeflow;
	- Databricks;
- Model registry and life cycle management:
	- MLflow, Neptune, Weights & Biases;
- Benchmarking:
	- MLPerf, DAWNBench, MLflow

#### Tags
#mlops #ml #technologies