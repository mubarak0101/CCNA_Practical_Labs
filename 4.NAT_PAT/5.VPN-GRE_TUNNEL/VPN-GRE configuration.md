
# VPN GRE Tunnel Network Topology

This project demonstrates a VPN setup using GRE (Generic Routing Encapsulation) Tunnels to securely connect two Cisco branches over the Internet. The setup also includes OSPF routing to dynamically manage the routing between branches. The purpose of this README is to provide a comprehensive guide on the topology, configuration, and verification steps.

## Network Topology Overview

- **Branches**: 
  - **Mumbai Branch (Cisco Branch 1)**: Connected to the router with IP `192.168.10.10`.
  - **Delhi Branch (Cisco Branch 2)**: Connected to the router with IP `192.168.30.10`.
- **GRE Tunnel**:
  - **Tunnel Source (Router0, Mumbai)**: `192.10.1.1`
  - **Tunnel Destination (Router2, Delhi)**: `192.10.3.2`
  - **Tunnel IP Addresses**:
    - **Mumbai Branch Tunnel**: `10.10.10.1/24`
    - **Delhi Branch Tunnel**: `10.10.10.2/24`

## IP Addressing and Routing

### Device IP Address Plan

| Device             | Interface   | IP Address        |
|--------------------|-------------|-------------------|
| Mumbai Router0     | G0/0        | 192.10.1.1        |
| Mumbai Router0     | Tunnel 10   | 10.10.10.1        |
| Delhi Router2      | G0/0        | 192.10.3.2        |
| Delhi Router2      | Tunnel 10   | 10.10.10.2        |
| Intermediate Router1 (ISP) | G0/0 | 192.10.2.1 |
| Intermediate Router1 (ISP) | G0/1 | 192.10.2.2 |
| Intermediate Router3 (ISP) | G0/0 | 192.10.3.1 |
| Intermediate Router3 (ISP) | G0/1 | 192.10.3.2 |

### Routing Protocol - OSPF

Both branches use OSPF (Open Shortest Path First) as the routing protocol within their respective networks to allow for scalable and dynamic routing.

#### OSPF Configuration - Mumbai Branch (Router0)

```shell
Router(config)# router ospf 10
Router(config-router)# network 192.168.10.0 0.0.0.255 area 0
Router(config-router)# network 192.10.1.0 0.0.0.255 area 0
Router(config-router)# network 10.10.10.0 0.0.0.255 area 0
```

#### OSPF Configuration - Delhi Branch (Router2)

```shell
Router(config)# router ospf 10
Router(config-router)# network 192.168.30.0 0.0.0.255 area 0
Router(config-router)# network 192.10.3.0 0.0.0.255 area 0
Router(config-router)# network 10.10.10.0 0.0.0.255 area 0
```

## GRE Tunnel Configuration Steps

### Step 1: GRE Tunnel Interface Configuration - Mumbai Router (Router0)

```shell
Router(config)# interface tunnel 10
Router(config-if)# ip address 10.10.10.1 255.255.255.0
Router(config-if)# tunnel source g0/0
Router(config-if)# tunnel destination 192.10.3.2
Router(config-if)# tunnel mode gre ip
Router(config-if)# no shutdown
```

### Step 2: GRE Tunnel Interface Configuration - Delhi Router (Router2)

```shell
Router(config)# interface tunnel 10
Router(config-if)# ip address 10.10.10.2 255.255.255.0
Router(config-if)# tunnel source g0/0
Router(config-if)# tunnel destination 192.10.1.1
Router(config-if)# tunnel mode gre ip
Router(config-if)# no shutdown
```

### Step 3: Static Routes Configuration for Internet Routers

- **ISP Router1** (connecting 192.10.1.1 and 192.10.3.2):

  ```shell
  Router(config)# ip route 192.10.3.0 255.255.255.0 192.10.2.2
  ```

- **ISP Router3** (connecting 192.10.1.1 and 192.10.3.2):

  ```shell
  Router(config)# ip route 192.10.1.0 255.255.255.0 192.10.2.1
  ```

## Verification Steps

To ensure proper connectivity and configuration, verify the following:

### 1. Verify OSPF Adjacency

Use the following command on each branch router to confirm that OSPF adjacency is established:

```shell
Router# show ip ospf neighbor
```

### 2. Verify GRE Tunnel Interface Status

Check the tunnel interface status with the following command to confirm the tunnel is up and running:

```shell
Router# show ip interface brief
```

The tunnel interface should show "up/up."

### 3. Verify Tunnel Connectivity

From a device in the **Mumbai Branch**, ping the tunnel IP address of **Delhi Branch** (`10.10.10.2`):

```shell
Router0# ping 10.10.10.2
```

### 4. Check OSPF Routes in the Routing Table

View the routing table to verify OSPF-learned routes for remote branch networks:

```shell
Router# show ip route ospf
```

This should show routes for the other branch’s network, indicating successful OSPF routing through the GRE tunnel.


## Key Points

- **GRE Tunneling**: GRE encapsulates packets, creating a private, secure link over a public network.
- **OSPF Routing**: OSPF ensures dynamic routing, allowing the branches to communicate effectively.
- **Tunnel Security**: Although GRE itself doesn’t encrypt data, the private addressing enhances basic security.
  
## Lincence and bug reporting
Enjoy and report bugs to https://github.com/mubarak0101/CCNA_Practical_Labs/issues

This is a free project to be used as you like at your own risk as long as you abide by CC0-1.0. https://choosealicense.com/licenses/cc0-1.0/

