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

12. 


