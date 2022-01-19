# Module 5 Linux Essentials

## Task 5.1

### Part 1

1. I used Ubuntu Server as a workstation. So I logged in as root (step 1.1) and changed the password to a new one (step 1.2):

![changing the password for root user](./images/1.png?raw=true)

Changing a user password does change the 'passwd' system file that contains one line for each user. This file is in the /etc/ directory. Moreover there are two more files: 
- 'shadow' that contains encrypted passwords, user data and other password info (such as data of last password change, min and max password age, etc);
- 'passwd-' that contains backups for passwords from 'passwd' file.

2. I determined the users registered in this system, it's just root (me) (step 1.3):

![determining the users registered in this system](./images/2.png?raw=true)

By using `w` command you can get user name, the name of terminal in which user works, the remote host (if user's connected from outside through ssh for example), login, idle, JCPU and PCPU time and command that user are running now. `who` command gives us a sumplified information about users in the system: just user name, terminal and login time.

3. I added some personal info to my root account (step 1.4):

![adding personal info for root user](./images/3.png?raw=true)

And for check it out I installed the finger lib, then entered `finger` command:

![checking out user info](./images/4.png?raw=true)

Like expected, info's been changed.

4. `man` and 'info' commands are used for getting a documentation for any command. It shows what does the command do, how it can be used, with which keys and values etc, that is a full information about the command. The main difference betwen them is `info` has a simpler markup language to use and basic hyperlink system, so you can follow links all over the manual. 
I've tried `man` and `info` with `w` command (step 1.5):

![checking 'man w' command](./images/5.png?raw=true)
![checking 'info w' command](./images/6.png?raw=true)

As shown below these results are identical, just have a difference in hyperlink's part. Btw command `w` has some keys to use: 
- -h or --no-header - shows user informations table without the header row:

![checking 'w -h' command](./images/7.png?raw=true)

- -s or --short - shows user informations table in short format: without login time, JCPU and PCPU times:

![checking 'w -s' command](./images/8.png?raw=true)

I've also tried `man` and `info` commands with all commands I used before. 

5. I learned that `more` command's used for paging through text file, page by page. It's like a document viewe but in the terminal (step 1.6). 
`less` command is more different. It has a sheer number of features like partial loading file (files load the way more faster than while using more or vi) and more advanced control. 
Here's an example of reading .bash with `more` command:

![reading .bash with 'more' command](./images/9.png?raw=true)

and with `less` command:

![reading .bash with 'less' command](./images/10.png?raw=true)

6. I created a new .plan file and added my plan to it, then tested it out (step 1.7):

![adding a plan and testing it](./images/11.png?raw=true)

7. I've listed all my files in home directory using `ls -al` command (step 1.8): 

![listing the home directory](./images/12.png?raw=true)

- `.` and `..` - these are shortcuts that stands for "current directory" and "parent directory";
- `.bash_history` file contains all the history from an os installation or last history clear;
- `.bash_logout` file is used for running some scripts on system logout;
- `.bashrc` file executes every time user logs in; like `.bash_logout` it may serve for running scripts on this event;
- `.cache` directory's being used by system and custom apps so they can put a data there and really speed up a work with it;
- `.local` directory serves for programs which put user information there;
- `.plan` file is used for storing user information about plans;
- `.profile` is a start-up file that stores some pre-defined settings that are loaded when a shell program starts;
- `.ssh` directory is not default, it's created when user run ssh commands and contains a data for it;
- `.sudo_as_admin_successful` file serves like a flag that checks if it's the first time for user being sudo;
- `shared` directory enables all users to have common access to itself;
- `learning` directory has been created by me for testing purposes.

I used keys 'a' for displaying all hidden files and special shortcuts (like '..') and 'l' for showing output in table view with additional information about each file. 


### Part 2

1. I examined the `tree` command. It can be used for listing files in current or specified directory. And it has a bunch of key-options to expand the functionality. According to step 2.1 I listed all files that contain a 'c' character in the title:

![listing all files that contain a 'c' character in the title](./images/13.png?raw=true)

And all files that start with a digit:

![listing all files that start with a digit](./images/14.png?raw=true)

Then I listed subdirs of the root dir that include only second nested level:

![command to list subdirs of the root dir](./images/15.png?raw=true)
![listing subdirs of the root dir](./images/16.png?raw=true)

2. It's a `file` command. There's an example of it's using (step 2.2):

![getting a type of the ~/learning/test.txt file](./images/17.png?raw=true)

3. There are some commands that help navigating the file system (step 2.3):
 - `ls` - uses to check a list of files in current or specific directory:
 ![`ls` command in action](./images/18.png?raw=true)

 - `cd` - uses to change a directory to another:
 ![`cd` command in action](./images/19.png?raw=true)

Home directory can be reached from anywhere by using the `cd ~` command:

![reaching the home directory](./images/20.png?raw=true)

The difference between relative and absolute paths is that relative paths can be reached only in within current directory, unlike absolute path that can be reached from anywhere. 

4. I examined the `ls` command and tested many options. There are some of them (step 2.4):
 - `ls -a` prints all files: whether it's hidden, specific shortcuts or general files:
 ![`ls -a` command in action](./images/21.png?raw=true)

 - `ls -d` prints current directory itself, not it's content:
 ![`ls -d` command in action](./images/22.png?raw=true)

 - `ls -l` prints content with additional information:
 ![`ls -l` command in action](./images/23.png?raw=true)
 There are the permission information, the number of links to that file, owner and group information, file size in bytes, last modified time and file or directory name information.

 - `ls -s` prints files and directories with their size. If use it with `-h` option it becomes more readable:
 ![`ls -s` and `ls -sh` commands in action](./images/24.png?raw=true)

 - `ls -1` prints content in column:
 ![`ls -1` command in action](./images/25.png?raw=true)

5. I created a 'subdir' subdirectory in my 'home' directory and a 'root_info.txt' file. I wrote all information about root's content to that file (step 2.5):

![creating a subdir and a text file inside it, writing information about root's content in it](./images/26.png?raw=true)

I opened the file:

![checking the 'root_info.txt' file's content](./images/27.png?raw=true)

I copied the file to the home dir using relative and absolute imports:

![copying the file to the home dir using relative and absolute imports](./images/28.png?raw=true)

Then I removed the subdirectory and two 'root_info*.txt' files from the home dir:

![removing the subdirectory and two 'root_info*.txt' files from the home dir](./images/29.png?raw=true)

6. I created a 'test' subdir in the 'home' dir and copied the .bash_history file in it, but changed it's name to 'labwork2' (step 2.6):

![creating a subdirectory and copying the .bash_history file in it with changing it's name](./images/30.png?raw=true)

Then I created a hardlink and a softlink to that file:

![creating a hardlink and a softlink to the file](./images/31.png?raw=true)

**Hardlink** it's a file that points on the hard drive where file data is stored. It means that when I change the data, it changes in all hardlink files. When I remove the file, hardlink will remain available and fully managable. 
**Softlink** it's a pointer to file. It only points to file name, so if the file's removed, the link is rendered useless.

I opened in vi a softlink file and put "data's changed" text at the start. Then I looked to the origin 'labwork2' file:

![changing data througt softlink](./images/32.png?raw=true)

The data is changed because if I open a softlink it point to the origin file so it's like I'm editing it.
I renamed the hardlink and the softlink according to the current step:

![renaming the hardlink and the softlink](./images/33.png?raw=true)

Then I deleted the 'labwork2' file:

![removing the 'labwork2' file](./images/34.png?raw=true)

The hardlink is still breathing and working well, but the softlink lost it's connection to the origin file. Like I wrote above that's because a softlink points to filename, but a hardlink, on the contrary, points to the specific space on the hard drive where file data is stored. 

7. To use locate utility I've installed the 'plocate' lib and updated a database via `sudo updatedb` command.
Just as described in step 2.7 I've searched in the filesystem by 'squid' and 'traceroute' sequences in filename:

![finding files with 'squid' and 'traceroute' sequences in filename](./images/35.png?raw=true)

8. There are several ways to check on system mounts (step 2.8):
 - by using the `cat /proc/mounts` command: 
 ![`cat /proc/mounts` command in action](./images/36.png?raw=true)
 
 - by using the `mount` command:
 ![`mount` command in action](./images/37.png?raw=true)
 
 - by using the `df -aTh`
 ![`df -aTh` command in action](./images/38.png?raw=true)
 
 - by using the `findmnt` command:
 ![`findmnt` command in action](./images/39.png?raw=true)

9. I filled in the 'learning/test.txt' file with some rows and searched with `grep` command by 'there' sequence in it (step 2.9):

![filling in the 'learning/test.txt' file and finding rows that maches 'there' sequence in it](./images/40.png?raw=true)

10. Using the `find` command I found all files in the '/etc/' dir that contain 'host' sequence (step 2.10):

![finding all files in the '/etc/' dir that contain 'host' sequence](./images/41.png?raw=true)

And files that contain 'ss' sequence by using `find` command (step 2.11):

![finding all files in the '/etc/' dir that contain 'ss' sequence by using `find` command](./images/42.png?raw=true)
![finding all files in the '/etc/' dir that contain 'ss' sequence by using `find` command](./images/43.png?raw=true)

I didn't find the way to search it by using only `grep` command, but with the `tree` command:

![finding all files in the '/etc/' dir that contain 'ss' sequence by using `tree` and `grep` commands](./images/44.png?raw=true)
![finding all files in the '/etc/' dir that contain 'ss' sequence by using `tree` and `grep` commands](./images/45.png?raw=true)

11. I wrote '/etc/' dir's content to a '~/etc_content.txt' file using stream redirection operation (step 2.12):

![writing '/etc/' dir's content to a '~/etc_content.txt' file using stream redirection operation](./images/46.png?raw=true)

Then I red it screen by screen using `more` command:

![reading the '~/etc_content.txt' file screen by screen using `more` command](./images/47.png?raw=true)
![reading the '~/etc_content.txt' file screen by screen using `more` command](./images/48.png?raw=true)

12. Devices are interfaces to actual drivers. I listed all devices by using `ls -l /dev` command(step 2.13):

![listing all devices](./images/49.png?raw=true)

There are four types of devices: **character device**(c), **block device**(b), **pipe device**(p) and **socket device**(s).

13. To determine the type of file I can use the `file <filename>` command. Linux has several types of files (step 2.14):
 - regular files
 - directory files
 - character special files
 - link files
 - socket files
 - named pipe files
 
14. I listed first 5 files from '/etc/' dir that were recently modified (step 2.15):

![listing first 5 files from '/etc/' dir that were recently modified](./images/50.png?raw=true)

