# Module 2 Virtualisation and Cloud Basic
## Task 2.2

1. I've got acquainted with the terms of Using the AWS Free Tier and understood that (step 1): 
  - AWS Free Tier allows users to use free benefits of AWS services. Each service has it's unique limits. User can be charged for usage on a different basis: hourly, by the minite, by the requests etc;
  - AWS Free Tier is enabled for 12 months from first sign in to the AWS;
  - AWS has tracking system for check on tier status and control it's limits. It can send notifications with information to user. Also, AWS Budgets service notifies users by email when they exceed 85% of AWS Free Tier;

2. I've already got an registered account in AWS (step 2).

3. According to step 4, I've started reviewing example "Launch a Linux VM with Amazon Lightsail". After initiating an instance creation, I picked an eu-central-1a (Frankfurt) region, 'cause it's the nearest region to me. Then I picked an instance image, blueprint - all according to the tutorial, - and added a simple shell-script that starts on the instance for the first time it's launched: 

![creating a shell script](./images/1.png?raw=true)

Then I downloaded already created private ssh-key for further connect to the instance, add key-only and key-value pair tags and initiated creating the linux2 vm:

![linux2 vm creating](./images/2.png?raw=true)

So, after successful creation I connected to my vm via ssh:

![successful connection to the vm](./images/3.png?raw=true)

Yeah, I'm in, it's so excited for me every time I do that!

4. For launch an instance with EC2 service I've been setting it up. First of all, I chose an CentOS AMI as was recommended in step 5:

![choosing the Centos ami from the AWS Marketplace](./images/4.png?raw=true)

Then I picked t2.micro tier with eligible free benefit:

![picking a free t2.micro tier](./images/5.png?raw=true)

After that I went throught next steps and created a key-value tag for the instance. I also created a new ssh-key pair for remote access via ssh and downloaded it. Then I launched the instance: 

![process of initiating instance launches](./images/6.png?raw=true)
![successfully created instance](./images/7.png?raw=true)

One more thing: I enabled Free Tier Usage alerts for notifying me by aws when the tier hits free borders:

![changing preferences for a free tier usage alert](./images/8.png?raw=true)

Then I sshed to the instance:

![connecting to the created instance to make sure it works](./images/9.png?raw=true)

It works just fine!

5. According to step 6 I need to create a snapshot with any new state of vm. So I created a readme_files dir and a readme.txt with a datetime in it:

![making some changes for creating a snapshot](./images/10.png?raw=true)

Then I went to "Elastic Block Store - Volumes" menu, selected my volume and in actions hitted a "Create snapshot" action, filled in the description and added tag:

