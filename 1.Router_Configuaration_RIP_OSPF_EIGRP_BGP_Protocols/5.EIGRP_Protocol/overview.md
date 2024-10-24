
# EIGRP Protocol Overview

## What is EIGRP?
EIGRP (Enhanced Interior Gateway Routing Protocol) is a Cisco proprietary routing protocol that combines the features of distance vector and link-state protocols. It is designed for IP networks and provides efficient and scalable routing, quick convergence, and reduced bandwidth usage through its use of advanced metrics.

## EIGRP Characteristics
- **Hybrid Protocol**: Combines the advantages of both distance vector and link-state protocols.
- **Fast Convergence**: Uses the DUAL (Diffusing Update Algorithm) to quickly calculate the best paths and converge rapidly after topology changes.
- **Support for Multiple Protocols**: Can route not just IPv4, but also IPv6, IPX, and AppleTalk, though primarily used for IPv4 and IPv6 today.
- **Reduced Bandwidth Usage**: Sends incremental updates rather than full routing tables, minimizing bandwidth consumption.
- **Metric Calculation**: Uses a composite metric based on bandwidth, delay, reliability, load, and MTU (Maximum Transmission Unit).

## EIGRP Operation
EIGRP operates through several key processes:
1. **Neighbor Discovery**: Routers use Hello packets to discover and maintain neighbor relationships.
2. **Topology Table Maintenance**: EIGRP routers maintain a topology table that stores all the routes learned from neighbors.
3. **DUAL Algorithm**: EIGRP uses the DUAL algorithm to determine the best path and backup routes, ensuring loop-free and efficient routing.
4. **Route Advertisement**: EIGRP sends routing updates only when there are changes in the topology, and these updates contain only the changes rather than the entire routing table.

## EIGRP Metrics
EIGRP uses a composite metric calculated with the following formula:
\[ \text{Metric} = \left( \frac{10^7}{\text{minimum bandwidth}} + \text{total delay} \right) \times 256 \]
- **Bandwidth**: The lowest bandwidth along the path.
- **Delay**: The cumulative delay of the path, measured in microseconds.

## EIGRP Packet Types
EIGRP uses five types of packets to communicate:
1. **Hello Packets**: Used for neighbor discovery and maintenance.
2. **Update Packets**: Contain routing information and updates to the routing table.
3. **Query Packets**: Request information about routes from neighbors.
4. **Reply Packets**: Respond to queries with the requested routing information.
5. **Acknowledgment Packets**: Acknowledge the receipt of update packets.

## EIGRP Configuration Examples
### Basic EIGRP Configuration (Cisco IOS)
```bash
Router(config)# router eigrp 1
Router(config-router)# network 192.168.1.0 0.0.0.255
```

### EIGRP Configuration with Multiple Networks
```bash
Router(config)# router eigrp 1
Router(config-router)# network 192.168.1.0 0.0.0.255
Router(config-router)# network 10.0.0.0 0.255.255.255
```

### Configuring EIGRP for IPv6
```bash
Router(config)# ipv6 router eigrp 1
Router(config-rtr)# no shutdown
Router(config-rtr)# ipv6 eigrp 1
Router(config)# interface GigabitEthernet0/0
Router(config-if)# ipv6 eigrp 1
```

## Common EIGRP Commands
- **Show EIGRP Neighbors:**
  ```bash
  show ip eigrp neighbors
  ```
- **Show EIGRP Routing Table:**
  ```bash
  show ip route eigrp
  ```
- **Show EIGRP Topology Table:**
  ```bash
  show ip eigrp topology
  ```
- **Configure EIGRP Metrics:**
  ```bash
  router eigrp 1
  metric weights 0 1 1 1 1
  ```

## Troubleshooting EIGRP
Common issues and troubleshooting steps:
- **Neighbors Not Forming:**
  - Verify EIGRP process ID is the same on both routers.
  - Check the network statements to ensure they include the correct subnets.
  - Ensure Hello and hold intervals match on both routers.

- **Routes Not Appearing:**
  - Use `show ip eigrp topology` to verify that routes are being advertised.
  - Check for any access lists that might be blocking EIGRP packets.

- **Slow Convergence:**
  - Investigate network changes or instability that may affect the DUAL calculations.
  - Check for route flapping that could lead to suboptimal routing.

---

