# Report task 2.2

**Dmytro Steblyna**

## Firstly, I registered an AWS Free Tier account. Then I started an Amazon Linux VM with Amazon Lightsail and connected to it.
<p><img src="screenshots/1.png" width="800"/></p>

## Launched another Linux VM without Amazon Lightsail. I used an instance of t2.micro and an Amazon Linux 2.0 operating system.
<p><img src="screenshots/2.png" width="800"/></p>
<p><img src="screenshots/3.png" width="800"/></p>

## Then I created a snapshot of the EC2 VM.
<p><img src="screenshots/4.png" width="800"/></p>


## Created and attached a Disk_D (EBS) to the instance to add more storage space. 
<p><img src="screenshots/5.png" width="800"/></p>
<p><img src="screenshots/6.png" width="800"/></p>
<p><img src="screenshots/7.png" width="800"/></p>


**I used the following commands to initially connect the disk to the system.**
<p><img src="screenshots/8.png" width="800"/></p>

## Created and saved some file on Disk_D
<p><img src="screenshots/9.png" width="800"/></p>

## Created an image from the snapshot and launched a new instance
<p><img src="screenshots/10.png" width="800"/></p>
<p><img src="screenshots/11.png" width="800"/></p>
<p><img src="screenshots/12.png" width="800"/></p>

## Detached Disk_D from the instance and attached it to the new instance (created from the snapshot)
<p><img src="screenshots/13.png" width="800"/></p>
<p><img src="screenshots/14.png" width="800"/></p>
<p><img src="screenshots/15.png" width="800"/></p>
<p><img src="screenshots/16.png" width="800"/></p>

## Launched and configured a WordPress instance with Amazon Lightsail
<p><img src="screenshots/17.png" width="800"/></p>
<p><img src="screenshots/18.png" width="800"/></p>


## Created a S3 Bucket, stored and retrieved some file.
<p><img src="screenshots/19.png" width="800"/></p>
<p><img src="screenshots/20.png" width="800"/></p>
<p><img src="screenshots/21.png" width="800"/></p>

## Created a user AWS IAM, configured CLI AWS and uploaded a file to S3. 
<p><img src="screenshots/22.png" width="800"/></p>
<p><img src="screenshots/23.png" width="800"/></p>
<p><img src="screenshots/24.png" width="800"/></p>
<p><img src="screenshots/25.png" width="800"/></p>

##  Elastic Container Service
**I created a container (based on the demo application), a cluster, and a service. And then started the application. Also, updated the task several times.**

<p><img src="screenshots/38.png" width="800"/></p>
<p><img src="screenshots/39.png" width="800"/></p>
<p><img src="screenshots/40.png" width="800"/></p>
___

## Then I created the S3 static web-page: 
http://dmytro-steblyna.ml.s3-website.eu-central-1.amazonaws.com

<p><img src="screenshots/26.png" width="800"/></p>
<p><img src="screenshots/37.png" width="800"/></p>

## Also I created a Hosted zone and connected my domain using Route 53 and checked for availability:

<p><img src="screenshots/34.png" width="800"/></p>
<p><img src="screenshots/35.png" width="800"/></p>

**Then I deleted the Hosted zone to avoid unexpected expenses.**

<p><img src="screenshots/36.png" width="800"/></p>
