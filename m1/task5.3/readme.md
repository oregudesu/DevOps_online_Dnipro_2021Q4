# Module 5 Linux Essentials

## Task 5.2

### Part 1

1. There're five process states: **running**, **interruptable_sleep**, **uninterruptable_sleep**, **stopped** and **zombie**.

2. `pstree` command displays all running processes as a tree. I got all processes with highlights and it's parents:

![showing all running processes with hightlight of curent process and it's parent](./images/1.png?raw=true)

3. Proc filesystem it's a mounted pseudo-filesystem used for trace processes in a system and provides an access to the state of each active process and thread.

4. Information about a processor can be gotten by using the `lscpu` command:

![getting the info about a cpu](./images/2.png?raw=true)

5. I've displayed all processes with columns by order described in step 5:

![listing of processes with ordered information](./images/3.png?raw=true)

6. Linux processes can be run in two modes: **user** and **kernel**. User mode is the mode where all processes have some limited resources. In the contrary, kernel mode allows processes to run without any restrictions of using hardware or memory resources. 

7. I listed first 10 processes:

![listing first 10 processes](./images/4.png?raw=true)

Processes can usually have these statuses:

**D** - uninterruptible sleep process: that means that process is in the kernel space and cannot be interrupted by any signal;
**R** - running or runnable process: that is currently running;
**S** - interruptible sleep process: that process is waiting for some input;
**I** - idle process: the same as interruptible sleep process, but in the kernel space, where it can't be interrupted;
**T** or **t** - stopped process;
**X** - killed process: can't actually be seen 'cause after killing a process there is not much time it displays in the process list with this status;
**Z** - zombie process (my favorite): already terminated, but not killed by it's parent process;
**<** - high priority process;
**N** - low priority process;
**L** - locked process: it has some data that locked in the memory;
**s** - session leader process;
**l** - multi-threaded process;
**+** - foreground process.

8. I listed all processes by 'oregu' and 'bob' users:

![listing all processes by 'oregu' and 'bob' users](./images/5.png?raw=true)

As you can see at the screenshot above, bob hasn't any processes, because he's not logged in right now.

9. To analyse currently running tasks you can use the `top` utility:

![example of using the 'top' utility](./images/6.png?raw=true)

Or also the `htop` utility can be used for that purpose:

![example of using the 'htop' utility](./images/7.png?raw=true)

The difference between them is that the last one has the more advanced functionality: you can focuse on specific process and there're more useful hotkeys that in the `top` utility.

10. The `top` utility displays:

- system information (such as time, users and tasks count, cpu load, memory status);
- running process information.

This information updates every 3 seconds and renders in the terminal.

11. I displayed all processes of the 'oregu' user with the command `top -u oregu`:

![displaying all processes of the 'oregu' user](./images/8.png?raw=true)

12. You can check on available interactive commands by hitting 'h' - help command:

![top help command](./images/9.png?raw=true)

As shown above there are a lotta interactive commands. For example:

- 'z' - enable color mode:

![color mode](./images/10.png?raw=true)

- 'd' or 's' - setting the update interval for information;
- 'k' - kill a task;
- 'r' - renice a task.
- 'u' - show tasks for specific user:

![picking a user](./images/11.png?raw=true)
![sorted tasks](./images/12.png?raw=true)

Also you can refresh a screen information by hitting Enter. 

13. Now the top command view is sorted by pid:

![top command view sorted by pid](./images/13.png?raw=true)

To sort it by any column I need to press 'shift + f':

![interactive menu for choosing the sort method](./images/14.png?raw=true)

Then I chose the sorting by TIME+ (processor time that's taken, as described in the task) by hitting 's' and pressed Enter to save my choice:

![choosing the sort option](./images/15.png?raw=true)

I pressed 'q' to get back to top view and all processes are sorted by TIME+:

![top command view sorted by TIME+](./images/16.png?raw=true)

14. To run a process with a specific priority you can use the `nice` command. 
For example, you can run a python script with 5 priority by using one of these commands: `nice -5 python main.py` or `nice -n 5 pyhton main.py`.
For -5 priority (higher priority) it's `nice --5 python main.py` or `nice -n -5 pyhton main.py`.
To change a priority of running process you need to use this command: `renice -n -20 -p <process_id>`.

15. Yeah, with the 'r' interactive command's help.

16. To kill a process you can use `kill` command. There's an example: `kill -9 1234` where '-9' is the signal code and '1234' is a process id (pid).
There are a lot of signals that can be send to process:

![signals list](./images/17.png?raw=true)

The most common kill signals are:
- SIGHUP - 1 - hangup;
- SIGINT - 2 - interrupt from keyboard;
- SIGKILL - 9 - kill signal;
- SIGTERM - 15 - termination signal;
- SIGSTOP - 17, 19, 23 - stop the process.

17. For get this step done I created a simple bash script that prints a row with current datetime every 3 seconds:

![bash script](./images/18.png?raw=true)

I ran it with and redirect the output to a file /tmp/out:

![running the bash-script](./images/19.png?raw=true)

But as shown above it's blocking my terminal, so I can't do anything else while the job running. I suspended it by using 'ctrl+z' combination:

![suspending the runned bash-script](./images/20.png?raw=true)

`jobs` command displays a list of jobs with their status. Let's see it for ourselves:

![listing all jobs in system](./images/21.png?raw=true)

So it turns out that I have the only job which I ran and suspended in previous steps. To prevent it from blocking the terminal I'm gonna make it a background job by using `bg` command:

![switching the job to bg](./images/22.png?raw=true)

Now It's running at the background. With `fg` command I can switch it back to foreground:

![switching the job to fg](./images/23.png?raw=true)

We can see the interval between lines 3 and 4 - that's when I suspended the job before moving it to bg: 

![/tmp/out file](./images/24.png?raw=true)

To kill a job you need to know it's pid, then kill it:

![killing the job](./images/25.png?raw=true)

`nohup` command's used for protect a job from the SIGHUP signal, so after closing a terminal it's still alive.


### Part 2

1. The most frequently used SSH-commands in Windows:
- `ssh` is used to connect to remote host. For example, let's connect to my ubuntu-server2 workstation:

![connecting to ubuntu-server](./images/26.png?raw=true)

- `ssh-keygen` generates a new key pair for ssh authentification:

![generating a ssh key pair](./images/27.png?raw=true)

- `ssh-copy-id` installs an ssh key as an autorised key to the server. This command's available on Linux and MacOS, so I used the alternative sequence of commands in Windows10. First of all I copied the ssh public key to the authorized_keys file:

![copying the ssh public key to the authorized_keys file](./images/28.png?raw=true)

Then I made sure that ~/.ssh folder is created on my linux workstation:

![checking on ~/.ssh folder on linux](./images/29.png?raw=true)

In the place. Let's copy the authorized_keys file from windows10 to linux with `scp` command:

![copying the authorized_keys file to linux](./images/30.png?raw=true)

Then I edited the /etc/ssh/sshd_config file: change to 'no' the 'PasswordAuthentication' and 'UsePAM' properties. And restarted ssh service:

![copying the authorized_keys file to linux](./images/31.png?raw=true)

After all changes I tried to simply connect to the linux machine, without the key:

![trying to connect to the linux machine](./images/32.png?raw=true)

Alright, that works, access denied. Let's try again with the key:

![trying to connect to the linux machine with the key](./images/33.png?raw=true)

I'm in!

- `ssh-agent` is actually a service that keeps track of user's keys and passphrases. On Windows it remembers all ssh entries even after system restart, but on Linux - it works only in a single terminal session. To set private key for my second linux workstation on Windows I ran the command:

![trying to run the ssh-agent command](./images/34.png?raw=true)

But it said that there's the 1058 error. That means the service is not started on my Windows system. I ran that command in the PowerShell to allow it to start manually:

![configuring the ssh-agent service startup](./images/35.png?raw=true)

Then I started ssh-agent service and add my identity with the `ssh-add` command:

![starting the ssh-agent service and adding the identity to it](./images/36.png?raw=true)

Now I'm able to ssh to my ubuntu-server workstation without passing the ssh key every time:

![ssh to my ubuntu-server workstation with ssh-agent service](./images/37.png?raw=true)

2. For increase a security of ssh connection I've done next steps:

- I configured the idle timeout interval that allows the server to log out the idle users:

![configuring the idle timeout interval](./images/38.png?raw=true)

- I configured the max count of auth tries:

![configuring the max count of auth tries](./images/39.png?raw=true)

- I disabled empty passwords to prevent connected users from creating accounts without a password:

![disabling empty passwords](./images/40.png?raw=true)

- I limited user's access through ssh (before doing that I created a new user named 'bob'):

![limiting user's access](./images/41.png?raw=true)

- I configured the permission for root login to 'no':

![disabling the login as root user](./images/42.png?raw=true)

- I allowed only ssh protocol version 2:

![allowing only ssh protocol version 2](./images/43.png?raw=true)

- I changed a standart 22 port to custom one:

![changing a ssh port](./images/44.png?raw=true)

Then I restarted the ssh service and tried to loging in as a root user:

![trying to login in as a root user](./images/45.png?raw=true)

But the server refused my connection because of the port I'm trying to connect to. So, let's connect to the right port as root user:

![trying to login in as a root user to the right port](./images/46.png?raw=true)

But the server's still refusing my connection, now because it doesn't allow the root user to connect through ssh. Let's try the 'bob' user:

![trying to login in as the bob user to the right port](./images/47.png?raw=true)

And everything works!









