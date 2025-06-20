### Storage Abstractiosn

Data warehouse, data lake, data lakehouse

Architectural ideas
- Data warehouse: subject-oriented,integrated,nonvolatile and time-variant colleciton of data in support of management's decisions

integrated: combines data from different sources into a consisten format.
nonvaolatie: dat is read-only and cannot be deleted or updated.

time-variant: stores current and historical data


etl: extract-transfrom-load

extraction -> staging area -> transformation-model data -> data warehouse

data marts: subset data-warehouse [simple denormalized schema]

### Table

| traditional data warehouse | cloud data warehouse| 	
| -------------------------- | ------------------- |
| Stored data is highly structured | Stored data is highly structured|
| Data modeled to enable analytical queries | Data modeled to enable analytical queries| 
| - | high processing from MPP |
| - | columnar storage |
| - | separation of storage and compute | 


### Data lake- key architectural ideas

Central repositoyr for storing large volumes of data
No fixed schema or predefined set of transformations
Schema on read pattern

reader determines the schema when reading the data.

storage = hadoop hdfs changing to s3.
processing tools =  spark,apache pig,hive, prest


data-swap: no data cataloing, no proper data manageement, no data discovery tools, no guarantee on the data integrity and quality, WERE PAINFUL to implement DMLno schema management and data modeling

### Data Zones: Used to organize dat in a data lake, where each zone
houses data that has been processed to varying degrees.

landing/raw -> storage{cleaned,transformed} -> enriched
