# Apache Spark
Created: 2022-12-23 14:02
#note

Framework designed for distributed computing.

Very efficient to distribute computation and scale things up, thanks to a cluster manager that allocates the things to do among executors. 

Processing is organized using a directed acyclic graph.

The main parts of Spark are:
- driver -> it is the program and a session for Spark;
- Executors -> nodes that receive the work to do from the driver;
- Cluster manager -> it communicates with both driver and executors to manage allocation of resources, the division of the jobs and the execution of the program.

**Software perspective:** all the components are managed by the Spark Core and on top of it there are libraries for additional features.

**RDD:** is an object that encapsulates the data we want to work on. It hides all the complex architecture and work done under the hood.
There are evolutions of RDD as DataFrame (row objects) or DataSet (similar to DataFrame but it adds type safety).


## References
1. [LinkedIn course on RecSys](https://www.linkedin.com/learning/building-recommender-systems-with-machine-learning-and-ai/introduction-and-installation-of-apache-spark?autoSkip=true&autoplay=true&resume=false)

## Code
1. 

#### Tags
#ml #scaling