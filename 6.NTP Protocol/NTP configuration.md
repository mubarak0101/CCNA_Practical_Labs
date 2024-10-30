

# NTP Configuration Network Topology


The topology includes:
- One NTP Server (Router184) configured as the **NTP Master**.
- Multiple NTP Clients (Routers6, 7, 8, and 9) which synchronize their clocks with the NTP Server.
- PCs connected to switches to verify time synchronization across the network.

## Network Layout and IP Addressing

### Devices and IP Addresses

| Device       | Interface    | IP Address  | Role           |
|--------------|--------------|-------------|----------------|
| Router184    | Fa0/0        | 10.1.1.1    | NTP Server (Master) |
| Router6      | Fa0/0        | 10.1.1.2    | NTP Client    |
| Router8      | Fa0/0        | 50.1.1.1    | NTP Client    |
| Router7      | Fa0/0        | 20.1.1.2    | NTP Client    |
| Router9      | Fa0/0        | 30.1.1.1    | NTP Client    |
| PC0          | Fa0          | 60.1.1.2    | Time Verification |
| PC1          | Fa0          | 40.1.1.2    | Time Verification |
| PC2          | Fa0          | 10.1.1.3    | Time Verification |
| PC3          | Fa0          | 60.1.1.3    | Time Verification |

### Connection Overview
- **Router184** (NTP Server) distributes time information to all other routers, configured as NTP clients.
- Switches provide connectivity for PCs to routers, enabling time verification.

---

## Device Roles and Configuration

### 1. NTP Server (Master) - Router184

Router184 is designated as the NTP Server (Master) for the entire network. This router maintains the authoritative time source, and other devices synchronize their time with this router.

**NTP Master Configuration**:
```bash
Router184(config)# clock set 16:42:40 Oct 10 2024
Router184(config)# ntp master
```

- **Command Explanation**:
  - `clock set <time> <date>`: Sets the system time.
  - `ntp master`: Configures the router as an NTP master, making it the authoritative source of time for the network.

### 2. NTP Clients - Routers (6, 7, 8, and 9)

The remaining routers in the network (Router6, Router7, Router8, and Router9) are configured as NTP clients. They use Router184 as their NTP server to synchronize their clocks.

**NTP Client Configuration Example**:
```bash
Router(config)# ntp server 10.1.1.1
```

- **Command Explanation**:
  - `ntp server <IP>`: Configures the router to use the specified IP (10.1.1.1) as its NTP server.

### 3. PC Configuration

PCs are connected to routers via switches to allow time verification across different segments of the network. They check connectivity and validate time synchronization from their connected router.

---

## Verification and Troubleshooting

### Verification Commands

To confirm successful NTP configuration and time synchronization on the routers, use these commands:

- **Show Clock**: Displays the current time on the router.
  ```bash
  Router# show clock
  ```

- **Show NTP Status**: Provides the status of the NTP client configuration.
  ```bash
  Router# show ntp status
  ```

- **Show NTP Associations**: Lists the NTP servers with which the client is synchronized.
  ```bash
  Router# show ntp associations
  ```

### Sample Output for Verification
The following outputs indicate that NTP is functioning as expected:
- `show clock` should display a synchronized timestamp similar to the master router.
- `show ntp status` should show a status of "synchronized" for clients.
- `show ntp associations` should show the NTP master IP as a reference.

### Troubleshooting Steps

If there are issues with NTP synchronization, consider these steps:

1. **Verify NTP Master Configuration**:
   - Ensure `ntp master` is set on Router184.
   - Check that the clock on Router184 is correctly set.

2. **Check Client Configuration**:
   - Confirm that each client router has the `ntp server` command pointed to Router184’s IP.
   - Verify connectivity between each client router and the NTP server.

3. **Network Connectivity**:
   - Use `ping` to verify that each client router can reach the NTP server (Router184).
   - Ensure all IP addresses are correctly configured on each device.

4. **Verify NTP Status**:
   - Run `show ntp status` on clients. If the status is "unsynchronized," check for connectivity and configuration errors.
   
5. **Check for Firewalls or ACLs**:
   - Ensure that there are no firewall rules or ACLs blocking NTP traffic (port 123) between routers.

