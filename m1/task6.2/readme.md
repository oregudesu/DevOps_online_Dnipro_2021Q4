# Module 6 Networking with Linux

## Task 6.2

1. For achive the result described in the task 6.2 I clonned my second VM (VM4_orhanishchuk) from the previous task:

![clonning VM from the previous task](./images/1.png?raw=true)

2. I regenerated the machine-id like I've described in the task 2.1:

![regenerating the vm's machine-id](./images/2.png?raw=true)

3. There's one more thing: while clonning the machine an ip address in the network config has been copied as well, so now these two vm's have the same ip. I changed the ip for the new vm:

![changing the ip addres for the new vm](./images/3.png?raw=true)

Then I restarted the network service with `sudo netplan apply`.

4. I installed and configured dhcp server in two ways (step 2):

- using vboxmanage:

	I added dhcp server via `vboxmanage dhcpserver add` command:
	
![configuring dhcp server via vboxmanage](./images/4.png?raw=true)

	Then I configured network for all three vm's: for the first one I added internal network interface with 'dhcp4: true' property, for the rest two vm's I commented assigning static ip address and uncommented 'dhcp: true' property:
	
![configuring network for three vm's](./images/5.png?raw=true)

	Then I restarted my host machine and looked at ip addresses for each vm:
	
![checking on the ip address for each vm](./images/6.png?raw=true)

	Yes, the dhcp server gave for every vm it's own ip address. I pinged every machine from all of them:
	
![pinging machines between itselves](./images/7.png?raw=true)

Works great.

- using isc-dhcp-server:
 
	I installed the isc-dhcp-server package with `sudo apt-get install isc-dhcp-server`. Then I edited the `/etc/dhcp/dhcpd.conf` file:
	
![configuring dhcp server](./images/8.png?raw=true)

	And I defined the network interface in the `/etc/default/isc-dhcp-server`:
	
![defining the network interface](./images/9.png?raw=true)

	I checked a status of the dhcp server:
	
![checking a status of the dhcp server](./images/10.png?raw=true)
	
	But it's failed to launch. Let's find out why by reading logs from it's process (as we can see at the previous screen, process_id = 38983):
	
![reading logs for that process](./images/11.png?raw=true)

	Oops, I missed a semicolon between domain-name-servers in the `/etc/dhcp/dhcpd.conf`. Let's fix this:
	
![fixing dhcpd.conf file](./images/12.png?raw=true)

	Now let's check the running status:
 
![checking a status of the dhcp server](./images/13.png?raw=true)

	Still not working. Let's check process logs:
	
![checking process logs](./images/14.png?raw=true)

	It says "No subnet declaration for enp0s8 (No IPv4 addresses)". Of course! I haven't set an IP address for that machine because I've set the dhcp server on vmbox and it gives that machine an IP address as well as others. But in that case I use that machine like a dhcp server, so it need to have the ip address set. So let's modify `/etc/netplan/00-installer-config.yaml`: add the IP address and comment dhcp option:
	
![modifying network config](./images/15.png?raw=true)

	Also I've changed a lil bit config in the `/etc/dhcp/dhcpd.conf`, found one in the [ubuntu documentation](https://help.ubuntu.com/community/isc-dhcp-server):

![changing dhcp config](./images/16.png?raw=true)

	So, let's restart the service and check on it's status:
	
![restarting the service and checking it's status](./images/17.png?raw=true)
	
	Hell yeah! It's finally running!
	Let's also check if dhcp server gave to another two machines IP addresses:
	
![checking IP addresses on other two machines](./images/18.png?raw=true)

	Yes it did!
	As always, ping time:
	
![pinging machines](./images/19.png?raw=true)
	
5. I installed and configured DNS server using `dnsmasq` service (step 4):

	First of all I disabled and stopped the `systemd-resolved` dns-service because it works on port 53 and there may be the conflict in dnsmasq:
	
![disabling and stopping the systemd-resolved service](./images/20.png?raw=true)

	Then I installed dnsmasq package with `sudo apt-get install dnsmasq`. And moved to it's configuration, first in the `/etc/dnsmasq.conf` file.
	I uncommented the port 53 property:

![editing /etc/dnsmasq.conf file](./images/21.png?raw=true)

	I uncommented these two options for enable requests filtering in the dns server:
	
![editing /etc/dnsmasq.conf file](./images/22.png?raw=true)
	
	I enabled strict checking order for all nameservers described in the `/etc/resolv.conf`:
	
![editing /etc/dnsmasq.conf file](./images/23.png?raw=true)

	Then I edited the `/etc/hosts` file, I filled it in with names and ip addresses of all my vm's:
	
![editing /etc/hosts file](./images/24.png?raw=true)

	Then I edited the `/etc/resolv.conf` file with filling it in with two nameservers: my local dns server and google dns server (8.8.8.8) for managing global internet names:
	
![editing /etc/resolv.conf file](./images/25.png?raw=true)

	After that I restarted dnsmasq service with `sudo systemctl restart dnsmasq` command and tried to ping two vm's by their names from the main vm:
	
![pinging vm's from the main vm by their names](./images/26.png?raw=true)

	Let's ping the main machine from these two vm's too (step 5):
	
![pinging main vm's from the rest two machines](./images/27.png?raw=true)

	But they just don't see that host by it's name! It's because the dns server ip's described in their configs are just google's dns servers. These vm's don't know the ip address for the local dns server. So I need to add that ip address to dhcp server's config on the main machine:
	
![editing /etc/dhcp/dhcpd.conf file](./images/28.png?raw=true)

	I restarted dhcp server on the main vm and network interfaces on all vm's. Let's check the ping now:
	
![editing /etc/dhcp/dhcpd.conf file](./images/29.png?raw=true)

	It works!

