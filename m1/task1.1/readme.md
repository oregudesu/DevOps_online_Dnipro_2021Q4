# **Task 1.1** - Working with git and github 

1. According to first step, git is need to be installed on my workstation. I've already done that, so I can skip it.
1. I set up git's global configs, such as name, email and core text editor: 

![screen from terminal where I'm setting up git configs](/images/2.0.png)
![screen from terminal where I'm setting up git configs](/images/2.1.png)

So, I checked it out:
 ![screen from terminal where I'm checking out git configs](/images/2.2.png)
 
1. I created a new git account and a new private repo and called it according to step 4: DevOps_online_Dnipro_2021Q4.
1. In that step I cloned the repo to my workstation via ssh. Before that I generated two ssh keys - private and public: 

![screen from terminal where I'm generation ssh keys](/images/6.0.png)

and copied the public one to my github profile settings. On my workstation I moved them to a new created key folder:

![screen from terminal where I'm moving ssh keys to key folder](/images/6.1.png)

Then I ran the ssh-agent and created a new ssh-identity:

![screen from terminal where I'm running the ssh-agent and ssh-identity](/images/6.2.png)

After that I could finnaly clone my repo to local machine:
 
![screen from terminal where I'm clonning my repo](/images/6.3.png)
 
1. I created a directory structure inside the local repo according to step 5:

![screen from terminal where I'm creating new directories in the local repo](/images/8.png)

1. Then I created an empty readme.txt file in the task1.1 dir (steps 8-9):

![screen from terminal where I'm creating readme.txt file](/images/9.png)

1. Init commit (step 10):

![screen from terminal where I'm making an init commit](/images/10.png)

1. I created and checked out on develop branch (step 11):

![screen from terminal where I'm creating and checking out on develop branch](/images/11.png)

1. I created an empty index.html file and commited (step 12). The process is the same as in step before, so there's no screen.
1. I created and checked out on images branch. I downloaded two images and moved 'em to the images folder and commited all changes (step 13):

![screen from terminal where I'm creating and checking out on images branch and commiting changes](/images/13.png)

1. Then I started editing index.html file with vi editor (I've never used it before, so decided to learn) (step 14):

![screen from terminal where I'm starting to edit the index.html file](/images/14.0.png)
![screen from terminal where I'm editing index.html file](/images/14.1.png)

I added doctype and img tags to the index.html, saved it and commited my changes.

1. I went back to develop branch. Then I created and checked out on styles branch, created styles.css file inside of styles folder and edited it with the vi editor. I commited all changes. This process is similar to making and filling images branch (step 16).
1. Then I changed my index.html file with vi editor again (step 17):

![screen from terminal where I'm editing index.html file](/images/17.png)

1. After that I checked out back on develop branch and merged images branch to it (steps 18-19):

![screen from terminal where I'm merging images branch to develop](/images/19.0.png)

This merge went good. Then I merged styles branch to develop:

![screen from terminal where I'm merging styles branch to develop](/images/19.1.png)

But this one failed with a conflict. I found a confilct file with **git diff** command and changed it:

![screen from terminal where I'm starting to edit index.html file to resolve merge conflict](/images/19.2.png) ![screen from terminal where I'm editing index.html file](/images/19.3.png)

I resolved this merge conflict and commited to local repo.

1. Then I checked out on master branch and merged develop to it (step 21):

![screen from terminal where I'm merging develop branch to master](/images/21.png)

1. In the step 22 I've been playing around with git log command:

![screen from terminal where I'm playing with git log command](/images/22.0.png)
![screen from terminal where I'm playing with git log command](/images/22.1.png)
![screen from terminal where I'm playing with git log command](/images/22.2.png)
![screen from terminal where I'm playing with git log command](/images/22.3.png)
![screen from terminal where I'm playing with git log command](/images/22.4.png)
![screen from terminal where I'm playing with git log command](/images/22.5.png)
![screen from terminal where I'm playing with git log command](/images/22.6.png)
![screen from terminal where I'm playing with git log command](/images/22.7.png)
![screen from terminal where I'm playing with git log command](/images/22.8.png)

1. I pushed all my changes from previous steps to remote repo (step 23):

![screen from terminal where I'm pushing all my changes to remote](/images/23.png)

1. I wrote result from git reflog command to the task1.1_GIT.txt file according to 24 step:

![screen from terminal where I'm writing git reflog's result to the task1.1_GIT.txt file](/images/24.png)

And moved it to task1.1 folder (step 25):
 
![screen from terminal where I'm moving task1.1_GIT.txt file to task1.1 folder](/images/25.png)

1. I created the readme.md file and started editing it in the notepad++ editor (step 26):

![screen from terminal where I'm creating the readme.md file](/images/26.0.png)
![screen from terminal where I'm starting to edit the readme.md file](/images/26.1.png)

1. Devops is the bridge between software development and IT operations. I like the comparison from our mentor, he said that devops engineer is like a superhero in a team. That kind of specialist makes sure that everything's connected towards integration and delivery. (step 27)

And I leave some nekos below, 'cause I like them :)

![cat](/images/cat1.jpeg)
![cat](/images/cat2.png)
