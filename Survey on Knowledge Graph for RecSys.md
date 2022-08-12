# Survey on Knowledge Graph for RecSys
Created: 2022-08-12 15:49
#note

A knowledge graph is a heterogeneous graph where nodes represent entities and edges represent relations between entities -> we can map items and their attributes to understand the mutual relations between items.
This can help in case of data sparsity ([[Cold-start]]) or performance problems. Another quality of KG-based recommendation is the interpretability.
They are often use to provide side information to recommender systems

KGs can be applied in three ways: the embedding-based method, the path-based method and the unified method.

# Knowledge Graphs
A common way to represent KGs is the RDF standard, where each edge is represented in the form of a triple (head entity, relation, tail entity).

**Notation:** 
- Heterogeneous Information Network (HIN) -> a HIN is a directed graph G= (V,E) with an entity type mapping function $\phi:V \rightarrow A$ and a link type mapping function $\psi : E \rightarrow R$. Each entity $v \in V$ belongs to an entity type $\phi(v) \in A$ and each link $e \in E$ belongs to a relation type $\psi(e) \in R$. In addition, the number of entity types |A|>1 and/or the number of relation types |R|>1.
- 
## References
1. [Survey](https://arxiv.org/pdf/2003.00911.pdf)

## Code
1. 

#### Tags