Created: 2023-02-13 11:47
#note

Feature validation pipeline:
- basic feature validation (missing or erroneous data, data formats);
- data distribution validation (mean, quartiles etc);
- out of distribution validation (values beyond quartiles and new class values);
- correlation validation (feature vs target)

Managed feature stored:
- centralized store for features;
- preprocessed and ready for ML;
- shared across multiple teams;
- regularly updated with new features;
- registry for features

Best practices:
- shared ownership with defined responsibilities
- flexible schema for regular additions;
- loosely coupled datasets, yet linkable
- updated registry for available data
- flexibility for last mile post-processing
- multiple technologies as needed; low cost as possible

#### Tags
#mlops #feature #pipeline