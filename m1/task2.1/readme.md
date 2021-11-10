#Module 2 Virtualisation and Cloud Basic#
##Task 2.1##

###Part 1###

1. It's Microsoft Hyper-V and VMware ESX Server.
2. Main defferences btw Hyper-V and VMware ESX Server:
 - VMware has several RAM optimization technics, while Hyper-V sticks just with one. 
 - VMware supports more operation systems than Hyper-V.
 - VMware charges per processor, while Hyper-V pricing is based on CPU's count on each host.

###Part 2###

1. I've already got VirtualBox installed so I've updated it to the latest version for now (step 1.2):

![my VirtualBox version](./images/1.png?raw=true)

2. I've downloaded the latest version of Ubuntu Server (step 1.3).
3. I created new VM and named it "VM1_orhanishchuk" according to step 1.4

![my new VM with Ubuntu Server installed](./images/4.png?raw=true)

4. I got acquainted with start, stop, reboot, save state commands and used Host key which is right ctrl key as default (step 1.5).
	- start, stop and reboot commands - these are for running, killing and rerunning a vm;
	- save state command is used for temporary freezing, it's like a hybernation mode in the windows;
	- host key provides us the opportunity of changing focus from vm back to host machine.
5. I cloned my VM1 and named it "VM2_orhanishchuk" as described in the 1.6 step:

![clonned VM from the previous](./images/6.png?raw=true)

6. I created a group of two VM's (step 1.7):

![clonned VM from the previous](./images/7.png?raw=true)

7. I created several snapshots for the VM1 (step 1.8):

![clonned VM from the previous](./images/8.png?raw=true)

8. I exported vm appliance as an .ovi file to my host machine disk. Then I imported it like a new vm (step 1.9): 

![settings before export](./images/9.1.png?raw=true)
![exporting process](./images/9.2.png?raw=true)
![settings before import](./images/9.3.png?raw=true)
![my new imported vm](./images/9.4.png?raw=true)
