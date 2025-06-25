# Kubernetes Job Workload Explained

This document uses Mermaid diagrams to explain how a Kubernetes Job works.

## Basic Job Structure

```mermaid
graph TD
    A[Job Resource] --> B[Pod Template]
    B --> C[Pod 1]
    B --> D[Pod 2]
    B --> E[Pod 3]
    C --> F[Container]
    D --> G[Container]
    E --> H[Container]
    
    classDef jobResource fill:#f9f,stroke:#333,stroke-width:2px
    classDef podTemplate fill:#bbf,stroke:#333,stroke-width:1px
    classDef pod fill:#dfd,stroke:#333,stroke-width:1px
    classDef container fill:#ffd,stroke:#333,stroke-width:1px
    
    class A jobResource
    class B podTemplate
    class C,D,E pod
    class F,G,H container
```

## Job Lifecycle

```mermaid
stateDiagram-v2
    [*] --> Created
    Created --> Active: Pods created
    Active --> Succeeded: All pods completed successfully
    Active --> Failed: One or more pods failed
    Active --> Active: Pod failure (with restart policy)
    Succeeded --> [*]
    Failed --> [*]
```

## Job Control Flow

```mermaid
sequenceDiagram
    participant User
    participant API as Kubernetes API
    participant JobController as Job Controller
    participant PodController as Pod Controller
    participant Node

    User->>API: Create Job (kubectl apply)
    API->>JobController: Job Created Event
    JobController->>API: Create Pod(s)
    API->>PodController: Pod Created Event
    PodController->>Node: Schedule Pod
    Node->>PodController: Pod Status Updates
    PodController->>API: Update Pod Status
    API->>JobController: Pod Status Change Events
    JobController->>API: Update Job Status
    API->>User: Job Status (kubectl get jobs)
```

## Job Parallelism and Completions

Kubernetes Jobs allow you to control how many pods run in parallel and how many successful completions are required before the job is considered complete. These are managed by two key fields:

- **parallelism**: The maximum number of pods that can run at the same time. This allows you to process multiple tasks concurrently, improving throughput for batch workloads.
- **completions**: The total number of successful pod completions required for the job to finish. Each time a pod completes successfully, the job controller counts it toward this total.

### How It Works

- If `parallelism` is less than `completions`, Kubernetes will create new pods as others complete, ensuring that no more than `parallelism` pods are running at once, until the total number of successful completions reaches the `completions` value.
- If `parallelism` is equal to or greater than `completions`, all pods may be created and run at the same time.
- If a pod fails and the job's `backoffLimit` is not reached, Kubernetes will create a replacement pod to try again, until the required number of completions is achieved or the job fails.

### Example

Suppose you have a job with `parallelism: 3` and `completions: 5`:
- At most 3 pods will run at the same time.
- As soon as a pod completes, a new one is started (if needed) until 5 pods have completed successfully.

```mermaid
graph TD
    Job["Job\nparallelism: 3\ncompletions: 5"] --> Pod1["Pod 1 (Running)"]
    Job --> Pod2["Pod 2 (Completed)"]
    Job --> Pod3["Pod 3 (Running)"]
    Job -.-> Pod4["Pod 4 (Not Started)"]
    Job -.-> Pod5["Pod 5 (Not Started)"]
    
    classDef running fill:#9f9,stroke:#333
    classDef completed fill:#99f,stroke:#333
    classDef notStarted fill:#fff,stroke:#333,stroke-dasharray: 5 5
    
    class Pod1 running
    class Pod2 completed
    class Pod3 running
    class Pod4,Pod5 notStarted
```

This setup is useful for parallelizing batch jobs, such as processing files, running tests, or performing data transformations, where you want to control both concurrency and total work done.

## Key Components Explained

- **Job Resource**: The Kubernetes object that manages the batch workload
- **Pod Template**: Specification for pods created by the job
- **Parallelism**: Maximum number of pods that can run in parallel
- **Completions**: Total number of successful pod completions required
- **BackoffLimit**: Number of retries allowed before the job is marked as failed
- **ActiveDeadlineSeconds**: Time limit for the job execution

## Common Use Cases

1. **Batch Processing**: Running finite data processing tasks
2. **Migration Scripts**: Database migrations or data transformations
3. **CI/CD Tasks**: Build, test, and deployment operations
4. **Initialization Tasks**: One-time setup operations

## Job vs CronJob

```mermaid
graph LR
    CronJob["CronJob\n(scheduled job)"] --> |"creates on schedule"| Job
    Job --> |"creates"| Pods
    
    classDef cronjob fill:#fcf,stroke:#333
    classDef job fill:#cff,stroke:#333
    classDef pod fill:#dfd,stroke:#333
    
    class CronJob cronjob
    class Job job
    class Pods pod
```