![creating a snapshot](./images/11.png?raw=true)
![adding some info to snapshot's properties](./images/12.png?raw=true)

And here it is, in the "Snapshots" submenu:

![checking on successfully created snapshot](./images/13.png?raw=true)

6. I headed over "Elastic Block Store - Volumes" and created a new one with next params (step 7):

![creating a new volume](./images/14.png?raw=true)

And attached it to centos7_64_first vm. Then I formatted the volume to the ex4 filesystem:

![formatting the volume to the ex4 filesystem](./images/15.png?raw=true)

I created a new dir in the root and mounted the volume to that dir:

![creating a new directory in the root and mounting the volume to it](./images/16.png?raw=true)

Then I installed wget package with `sudo yum install`  and downloaded an image from internet, saved it to disk_d:

![downloading some picture from internet and saving it to the volume](./images/17.png?raw=true)

7. According to step 8 I need to launch the new instance from the snapshot I've made before. So, first of all I created an AMI from my snapshot:

![creating an image from the snapshot](./images/18.png?raw=true)

I left all params as default except that one:

![making changes in the image preferences](./images/19.png?raw=true)

Then I launched the instance from the new-created AMI:

![checking on successfully installed instance](./images/20.png?raw=true)

And connected to it for a check:

![connecting to the instance for making sure it works](./images/21.png?raw=true)

8. Before detaching the volume, I unmounted it in the Centos instance (step 9):

![unmounting the volume to detaching it from the vm](./images/22.png?raw=true)

Then I went to "Elastic Block Store - Volumes", detached the Disk_d volume from first instance and attached to second:

![detaching the volume from the vm](./images/23.png?raw=true)
![attaching the volume to another vm](./images/24.png?raw=true)

And checked for a file I downloaded to it:

![checking for a downloaded before file](./images/25.png?raw=true)

It's here.

9. I repeated the "Launch a Wordpress website" step-by-step tutorial. I connected to the newly created vm and get the password to my wordpress website admin panel (step 10):

![connecting to vm with WordPress after successful launching it and getting a password to the admin panel](./images/26.png?raw=true)

Then I connected to it using the public IP:

![successful connection to the admin panel via public IP](./images/27.png?raw=true)

And created the static IP:

![static IP's created](./images/28.png?raw=true)

And, finally, I created a DNS zone for that website:

![DNS region for the vm is created](./images/29.png?raw=true)

10. I reviewed and repeated the "S3 Store and Retrieve File" step-by-step tutorial, created my own bucket and uploaded a picture there (step 11):

![demonstrating the created s3 bucket and uploaded file in it](./images/30.png?raw=true)

11. I reviewed and repeated the "S3 Store and Retrieve File" step-by-step tutorial and have installed AWS CLI to my Ubuntu Linux (step 12):

![downloading and unzipping aws cli archive](./images/31.png?raw=true)
![installing aws cli](./images/32.png?raw=true)
![checking on aws cli version](./images/33.png?raw=true)

Then I've configured the aws cli for make it prepared for using:

![configurating aws cli](./images/34.png?raw=true)

So, cli's ready to use. I created a new s3 bucket:

![creating a new s3 bucket](./images/35.png?raw=true)

Then I dowloaded some image from Internet to the Downloads dir and uploaded it to my s3 bucket:

![uploading a picture to s3 bucket](./images/36.png?raw=true)

Let's check it out on the website:

![checking out for a job that's done](./images/37.png?raw=true)

Then I downloaded that picture to the Documents dir:

![downloading the picture from s3 bucket to the Documents dir](./images/38.png?raw=true)

And I removed this picture from the bucket:

![removing the picture from the bucket](./images/39.png?raw=true)

12. I reviewed and repeated the "Register a domain name" step-by-step tutorial, created new static IP address and associated it with a first Centos vm instance (step 13):

![a new static IP address associated with a first Centos vm instance](./images/40.png?raw=true)

I tried to connect to it:

![connection to the instance](./images/41.png?raw=true)

Works fine. 
For registering a new domain I'm gonna be charged according to billing plans for different domains. 

13. I reviewed and repeated the "Docker basics for Amazon ECS" step-by-step tutorial and have installed the Docker engine on my Linux via [the tutorial](https://docs.docker.com/engine/install/ubuntu/). I ran the hello-world example for verify proper installation:

![running the docker hello-world example](./images/42.png?raw=true)

So, in continue of the tutorial I need to create my own Docker image. Firstly I created a Dockerfile with a `touch Dockerfile` command and put the script from the tutorial inside it.
Then I ran the docker build command:

![running the docker build command](./images/43.png?raw=true)

And after building I had successfully builded image:

![successfully builded image](./images/44.png?raw=true)

And started it for a test:

![running my docker image](./images/45.png?raw=true)
![trying to connect to localhost for access the server from the image](./images/46.png?raw=true)

It works! The next thing I need to do is upload my image to the AWS ECR. For do that I created a repo in the ECR and saved output with the uri to the file:

![creating a repo int the ECR](./images/47.png?raw=true)

Then I tagged my image inside my Docker:

![tagging the image inside the Docker](./images/48.png?raw=true)

Logined in to the ECR fom CLI:

![loginning in to the ECR from CLI](./images/49.png?raw=true)

And pushed the image to it:

![pushing the image to ECR](./images/50.png?raw=true)

14. According to the last step (15) I need to create a public page with my photo, Amazon services list with which I worked and completed aws tutorials and labs. So, first of all I created a static page on my local workstation, then created a new S3 bucket, uploaded my site there. After that with Route53 service I bought the "oregu.link" domain for one year and added a record to my hosted zone to redirect to S3 website: 

![my s3 bucket for website hosting](./images/51.png?raw=true)
![record in my hosted zone for the oregu.link domain](./images/52.png?raw=true)

So, after all setting up it works:

![testing an access to my site via custom domain](./images/53.png?raw=true)