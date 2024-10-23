# Parallel 3 Router Static Configuration Topology

This project demonstrates the implementation of a three-router static routing network in Cisco Packet Tracer. The network consists of three branches: **Pune Branch 1**, **Pune Branch 2**, and **Mumbai Branch**, each connected through routers using static routes.

## Network Topology Overview

- **Router 1** connects to Pune Branch 1.
- **Router 2** is the central router, connecting Pune Branch 2 and linking Router 1 to Router 3.
- **Router 3** connects to Mumbai Branches 1 and 2.

The routers are configured with static routes to ensure that all branches can communicate with each other. 

## Devices and Configuration

### Pune Branch 1 (Connected to Router 1)

- **Devices**: 
  - PCs: 192.10.2.10, 192.10.2.20
  - Printer: 192.10.2.30
  - Switch: 2960

### Pune Branch 2 (Connected to Router 2)

- **Devices**: 
  - PCs: 192.10.1.10, 192.10.1.20
  - Laptops: 192.10.1.30, 192.10.1.40
  - Switch: 2960

### Mumbai Branch (Connected to Router 3)

- **Devices**:
  - PCs: 192.10.4.10, 192.10.4.20, 192.10.4.30
  - Printer: 192.10.4.40
  - Switch: 2960

## Steps to Implement in Cisco Packet Tracer

1. **Add the Routers**:
   - Place three **1841 routers**: Router 1, Router 2, and Router 3.
   
2. **Add Switches and End Devices**:
   - Add the respective switches and connect end devices (PCs, laptops, printers) in each branch.

3. **Connect the Routers**:
   - Use **Ethernet or Serial links** to connect:
     - Router 1 to Router 2.
     - Router 2 to Router 3.

4. **Configure the Routers**:
   - Assign IP addresses to the routers and interfaces.
   - Configure static routing on each router.

## Router Configuration

### Router 1
```bash
Router(config)# ip route 192.10.3.0 255.255.255.0 192.10.5.2
Router(config)# ip route 192.10.4.0 255.255.255.0 192.10.5.2
Router(config)# ip route 192.10.8.0 255.255.255.0 192.10.5.2 
bash`

Router(config)# ip route 192.10.1.0 255.255.255.0 192.10.5.1
Router(config)# ip route 192.10.2.0 255.255.255.0 192.10.6.1
Router(config)# ip route 192.10.4.0 255.255.255.0 192.10.6.2

Router(config)# ip route 192.10.1.0 255.255.255.0 192.10.8.1
Router(config)# ip route 192.10.2.0 255.255.255.0 192.10.8.1
Router(config)# ip route 192.10.5.0 255.255.255.0 192.10.8.1

