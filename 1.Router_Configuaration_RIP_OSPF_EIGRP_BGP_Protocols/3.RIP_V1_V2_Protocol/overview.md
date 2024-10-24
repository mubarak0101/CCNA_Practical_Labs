
# Routing Information Protocol (RIP)

## Overview

**Routing Information Protocol (RIP)** is one of the oldest distance-vector routing protocols. It is used in small to medium-sized networks to route data based on the number of hops between source and destination.

RIP has two main versions:
1. **RIP Version 1 (RIPv1)** – The original version, designed for classful IP networks.
2. **RIP Version 2 (RIPv2)** – An enhanced version that supports classless routing and subnet masks.

---

## Key Features of RIP

1. **Distance Vector Protocol**: RIP uses a distance vector algorithm to determine the best path based on hop count.
2. **Hop Count Limit**: RIP allows a maximum of 15 hops, meaning that networks beyond 15 hops are considered unreachable.
3. **Updates**: RIP routers send out updates every 30 seconds, broadcasting the entire routing table to neighbors.
4. **Split Horizon**: A mechanism to prevent routing loops by not advertising routes back in the direction from which they came.
5. **Hold Down Timers**: RIP uses timers to prevent flapping routes from being quickly accepted and dropped.
6. **Metric**: RIP uses the number of hops as its metric for determining the best path.

---

## Differences Between RIPv1 and RIPv2

| Feature           | RIPv1                       | RIPv2                             |
|-------------------|-----------------------------|------------------------------------|
| Routing Type      | Classful (No Subnet Mask)    | Classless (Supports Subnet Mask)   |
| Authentication    | No Authentication           | Supports Authentication (Plaintext or MD5) |
| Broadcast/Multicast | Broadcast (255.255.255.255) | Multicast (224.0.0.9)             |
| VLSM Support      | No                          | Yes                               |
| Next Hop Info     | No                          | Yes                               |

---

## RIPv1 Configuration Example

RIP Version 1 is a classful routing protocol, meaning it doesn't support subnet masks or VLSM.

### Router Configuration
```bash
Router(config)#router rip
Router(config-router)#network 192.168.1.0
Router(config-router)#network 192.168.2.0
Router(config-router)#exit
```

This basic configuration enables RIP routing on the networks `192.168.1.0` and `192.168.2.0`.

---

## RIPv2 Configuration Example

RIP Version 2 adds support for classless routing and subnet masks, making it more suitable for modern network environments.

### Router Configuration
```bash
Router(config)#router rip
Router(config-router)#version 2
Router(config-router)#network 192.168.1.0
Router(config-router)#network 192.168.2.0
Router(config-router)#exit
```

In this configuration:
- `version 2` enables RIP Version 2.
- The `network` command specifies which networks will participate in RIP.

---

## Common RIP Commands

### 1. Show RIP routes
```bash
Router#show ip route rip
```

### 2. Verify RIP version
```bash
Router#show ip protocols
```

### 3. Debugging RIP
```bash
Router#debug ip rip
```

