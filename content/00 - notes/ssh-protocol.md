---
tags:
  - permanent
  - compsci/networks
  - "#publish"
created: 2024-09-24T16:50
modified: 2024-09-24T18:50
---
# SSH (Secure Shell) Protocol

SSH (Secure Shell) is a cryptographic network protocol used for secure communications over an unsecured network. In essence, SSH acts like a secure bridge between two points, allowing users to perform various tasks on remote systems as if they were sitting right in front of them, all while ensuring that the data exchanged remains private and intact. SSH is often used for controlling servers remotely, for managing infrastructure, and for transferring files.

## TCP/IP 

SSH operates as an application layer protocol within the TCP/IP suite, which is the foundation of Internet communications.

1. At the bottom, the Internet Protocol (IP) handles routing of packets between networks.
2. Above IP, the Transmission Control Protocol (TCP) ensures reliable, ordered delivery of data.
3. SSH runs on top of TCP, typically using port 22 by default.

> [!diagram]-
> ![[Pasted image 20240924174557.png]]

When you initiate an SSH connection, it establishes a TCP connection first. Once this connection is established, SSH uses it as a secure tunnel for its own protocol. SSH then handles encryption, authentication, and data integrity within this tunnel, adding a layer of security to the underlying TCP/IP communication. This layered approach allows SSH to provide secure remote access and file transfer capabilities while relying on the established infrastructure of TCP/IP for basic network communication.

## Public-Key Cryptography

SSH is secure because it incorporates encryption and authentication via a process called [[public-key-cryptography|public-key cryptography]]. Public key cryptography is a way to encrypt data, or sign data, with two different keys. Because the two keys correspond to each other, establishing the key owner's identity requires possession of the private key that corresponds with the public key.

In an SSH connection, both sides have a public/private key pair, and each side authenticates the other using these keys. This differentiates SSH from HTTPS, where most implementations only verifies the identity of the web server in a client-server connection.