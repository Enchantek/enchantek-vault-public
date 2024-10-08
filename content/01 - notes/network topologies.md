---
tags:
  - permanent
  - compsci/networks
  - publish
created: 2024-09-12T16:59
modified: 2024-10-08T16:10
---
Network topology refers to the physical or logical arrangement of devices on a computer network, defined by how nodes (devices) are connected and how data flows between them. How topologies are used significantly affects network performance, scalability, and reliability. Each different topology are suited for different network requirements and environments.

| Topology                    | Description                                                                                                                                                                                                                               |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[[bus-topology\|Bus]]**   | All devices connect to a single cable (the bus). Data transmitted by any device is received by all others. Simple and cost-effective for small networks, but vulnerable to cable failures and performance issues in larger networks.      |
| **[[ring topology\|Ring]]** | Devices form a closed loop, each connecting to two others. Data travels in one direction around the ring. Offers fair access to all nodes but can be disrupted by single device or cable failures. Used in some specialized applications. |
| **[[star topology\|Star]]** | All devices connect to a central node (hub or switch). Each device has a dedicated point-to-point link to the central node. Offers easy installation and troubleshooting, but vulnerable to central node failure.                         |
