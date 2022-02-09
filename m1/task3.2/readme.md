# Module 3 Networking Fundamentals

## Task 3.2

### Connecting separated networks via Internet

1. I builded Internet network by connecting 3 PT-Empty routers with each other. But before that I inserted 5 1CGE modules in them:

![5 inserted 1CGE modules in a router](./images/1.png?raw=true)

![Internet network between three local networks](./images/2.png?raw=true)

2. I've substituted my birthday's information to the formula in the step 2 and got the IP address for my Internet: 38.4.98.0/24. Then I divided it into 4 /26-subnetworks. Why 4? Because dividing /24-subnet to /26-subnets leaves only 64 addresses for each /26-subnet. Thus 256 / 64 = 4. 

3. According to step 3 I've set 10.98.28.1/24 IP address for Router ISP1, 4.28.98.1/24 - for Router ISP3. For other routers I've set IP addresses like that:

|  | GE0/0 | GE1/0 | GE2/0 | GE3/0 |
| :---: | :---: | :---: | :---: | :---: |
| Router ISP1 | 10.98.28.1/24 | 38.4.98.65/26 | 38.4.98.194/26 | - |
| Router ISP2 | 38.4.98.1/26 | 38.4.98.66/26 | - | 38.4.98.129/26 |
| Router ISP3 | 4.28.98.1/24 | - | 38.4.98.193/26 | 38.4.98.130/26 |

![routers with IP addresses on each gateway](./images/3.png?raw=true)

For Home router I've set 38.4.98.2/26 IP address.

4. Then I've set to all pc's it's own gateway and add to each router static routing notes (step 4):

![routers with static routing notes](./images/4.png?raw=true)

And pinged from all pcs to it's gateway (step 5):

![pinging gateways from pcs](./images/5.png?raw=true)

All pinged well.

### Setting up VLAN in Data Center network

1. I checked the connection between servers in Data Center network (step 6):

![checking connection between Web Server 1 and Web Server 2](./images/6.png?raw=true)

![checking connection between Web Server 2 and Web Server 3](./images/7.png?raw=true)

![checking connection between Web Server 3 and Web Server 1](./images/8.png?raw=true)

2. According to step 7 I've changed the subnet mask for the servers to 255.255.255.192 and tried to ping and tracert Web Server 2 from Web Server 1:

![trying to ping Web Server 2 from Web Server 1](./images/9.png?raw=true)

But all packets were lost. That is why: by changing subnet mask for servers I also changed the network id for each server as showed in the table: 

|  | Network ID for /24 | Network ID for /26 |
| :---: | :---: | :---: |
| Router ISP1 (4.28.98.50) | 4.28.98.0 | 4.28.98.0 |
| Router ISP2 (4.28.98.100) | 4.28.98.0 | 4.28.98.64 |
| Router ISP3 (4.28.98.150) | 4.28.98.0 | 4.28.98.128 |

So, these three servers cannot properly sharing data with each other because they belong to, like, different networks, but connected to the same switch. After first ping from each server, the router memorized them and next pings worked just fine:

![pinging and tracerting from Web Server 1 Web Server 2](./images/10.png?raw=true)

But with one difference: every ICMP packet goes to the gateway and then to a destination. One again: that's because all servers are not in the same subnetwork. 

3. I added three new VLAN into VLAN database in the Switch0 (steps 9-10):

![three new VLAN in a Switch0's VLAN database](./images/11.png?raw=true)

And assigned these vlans to FE0/2, FE0/3 and FE0/4 accordingly. Then I tried to ping and tracert:

![trying to ping and tracert Web Server 2 from Web Server 1 with enabled VLAN for each of them](./images/12.png?raw=true)

But nothing happens, all packets are gone without a trace. This is because separate VLAN's cannot interract with each other because they're isolated like containers.

### Setting up routing between Data Center servers (additional task)

1. I switched from access to trink mode in GE0/1 in the Switch0 (step 12):

![switching GE0/1 mode to trunk in the Switch0](./images/13.png?raw=true)

2. Then I removed IP address and subnet mask from Router ISP3's GE0/0 (step 13). In CLI mode I created three subinterfaces and assigned ip addresses to them (step 14):

![3 subinterfaces in the Router ISP3](./images/14.png?raw=true)

Then I set gateway address to all servers and tried to ping servers (step 15-16):

![pinging and tracerting Web Server 2 from Web Server 1](./images/15.png?raw=true)

3. At the end of this task I aborted all changes from step 7 and saved it as lab3 file for the next task.

