# Module 5 Linux Essentials

## Task 5.2

1. `/etc/passwd` file stores the info about user accounts in the system:

![/etc/passwd file's content](./images/1.png?raw=true)

Each row has several fields separated by a colon. There are (in right order): 

- username;
- x character that indicates a password; 
- user id (UID);
- group id (GID);
- user id info;
- user's home directory path;
- default shell for user.

There are three types of users in Linux system: **root**, **regular** and **service**. 
**Root user** is automatically created when Linux is installed. 
**Regular users** have some privileges for perform daily tasks and can be created by root user.
**Service users** are created by softwares and allow them to interract with Linux system. These 'users' are also called **pseudo users**.
For determine which user are pseudo I need to look at user id - they have from 1 to 499. For example, in the screenshot below there are these pseudo users: daemon, bin, sys, sync, games etc.

`etc/group` file stores the info about groups:

![/etc/group file's content](./images/2.png?raw=true)

Like the previous file, it has rows with next fields:

- group name;
- password;
- group id;
- group members.

2. UID - it's a user id. It's written at the first field in `/etc/passwd` file.
Users have these UID ranges:

- root user: UID's always 0;
- regular users: UID starts from 500;
- service users: UID's in between 1 and 499.

3. GID - it's a group id. It can be seen in both `/etc/passwd` and `/etc/group` files.

4. To define what group the current user belongs to, there's a `group` command:

![check what group the current user belongs to](./images/3.png?raw=true)

To check another user I need to add his/her nickname after the command.

5. To add user to the system I can use `useradd` command:

![creating a new user](./images/4.png?raw=true)

I used `-m` key so that user's created with their home directory. Then I created a password for the new user to being able to log in:

![creating a password for the new user](./images/5.png?raw=true)

6. Before changing username I have to be sure it'll work. So firstly I have checked the list of regular users, then changed guest user's name to 'bob' and checked users one more time:

![changing username](./images/6.png?raw=true)

Yes, it changed username, but didn't change user's home directory and default shell. To change 'em I ran these commands:

![changing user's home directory](./images/7.png?raw=true)

![changing user's default shell](./images/8.png?raw=true)

And I tried to log in as new user:

![logging in as new user](./images/9.png?raw=true)

7. `/etc/skel/` directory is used to initiate home dir when a user's first created:

![/etc/skell/ dir content](./images/10.png?raw=true)

8. To remove a user from system you can use a `userdel` command. To remove also their mailbox and home dir, you should add `-r` key:

![removing user from system with home dir and mailbox](./images/11.png?raw=true)

9. To lock a user you can use `passwd -l username` or `usermod -l username` command:

![locking the bob user](./images/12.png?raw=true)

After the command's complete I checked if 'bob' user is locked with status command: `sudo passwd -S bob`. Second parameter has 'L' value which means 'Locked', so the command worked perfectly.
To unlock a user you can use `passwd -u username` or `usermod -u username` command:

![unlocking the bob user](./images/13.png?raw=true)

And one more check after: the second parameter is 'P' which means 'Password', so bob's unlocked now.

10. To delete a password from user you should use the `sudo passwd -d username` command. I deleted a password for the 'bob' user:

![deleting a password for the bob user](./images/14.png?raw=true)

And checked it out:

![logging in as bob user](./images/15.png?raw=true)

It worked!

11. The command `ls -ld dir_path` is used to see extended information about a directory: 

![getting extended info about /learning dir](./images/16.png?raw=true)

This output has next columns: permissions, number of hardlinks, owner and group names, size in bytes, modification datetime and dir name. 

12. Access rights diagram looks like that: `-rwxrwxrwx`.
It has four parts, lemme separate them by vertical line: `-|rwx|rwx|rwx`. 
So first part describes the file type. It can be `-` for the regular file. `d` for the directory, `b` for the block device, `c` for the character device, `l` for the symbolic link, `p` for the pipe, `s` for the socket.
Second, third and fourth parts set access rights for owner of this file, group owner of this file and for all of users. 
Now a bit more about access rights format, there are three keys: `r` - for reading, `w` - for writing and `x` - for executing. These keys also have a numerical value: for `r` it's 4, for `w` it's 2 and for `x` it's 1. For each group these values can be summarized, for example `rw-` -> 4 + 2 = 6 or `rwx` -> 4 + 2 + 1 = 7. 

13. For example, I wanna know relationship between the '/learning/123.txt' and 'bob' user. First of all I need to check information about the user:

![checking information about 'bob' user](./images/17.png?raw=true)

Alright, he's member only of one group - 'guest'. Then I check extended info of the file:

![checking extended info of the file](./images/18.png?raw=true)

It says that file was created by 'oregu' user and belongs to 'oregu' group. For owner and for group it has read and write permissions, but for all another users - it can only be red. So the user 'bob' can read this file, but not else. 

14. Changing an owner of a file is available with the `chown` command. For example, I wanna change the owner of the '/learning/123.txt' file to 'bob':

![changing the owner of the /learning/123.txt file to 'bob'](./images/19.png?raw=true)

And let's add the executable access rights of this file with the `chmod` command for all regular users:

![changing the access mode of the /learning/123.txt file for all regular users](./images/20.png?raw=true)

15. As I've already described above, 4 stands for `r` or read permission, 2 stands for `w` or write permission and 1 stands for `x` or execute permission. 
`umask` determines the permissions for newly created files. It can be used to control permissions by default. You can change it's value by appending or editing relevant row in '/etc/profile' or '~/.bashrc' file. 

16. Sticky bit is the permission that is set on the file or dir and allows only the owner of the file (or root user) remane and delete the file. It can be set with `chmod` command: 

![setting the sticky bit to the file](./images/21.png?raw=true)

Let's test it out. But I can do this only from a new user, so I'll create him, add to the 'oregu' group, log in as him and try to remove the file:

![creating a new user](./images/22.png?raw=true)

![adding the user to 'oregu' group](./images/23.png?raw=true)

![logging in as new user](./images/24.png?raw=true)

![trying to remove the '123.txt'](./images/25.png?raw=true)

There are two more bits: **setuid** and **setguid**. The setuid bit allows users to execute file with privileges of it's owner. To set this bit you can run `chmod u+s file` command. 
The setgid bit allows users to execute file with privileges of the group of it's owner. To set it you can tun `chmod g+s file_or_dir`

17. I think as it's a command script file then it need to have an executable attribute. The question is who's allowed to run that script: owner, group or everyone? 

