Created: 2023-02-23 12:01
#quicknote


Definition of **Architecture**: the way software components are arranged and the interactions between them.

There are several elements to consider, as shown in the next image:
![[infrastructure_service_ml_models.png]]

The minimal capacity needed to offer the service is fundamental. For this, remember to consider:
- system and service load estimates (average versus peak loads);
- requirements for a rollout strategy;
- autoscaling for optimal use of the system;
- overload mitigation strategies

Obviously, the cost planning is also important -> ML services can overrun costs if not properly planned and monitored.

#### Tags
#ml #course
