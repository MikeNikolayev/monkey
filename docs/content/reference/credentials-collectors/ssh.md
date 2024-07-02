---
title: "SSH"
tags: ["credentials collector", "ssh", "linux"]
pre: '<i class="fas fa-terminal"></i> '
---

## Description

The SSH Credentials Collector steals SSH keys from Linux users.

For all users on the system, it locates the `/home/<user>/.ssh`
directory and steals keypairs from it. The supported private key
encryption formats are RSA, DSA, EC, and ECDSA.