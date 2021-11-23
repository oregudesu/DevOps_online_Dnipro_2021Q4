# Module 2 Virtualisation and Cloud Basic
## Task 2.1

### Part 1

1. It's Microsoft Hyper-V and VMware ESX Server.
2. Main defferences btw Hyper-V and VMware ESX Server:
 - VMware has several RAM optimization technics, while Hyper-V sticks just with one. 
 - VMware supports more operation systems than Hyper-V.
 - VMware charges per processor, while Hyper-V pricing is based on CPU's count on each host.

### Part 2

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

9. I explored VM configurations options (step 2.1):
 - in the general settings we can set up a name and an operation system for our vm. Also we can specify a snapshot folder and set up disc encryption;
 - in the system settings we can dedicate a memory of RAM and CPU's count. Also we can set the boot order up;
 - display settings allow us to change count of dedicated video memory, set up the vm for several physical monitors (up to 8), pick graphics controller, set up remote display and video recording;
 - the storage tab give us settings for a hard drive: we can add, remove them and change it's type;
 - in the audio tab we can select audio driver and controller for our vm;
 - network settings allow us to create network adapters and set them up;
 - in the serial ports tab we can create and set COM ports; 
 - the usb tab allows us to pick an usb controller to get access to usb devices from host machine;
 - in the shared folder settings we can set up a shared folder for share data between host and virtual machines;
 - and user interface settings allow us to change interface control of vm window. 
 
10. I configured USB setting for my vm (step 2.2):

![configuring usb settings](./images/10.1.png?raw=true)

Then I attached my USB drive to the vm:

![attaching my usb device](./images/10.2.png?raw=true)

And checked if the vm sees my USB drive:

![checking if the vm sees my usb device](./images/10.3.png?raw=true)
(1 - before attach, 2 - after attach)

Ok, let's get access to files in the USB drive. First of all, this drive needs to be mounted in Ubuntu Server:

![mounting usb device](./images/10.4.png?raw=true)

There we go. Now let's check on files on the drive:

![configuring usb settings](./images/10.5.png?raw=true)

Yeah, that's exactly what it have!

11. For setting up the shared folder (step 2.3) first of all I created this folderon my host machine. I called it "test_folder_for_vm" and created a readme.txt file inside. 
Then I specify a path to that folder in the Shared Folder settings for my vm:

![specifying a path to the shared folder on the host machine](./images/11.1.png?raw=true)

I ran the vm and in the top tab Devices I launched "Insert Guest Additions CD Image":

![launching Insert Guest additions CD Image](./images/11.2.png?raw=true)

Then I mounted a file that represents my shared folder to the image directory for getting it ready to use:

![mounting a file that represents the shared folder in Linux system](./images/11.3.png?raw=true)

And installed build-essential and linux-headers dependencies:

![installing build-essential and linux-headers libs](./images/11.4.png?raw=true)

And installed VirtualBox Guest Additions:

![installing VirtualBox Guest Additions](./images/11.5.png?raw=true)

After that I restart my machine. Once it's restarted, I mounted all files from my shared folder to the /shared dir:

![mounting all files from shared folder to /shared dir](./images/11.6.png?raw=true)

And checked out for accessing data from the shared folder:

![checking accesing to files from my shared folder](./images/11.7.png?raw=true)

Yeah! It works great!

12. In this step I tried to ping different devices in different network types (step 2.4). But my first try with NAT Network failed, because two of my vm's have been generating the same IP.
My first guess was MAC adresses sameness. But changing it to different ones for each maching doesn't give a shot. After some time of research I finally found the problem: machine-id sameness!
When I cloned my first machine, I do it for all it's settings. So, I found a path where it stores and checked it on two my vm's:

![comparison machine-id's for two my vm's](./images/12.1.png?raw=true)

Gotcha! Ok, It's need to be regenerated at least for one of the vm's. I checked, is it a file or a shortcut:

![checking on machine-id file type](./images/12.2.png?raw=true)

So, it's a shortcut. The original file is in the /etc/ dir. Let's remove and regenerated it:

![removing and regenerating vm's machine-id](./images/12.3.png?raw=true)

And take a look at that file:

![checking on results](./images/12.4.png?raw=true)

It's done, a machine-id's changed.
Then I tested all types of network and created a table of connections:

|  | VM1 <-> VM2 | VM -> Host | Host -> VM | VM -> LAN | LAN -> VM |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **NAT** | - | + | - | + | - |
| **Bridget Adapter** | + | - | + | + | + |
| **Internal Network** | - | - | - | - | - |
| **Host-only Adapter** | + | - | + | - | - |
| **NAT Network** | + | + | - | + | - |


13. According to steps 3.1-3.2 I need to examine commands of vmbox cli. To do so I desided to start with information about my installed VM's:

![getting info about installed vm's](./images/13.1.png?raw=true)

But my cmd doesn't see the VMBox tools. I need to add the path to VirtualBox directory to the system path:

![adding the VirtualBox path to the system path](./images/13.2.png?raw=true)

Done! Then I tried to do the vboxmanage command:

![getting info about installed vm's, second attempt](./images/13.3.png?raw=true)

Works perfectly! Lets try to get info about one vm:

![getting info about the first vm](./images/13.4.png?raw=true)

The output's too long so I showed just a part. Lets launch that vm:

![launching the first vm](./images/13.5.png?raw=true)

Yeah, it's started! Lets power it off:

![powering off the first vm](./images/13.6.png?raw=true)

Exactly. What about create one:

![creating a new vm](./images/13.7.png?raw=true)

Then create a medium:

![creating a medium for the new vm](./images/13.8.png?raw=true)

Attach SATA controller to the medium:

![attaching a SATA controller to the medium](./images/13.9.png?raw=true)

And attach IDE controller to the Ubuntu Server iso:

![attaching an IDE controller to the Ubuntu Server iso](./images/13.10.png?raw=true)

Fine! Lets start our new vm and look if os installation go properly:

![launching the new vm](./images/13.11.png?raw=true)

YUMMY! And last command: take a snapshot from the new machine. Lets create a new folder in the new vm:

![creating a new folder in the new vm](./images/13.12.png?raw=true)

And take a snapshot:

![taking a snapshot with recent changes](./images/13.13.png?raw=true)
