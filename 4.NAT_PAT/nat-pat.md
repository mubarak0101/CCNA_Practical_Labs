
# NAT Network Topology


## Overview of NAT Types

### 1. **Static NAT**
   - **Purpose**: Maps a specific private IP address to a specific public IP address on a one-to-one basis.
   - **Use Case**: Useful for devices that require a consistent public IP address for external access (e.g., web servers, mail servers).
   
### 2. **Dynamic NAT**
   - **Purpose**: Assigns a public IP address from a pool of addresses to a private IP address on a one-to-one basis when needed.
   - **Use Case**: Ideal for organizations with a limited pool of public IP addresses and many internal devices that need occasional internet access.
   
### 3. **PAT (Port Address Translation)**
   - **Purpose**: Allows multiple devices on a private network to share a single public IP address, distinguished by unique port numbers.
   - **Use Case**: Common for home and small business networks, allowing all internal devices to access the internet simultaneously.

## Topology Overview

The topology consists of an **inside network** (private) and an **outside network** (public/global IP network):

- **Inside Network**:
  - A subnet (192.168.10.0/24) with multiple PCs (PC4, PC5, PC6, PC7).
  - Private IP addresses are not routable on the internet, requiring NAT to communicate with external servers.

- **Outside Network**:
  - Public-facing IPs assigned to servers (Server2 and Server3) and internet-facing routers.
  - Public IP addresses allow these devices to communicate with the broader internet.

## Detailed NAT Configurations

### 1. Static NAT Configuration

Static NAT is configured for fixed one-to-one mapping between internal and external IPs. This is beneficial when specific internal devices need predictable public IP addresses for applications that require consistent IPs, such as a hosted web server.

#### Configuration Steps:

1. **Define Static NAT Mappings**:
   - Each private IP is mapped to a specific public IP. For instance:
     ```plaintext
     Router(config)# ip nat inside source static 192.168.10.1 100.1.1.3
     Router(config)# ip nat inside source static 192.168.10.2 100.1.1.4
     Router(config)# ip nat inside source static 192.168.10.3 100.1.1.5
     Router(config)# ip nat inside source static 192.168.10.4 100.1.1.6
     ```

2. **Configure NAT Interfaces**:
   - Mark the inside and outside interfaces:
     ```plaintext
     Router(config)# interface fa0/0
     Router(config-if)# ip nat inside
     Router(config-if)# exit
     Router(config)# interface fa0/1
     Router(config-if)# ip nat outside
     Router(config-if)# exit
     ```

3. **Verify Static NAT**:
   - Use the command `show ip nat translations` to confirm the mappings.

### 2. Dynamic NAT Configuration

Dynamic NAT uses a pool of public IP addresses to assign dynamically to devices when they initiate traffic to the outside network. This setup is suitable for scenarios where a limited number of public IPs are available for a large number of internal devices.

#### Configuration Steps:

1. **Define a Pool of Public IP Addresses**:
   - Specify the range of public IPs that NAT can dynamically assign:
     ```plaintext
     Router(config)# ip nat pool public_pool 100.1.1.10 100.1.1.20 netmask 255.255.255.0
     ```

2. **Create Access List to Identify Inside Addresses**:
   - Define an access list to permit internal addresses that are eligible for NAT:
     ```plaintext
     Router(config)# access-list 1 permit 192.168.10.0 0.0.0.255
     ```

3. **Link the Access List to the NAT Pool**:
   - Associate the access list with the NAT pool for dynamic address allocation:
     ```plaintext
     Router(config)# ip nat inside source list 1 pool public_pool
     ```

4. **Verify Dynamic NAT**:
   - Use `show ip nat translations` to see dynamically allocated IP addresses.
   - Check `show ip nat statistics` for NAT usage statistics.

### 3. PAT (Port Address Translation) Configuration

PAT (also known as NAT overload) allows multiple devices on the inside network to share a single public IP address, using unique port numbers to distinguish each session. PAT is highly efficient for large networks needing simultaneous internet access through a single public IP.

#### Configuration Steps:

1. **Define Access List for Inside Addresses**:
   - Specify the internal IP range for PAT:
     ```plaintext
     Router(config)# access-list 1 permit 192.168.10.0 0.0.0.255
     ```

2. **Configure PAT Overload**:
   - Configure the router to overload the outside interface IP, allowing multiple devices to share the same public IP:
     ```plaintext
     Router(config)# ip nat inside source list 1 interface fa0/1 overload
     ```

3. **Verify PAT**:
   - Use `show ip nat translations` to see port-mapped translations.
   - Check `show ip nat statistics` for PAT statistics.

## Routing Configuration for External Access

To allow internal devices to route traffic through the NAT-enabled router to the outside network:

1. **Set a Default Route** on each router pointing to the next hop or internet:
   ```plaintext
   Router(config)# ip route 0.0.0.0 0.0.0.0 [next-hop-IP]
   ```

2. Ensure that each device and server in the topology can resolve routes to communicate effectively.

## Testing and Verification

- **Testing Connectivity**:
  - From an internal PC, ping an external server to verify that NAT is functioning.
  - Use packet-tracing tools within Cisco Packet Tracer or similar tools to confirm that NAT is translating addresses as expected.

- **Verification Commands**:
  - `show ip nat translations`: Displays current NAT translations.
  - `show ip nat statistics`: Provides statistics on the number of active NAT translations and errors.

## Additional Notes

- **NAT Selection**:
  - **Static NAT** is ideal for consistent one-to-one mappings.
  - **Dynamic NAT** is optimal when only a few public IPs are available for a large internal network.
  - **PAT** is the best choice when a single public IP needs to serve multiple internal clients.

- **Potential Issues**:
  - Insufficient public IPs in the pool for Dynamic NAT may lead to failed translations.
  - PAT port conflicts can occur in high-traffic environments, though this is rare.

## How to Use This Project

1. **Download and Load Topology**: Use a network simulation tool like Cisco Packet Tracer.
2. **Apply Configurations**: Follow the specific configuration steps for each NAT type.
3. **Test and Verify**: Ensure proper operation and connectivity with the internet and external servers.

## Lincence and bug reporting
Enjoy and report bugs to https://github.com/mubarak0101/CCNA_Practical_Labs/issues

This is a free project to be used as you like at your own risk as long as you abide by CC0-1.0. https://choosealicense.com/licenses/cc0-1.0/

