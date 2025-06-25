### Data queries-storage

- Magnetics Disks

 Hard Disk Drives: track + sector = address data


- Solid States Drives

Flash Memory: SSD read and write data much faster


#### Comparing


|  | Magnetic Disk | SSD | RAM | CPU CACHE |
|_ | ------------ | ---- | --- | --------- |
|Latency| 4 milliseoncs | 0.1 miliseconds| 0.1 microseconds | 1 nanoseconds |
| IOPS | hundres | tens of thousands| millions  | / |
| Data Transfer speed | Up to 300MB/s | 4 GB/s|100GB/s | /| 
| Cost | $ 0.03-0.06GB| 0.08 GB| $3/GB | / |

#### Distributed storage

Data transfer speed limited by network perfmance


#### Serialization Formats
csv,xml,json

binary=parquet.avro
paquer=column-base format
avro=row-based format

#### Compression

encode characters based on their frequency

compressed file identify redudancy , improve query perfomance reduces the i/o time needed to load data.

#### Cloud Storage System

Block: Perfomance and flexibility. Divides files into small, fixed-size blocks and store them on disk.
higher scalabaility
 [ideal for frequent access and modificaiton]
 [for virtual machines]
ec2 uses ebs
Object: Store immutable files as data objects in a flat structure

to update the file you have to re-write the entire object.
can scale horizontally


[storage layer of cloud data warehouses or data lakes]
[storing data needed in OLAP systems]
[machine learning pipelines]

[no good for transaction workloads]

File: organize files into a directory tree
ensure directory contains metadata to reflect owner and some attribues

efs-aws


#### TABLLE

| file storage | block storage | object storage|
| ------------ | ------------  | -------------|
| support data sharing, easy to manage with low perfomance and scalability requirements |  supports transactional workloads allows fequent read an write with low latency | supports analytical queries on massive datasets, offer high scalability and parrellal data processing |

#### Storage Tiers
|_ | Hot Storage | warm storage | cold storage | 
|_ |----------  | ------------ | ------------ |
|Access Frequency |very frequent | less frequent | infrequent |
| Example | product recommendation applicaiton | regular reports and analysses | archive |
| storage medium | ssd & memory |  magnetic disk or hybrid | low cost magneti disks |
| storage cost | high | medium | low |
| retrieval cost | low | medium | high |


####  How distributed storage systems work

Group of nodes = cluster

Each node has medium.

Horizontal scaling.

Higher fault tolerance and data durability
High availability

Long processing tasks.

Methods for distributing data

replication: for redundancy

partitioning:  also sharding, different partition to a different nodes.


CAP:
Consistency.
Availability.
Partition Tolerance:



#### Object Storage: flat structure immutability

Object key = /data/csv = /year=2025/


#### File Storage
A directory 

#### Block Storage: 
File is splitted 
#### Memory
Memcached
Redis

#### Rows vs column

Rows: 
1 millon rows x 30 colums x 100 bytes per entry = 3G
data transfers speed : 200MB/s
Total transfer time 3GB/200MB/s = 15

Columns:
just one column!

#### Vector Database

Consists of numerical values arranged in an array
ex: weather info, image data.
Vector Embeddings: capture semantic meaning of an item, like a text document
or image
[Original data] => [vector embedding]
=> [vector database]

Distance Metrics: uses a distance metric to find similar vectors
not euclidean, 
cosine distance,manhattan distance 
