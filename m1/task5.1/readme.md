# Module 5 Linux Essentials

## Task 5.1

### Part 1

1. I used Ubuntu Server as a workstation. So I logged in as root (step 1) and changed the password to a new one (step 2):

![changing the password for root user](./images/1.png?raw=true)

Changing a user password does change the 'passwd' system file that contains one line for each user. This file is in the /etc/ directory. Moreover there are two more files: 
- 'shadow' that contains encrypted passwords, user data and other password info (such as data of last password change, min and max password age, etc);
- 'passwd-' that contains backups for passwords from 'passwd' file.

2. I determined the users registered in this system, it's just root (me) (step 3):

![determining the users registered in this system](./images/2.png?raw=true)

By using `w` command you can get user name, the name of terminal in which user works, the remote host (if user's connected from outside through ssh for example), login, idle, JCPU and PCPU time and command that user are running now. `who` command gives us a sumplified information about users in the system: just user name, terminal and login time.

3. I added some personal info to my root account (step 4):

![adding personal info for root user](./images/3.png?raw=true)

And for check it out I installed the finger lib, then entered `finger` command:

![checking out user info](./images/4.png?raw=true)

Like expected, info's been changed.

4. `man` and 'info' commands are used for getting a documentation for any command. It shows what does the command do, how it can be used, with which keys and values etc, that is a full information about the command. The main difference betwen them is `info` has a simpler markup language to use and basic hyperlink system, so you can follow links all over the manual. 
I've tried `man` and `info` with `w` command (step 5):

![checking 'man w' command](./images/5.png?raw=true)
![checking 'info w' command](./images/6.png?raw=true)

As shown below these results are identical, just have a difference in hyperlink's part. Btw command `w` has some keys to use: 
- -h or --no-header - shows user informations table without the header row:

![checking 'w -h' command](./images/7.png?raw=true)

- -s or --short - shows user informations table in short format: without login time, JCPU and PCPU times:

![checking 'w -s' command](./images/8.png?raw=true)

I've also tried `man` and `info` commands with all commands I used before. 

5. I learned that `more` command's used for paging through text file, page by page. It's like a document viewe but in the terminal (step 6). 
`less` command is more different. It has a sheer number of features like partial loading file (files load the way more faster than while using more or vi) and more advanced control. 
Here's an example of reading .bash with `more` command:

![reading .bash with 'more' command](./images/9.png?raw=true)

and with `less` command:

![reading .bash with 'less' command](./images/10.png?raw=true)

6. I created a new .plan file and added my plan to it, then tested it out (step 7):

![adding a plan and testing it](./images/11.png?raw=true)

7. I've listed all my files in home directory using `ls -al` command (step 8): 

![list the home directory](./images/12.png?raw=true)

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

