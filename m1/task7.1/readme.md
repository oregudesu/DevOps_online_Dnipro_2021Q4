# Module 7 Linux Administration with Bash

## Task 7.1

1. I created a script according to step 1 in the task. There are outputs in three cases of using this script:

- if I don't provide any options:

![running the first script with no options](./images/1.png?raw=true)

- if I provide "--all" option it gives me ip addresses with symbolic name for each of them in the current subnet:

![running the first script with --all option](./images/2.png?raw=true)

- if I provide "--target" option it gives me a list of open tcp ports:

![running the first script with --target option](./images/3.png?raw=true)


2. Second script outputs:

- if I provide no options:

![running the second script with no options](./images/4.png?raw=true)

- if I provide a directory instead of a file:

![running the second script with a directory provided](./images/5.png?raw=true)

- if I provide an apache_log file:

![running the second script with apache_log file provided](./images/6.png?raw=true)


3. Third script outputs:

- if I provide no options:

![running the third script with no options](./images/7.png?raw=true)

- if I provide only one option:

![running the third script with only option](./images/8.png?raw=true)

- if I provide files instead of directories:

![running the third script with two files provided](./images/9.png?raw=true)

- if I provide two directories:

![running the third script with two directories provided](./images/10.png?raw=true)

As you can see the script created a log file in `/var/log/` directory with a name of the script. Let's take a look at the log file:

![looking at the log file](./images/11.png?raw=true)

It says that 10.02.2022 at 18:50 the script added new file 'apache_logs.txt' to backup folder. Let's try to backup it one more time and take a look in the log file:

![looking at the log file after one more backup](./images/12.png?raw=true)

Now it says that it rewrote 'apache_logs.txt' file.

