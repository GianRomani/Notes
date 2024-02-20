Created: 2024-02-20 13:49
#quicknote

After we decided the [[Model Deployment]], we have to consider how we will release new versions of the model or in general of the service.
## Recreate strategy

- existing versions in production are stopped and uninstalled
- new versions are installed and tested, and then production resumes
- simple and easy to implement, **but** service downtime expected
- it could be used for batch applications where clients can be stopped from accessing the services for some time

## Rolling deployments

- used when we have n+1 deployments -> service is running on multiple nodes
- updates is don eon one node at the time -> service is always available

## Shadow deployments

- new instance/cluster with new version
- production traffic is duplicated and moved to the shadow deployment
- shadow is validated for stability and performance
- if validation is successful, we can move the service

## Canary deployments

- a separate cluster set up with the new version (canary)
- part of the traffic is moved to the canary
- canary is validated
- roll back if there are issues
- on successful validation, new version is deployed cross the board

## Blue/Green deployments

- new cluster with its own resources (nodes) set up for the new version
- the gateway/load balancer is switched from the existing to the new version
- if issues found, gateway can be switched back, otherwise, older version can be retired
- it is easy to move between versions, but additional resources are needed for the new cluster
#### Tags
#mlops #ml #linkedin