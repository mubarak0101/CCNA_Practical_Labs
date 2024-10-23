
# Network Topology Configuration

## Overview
This repository contains the configuration and setup for a network topology involving four branches: Pune, Mumbai, Nagpur, and Delhi, with a central router connecting them. The network is configured using static routing, and this README provides detailed information on the setup and configuration commands used.

## Network Topology
The network topology consists of the following branches and devices:

1. **Pune Branch**
   - Devices: Printer0, PC7, PC6
   - Switch: 2960-24TT Switch3
   - Router: 1841 Router0
   - Network: 192.10.2.0/24
   - Default Gateway: 192.10.2.5

2. **Mumbai Branch**
   - Devices: PC1, PC2, Laptop0, Laptop1
   - Switch: 2960-24TT Switch1
   - Router: 1841 Router0
   - Network: 192.10.1.0/24
   - Default Gateway: 192.10.1.5

3. **Nagpur Branch**
   - Devices: Laptop0, PC2, PC3
   - Switch: 2960-24TT Switch1
   - Router: 1841 Router1
   - Network: 192.10.3.0/24
   - Default Gateway: 192.10.3.5

4. **Delhi Branch**
   - Devices: PC4, Laptop2, Printer1
   - Switch: 2960-24TT Switch4
   - Router: 1841 Router3
   - Network: 192.10.4.0/24
   - Default Gateway: 192.10.4.5

5. **Central Router**
   - Router: 1841 Router2
   - Interfaces: 192.10.5.2, 192.10.6.1

## Configuration Commands
The following static routing commands are used to configure the routers in the network:

### Pune Branch Router (Router0)
```plaintext
ip route destination net add SM next hope add
Router(config)#ip route 192.10.3.0 255.255.255.0 192.10.5.2
Router(config)#ip route 192.10.4.0 255.255.255.0 192.10.5.2
Router(config)#ip route 192.10.6.0 255.255.255.0 192.10.5.2
Mumbai Branch Router (Router1)
plaintext


ip route destination net add SM next hope add
Router(config)#ip route 192.10.1.0 255.255.255.0 192.10.6.1
Router(config)#ip route 192.10.2.0 255.255.255.0 192.10.6.1
Router(config)#ip route 192.10.5.0 255.255.255.0 192.10.6.1
Nagpur Branch Router (Router2)
plaintext


ip route destination net add SM next hope add
Router(config)#ip route 192.10.1.0 255.255.255.0 192.10.5.1
Router(config)#ip route 192.10.2.0 255.255.255.0 192.10.5.1
Router(config)#ip route 192.10.3.0 255.255.255.0 192.10.6.2
Router(config)#ip route 192.10.4.0 255.255.255.0 192.10.6.2
Delhi Branch Router (Router3)
plaintext


ip route destination net add SM next hope add
Router(config)#ip route 192.10.1.0 255.255.255.0 192.10.6.1
Router(config)#ip route 192.10.2.0 255.255.255.0 192.10.6.1
Router(config)#ip route 192.10.3.0 255.255.255.0 192.10.5.1
Router(config)#ip route 192.10.5.0 255.255.255.0 192.10.5.1
Image Description
The image depicts a network topology with four branches (Pune, Mumbai, Nagpur, and Delhi) connected via a central router. Each branch has its own set of devices and a switch, with static routing configured to enable communication between the branches.

Feel free to implement these changes! Need help with anything else?


