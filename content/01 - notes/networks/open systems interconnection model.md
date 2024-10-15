---
tags:
  - permanent
  - publish
  - compsci
  - networks
created: 2024-09-17T16:27
modified: 2024-10-08T17:00
cssclasses:
  - center-tables
---
The OSI model is a conceptual framework used to describe how data communications occur between devices in a network. It divides network communication into seven abstraction layers, each with specific functions and interfaces with the layers above/below it.

| Layer | Name                                         | Description                                                                         |
| ----- | -------------------------------------------- | ----------------------------------------------------------------------------------- |
| 7     | **[[osi application layer\|Application]]**   | To allow access to network resources                                                |
| 6     | **[[osi-presentation-layer\|Presentation]]** | To translate, encrypt, and compress data                                            |
| 5     | **[[osi-session-layer\|Session]]**           | To establish, manage, and terminate sessions                                        |
| 4     | **[[osi-transport-layer\|Transport]]**       | To provide reliable process-to-process message delivery and error recovery          |
| 3     | **Network**                                  | To move packets from source to destination; to provide internetworking              |
| 2     | **Data Link**                                | To organize bits into frames; to provide hop-to-hop delivery                        |
| 1     | **Physical**                                 | To transmit bits over a medium; to provide mechanical and electrical specifications |

It is used as a guide of sorts for developing products and programs, the model will help understand which protocols and devices will be compatible with one another.

## Application Layer

