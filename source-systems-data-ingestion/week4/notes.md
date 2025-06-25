#### The three pillars of dataops

Aumtoation, Observability & Monitoring & Incident Response


### Orchestration

When to use cron
- To schedule simple and repetitive taks

- In the prototyping phase


### Advantages

- Written in python
- Open source is very active
- Is available as managed service  


### Challenges

- Scalability challenge
- Ensure integrity

### Basics


### AirFlow



### TaskFlowAPi

Use decorators 

```python
@dag(
description = "ETL Pipeline",
tags = ["data_engineer_team"],
schedule = "@daily"
start_date = datetime(2024,12,1),
catchup = False)

def my_first_dag():
	@task
	def extract_data():
		print("Done with the extractiont task")
	@task
	def transform_data():
		print("Done with transformation task")
	@task
	def load_data():
		print("done with loading task")
	extract_data() >> transform_data() >> load_data()

my_first_dag()



``` 
