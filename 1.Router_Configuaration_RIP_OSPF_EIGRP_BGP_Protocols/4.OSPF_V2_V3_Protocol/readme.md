
# OSPF Multi-Area Network Topology with DR/BDR Election

## Overview
This document describes the OSPF (Open Shortest Path First) multi-area network topology, focusing on the Designated Router (DR) and Backup Designated Router (BDR) election process. The topology consists of three areas: Area 0 (Backbone), Area 1, and Area 2, each containing multiple devices including PCs, laptops, printers, and routers.

## Topology Description

### Area 0 (Backbone)
- **Router0 Configuration:**
  ```plaintext
  Router(config)#router ospf 1
  Router(config-router)#router-id 1.1.1.1
  Router(config-router)#network 192.10.1.0 0.0.0.255 area 0
  Router(config-router)#network 192.10.3.0 0.0.0.255 area 1
  Router(config-router)#network 192.10.6.0 0.0.0.255 area 2
  Router(config-router)#exit
Devices and IP Addresses:

Printer0: 192.10.1.60 / 255.255.255.0 / 192.10.1.5

Laptop0: 192.10.1.50 / 255.255.255.0 / 192.10.1.5

PC0: 192.10.1.10 / 255.255.255.0 / 192.10.1.5

PC3: 192.10.1.20 / 255.255.255.0 / 192.10.1.5

PC5: 192.10.1.30 / 255.255.255.0 / 192.10.1.5

Area 1
- **Router0 Configuration:**
  ```plaintext
Router(config)#router ospf 1
Router(config-router)#network 192.10.3.0 0.0.0.255 area 1
Router(config-router)#network 192.10.5.0 0.0.0.255 area 1
Router(config-router)#exit

  
Devices and IP Addresses:

PC2: 192.10.5.10 / 255.255.255.0 / 192.10.5.5

PC4: 192.10.5.20 / 255.255.255.0 / 192.10.5.5

PC7: 192.10.5.40 / 255.255.255.0 / 192.10.5.5

Printer1: 192.10.5.60 / 255.255.255.0 / 192.10.5.5

Laptop1: 192.10.5.50 / 255.255.255.0 / 192.10.5.5

Area 2
- **Router1 Configuration:**
  ```plaintext
Router(config)#router ospf 1
Router(config-router)#network 192.10.6.0 0.0.0.255 area 2
Router(config-router)#network 192.10.2.0 0.0.0.255 area 2
Router(config-router)#exit


Devices and IP Addresses:

PC2: 192.10.2.10 / 255.255.255.0 / 192.10.2.5

PC4: 192.10.2.20 / 255.255.255.0 / 192.10.2.5

PC6: 192.10.2.30 / 255.255.255.0 / 192.10.2.5

PC7: 192.10.2.40 / 255.255.255.0 / 192.10.2.5

Printer2: 192.10.2.60 / 255.255.255.0 / 192.10.2.5

Laptop2: 192.10.2.50 / 255.255.255.0 / 192.10.2.5

Conclusion
This README provides a clear structure for understanding the OSPF multi-area network topology with the accurate IP addressing scheme. Follow the configuration steps to implement and verify the OSPF network.

