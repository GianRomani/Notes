# Metrics
Created: 2022-03-23 12:22
#survey

Use validation techniques (k-fold cross validation or leave one out cross validation in case of [[Cold-start]])

There are several aspects to consider:
- [[Accuracy]];
- [[Similarity]];
- [[Ranking recommendation metrics]];
- [[Set recommendation metrics]];
- [[Diversity metrics]];
- [[Stability and reliability]];

This [survey](https://link.springer.com/content/pdf/10.1007/s13042-017-0762-9.pdf) on evaluation methods for RS define 6 concepts for assessment of RSs:
- [[Utility]];
- [[Novelty]];
- [[Diversity for RS]];
- [[Unexpectedness]];
- [[Serendipity]];
- [[Coverage]].

### Metrics classification
Metrics can be classified in two ways:
1. User-dependent: they require user information -> they generally compare items recommended and history of the user -> utility, life and system level novelty, unexpectedness and serendipity use this kind of metrics;
2. User-independent concepts: they do not require user information, but they use other areas (recommendation list, info about the items etc) -> diversity, recommedation liste level of novelty and coverage fall in this group.

### Relationships among the concepts
Some of the metrics can be seen as base concepts, i.e. they do not depend on other concepts. Serendipity is a compund concept, i.e. its definition consists on three compounds: utility, novelty and unexpectedness. Diversity and coverage are isolated from the others.
![[relationship_among_metrics.png]]


## References
1. [Survey](https://link.springer.com/content/pdf/10.1007/s13042-017-0762-9.pdf)
2. https://www.sciencedirect.com/science/article/pii/S0950705113001044#b0940
3. https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9354169&tag=1


#### Tags
#evaluation_metrics
