# Module 6 Networking with Linux

## Task 6.1

1. I set network adapters for each machine:

![setting network adapters](./images/1.png?raw=true)

![setting network adapters](./images/2.png?raw=true)

![setting network adapters](./images/3.png?raw=true)

2. I checked info about network interfaces with `ifconfig` and `ip addr show` commands:

![checking network interfaces info in first workstation](./images/4.png?raw=true)

![checking network interfaces info in second workstation](./images/5.png?raw=true)

3. Internal network interface hasn't ip address so lets configure it so machines can talk with each other:
For the first one I did it with the `ifconfig` command:

![configuring internal network interface for the first machine](./images/6.png?raw=true)

And for the second machine I edited network config (`/etc/netplan/00-installer-config.yaml`) file because it doesn't have the 'ifconfig' package:

![configuring internal network interface for the second machine](./images/7.png?raw=true)

4. Then I restarted network services on both machines with `sudo netplan apply` command and checked if my vm's can talk to each other:

![pinging vm1 to vm2](./images/8.png?raw=true)

![pinging vm2 to vm1](./images/9.png?raw=true)

Yeah, works like it's crazy!

5. But I still can't access the internet with my second machine. For achieve that I need to configure the first machine with NAT interface. First of all I enabled a forwarding:

![enabling a forwarding](./images/10.png?raw=true)

Then I set three rules with the `iptables` command:

![setting forwarding rules](./images/11.png?raw=true)

That's all. Then I checked an access to Internet:

![checking an access to Internet by pinging google.com](./images/12.png?raw=true)

Everything's fine, everything works!

6. To check the route to Host machine I need to know it's ip:

![getting host machine's ip](./images/13.png?raw=true)

Then I can trace that route (step 3):

![tracing the route to host](./images/14.png?raw=true)

7. I've pinged the Google DNS - '8.8.8.8' (step 4):

![pinging Google DNS](./images/15.png?raw=true)

8. I determined a resource for the ip '8.8.8.8' (step 5):

![determining a host for the ip 8.8.8.8](./images/16.png?raw=true)

9. I got the ip address for 'epam.com' domain (step 6):

![getting the ip address for 'epam.com' domain](./images/17.png?raw=true)

10. I traced the route to 'google.com' (step 8):

![tracing the route to 'google.com'](./images/18.png?raw=true)

To determine my host's default gateway I need to trace the route to any ip. For example let's use previous screenshot: on position 3 you can see the default gateway for my host machine: it's 192.168.0.1 .

