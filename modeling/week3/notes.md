### Transformation

###3 Haddop Distributed File System
HDFS: combines computre and storage on the same nodes
NameNode, DataNodes: increases durability and availability of the data
MapReduce: send computation code to the nodes that contain the data

Shuffle: redistribute resuklts across the cluster

map -> shuffle -> reduce
produce a set of key-values pair      redistribute results across the clusters      aggregate data on each node


#### ShortComings- Hadoop

on disk: 

pro: simplifies state and workflow management
minimize memory consumption
cons:
drive high-disk bandwith utilization
increases processing time 

#### Spark

Uses in-memory processing.

Computing engin designed for processing large datasets.
Retains intermedidar resuls in memory
Limits disk I/O interactions enabling faster computation

Perform sql queries, apply streaming transformations
Spark Application: driver node (central node) 
worker nodes, cluster manager

#### SparkSession: single unified point to spark's application.


