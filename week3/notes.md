### Data architecture

Enterprise Architecture: the design of system to suport change in an
enterprise, achieved by flexible and reversible decisions reached through
a careful evaluation of trade-off

### Principles of Good Architecture

- Choose common component wisely
- Plan for failure
- Architect for scalability
- Architecture is leadsership
- Always be architecting
- Build loosely coupled systems
- Make reversible decicions
- Prioritixze security
- Embrace FinOps


### Batch Architectures
Ingest, transform, storage
Data collected over a fixed period of time.

### Architecting for Compliance
GDPR (general  data protectcion regulation)
pii(personal identifiable information)
right to have your data erased



### Provider

Resource and Data Sources: read from external resource

```

data "aws_subnet" "selected_subnet" {
  id= "subnet-04542323"
}
```

resource "aws_instance" "webserver"{
subnet_id = data.aws_subnet.selected_subnet.id
instance_type= "t2.micro"
}

