Created: 2024-02-20 14:17
#quicknote

Without resiliency, ML solutions would suffer from inconsistency, customer concerns, and loss of value.

Model resiliency:
- validate inputs during inference
- track resources utilization to identify choke points
- monitor operational metrics to identify degradation
- measure model drift and look for decay
- analyze model performance for bias

Service resiliency:
- add redundant nodes for tasks and services
- implement autoscaling to handle sudden changes in load
- throttle incoming requests to alleviate sudden bursts
- deploy in additional locations for geo-resiliency
- use redundant storage schemes to handle disk outages

Solution resiliency:
- impact on user experience in case of outages should be assessed, monitored, and alleviated
- create multi-region deployments of the solution
- load balance user requests across regions in case of service issues
- use circuit breakers in clients to overcome broken connections
- provide default/alternate functionality to users

#### Tags
#mlops #ml