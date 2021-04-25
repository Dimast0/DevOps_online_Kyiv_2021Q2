## Task 5.3
**Dmytro Steblyna**

## PART 1

## 1. How many states could have a process in Linux? 
**A Linux process has 5 states:**
- created;
- ready;
- waiting; 
- running;
- terminated. 

## 2. Examine the pstree command. Make output (highlight) the chain (ancestors) of the current process. 
```pstree``` shows running processes as a tree. 
<p><img src="screenshots/1.png"/></p>

## 3. What is a proc file system? 
**From RedHat Documentation:**
Under Linux, all data are stored as files. We are familiar with the two primary types of files: text and binary. But the /proc/ directory contains another type of file called a virtual file. It is for this reason that /proc/ is often referred to as a virtual file system.

These virtual files have unique qualities. Most of them are listed as zero bytes in size and yet when one is viewed, it can contain a large amount of information. In addition, most of the time and date settings on virtual files reflect the current time and date, indicative of the fact they are constantly updated.
Virtual files such as /proc/interrupts, /proc/meminfo, /proc/mounts, and /proc/partitions provide an up-to-the-moment glimpse of the system's hardware. Others, like the /proc/filesystems file and the /proc/sys/ directory provide system configuration information and interfaces.

For organizational purposes, files containing information on a similar topic are grouped into virtual directories and sub-directories. For instance, /proc/ide/ contains information for all physical IDE devices. Likewise, process directories contain information about each running process on the system.

## 4. Print information about the processor (its type, supported technologies, etc.). 
To view information about the processor, we can take a look at the cpuinfo file in the proc directory.
<p><img src="screenshots/2.png"/></p>

## 5. Use the ps command to get information about the process. The information should be as follows: the owner of the process, the arguments with which the process was launched for execution, the group owner of this process, etc. 
<p><img src="screenshots/3.png"/></p>

## 6. How to define kernel processes and user processes? 
A kernel processes always run in kernel mode and use kernel space only, when user processes have their own address space.

## 7. Print the list of processes to the terminal. Briefly describe the statuses of the processes. What condition are they in, or can they be arriving in? 
R (running), S (interruptible sleep (waiting for an event to complete)), D (uninterruptible sleep (waiting for I/O)), T (stopped), Z (zombie), X (dead).
<p><img src="screenshots/4.png"/></p>

## 8. Display only the processes of a specific user. 
<p><img src="screenshots/5.png"/></p>

## 9. What utilities can be used to analyze existing running tasks (by analyzing the help for the ps command)? 
We can use ```top```, ```htop```, ```pstree```.

## 10. What information does top command display?
```top``` displays Linux processes. The command provides a dynamic real-time view of a running system.  It can display system summary information as well as a list of processes or threads currently being managed by the Linux kernel.  

## 11. Display the processes of the specific user using the top command. 
```top -U username```

<p><img src="screenshots/6.png"/></p>

## 12. What interactive commands can be used to control the top command? Give a couple of examples. 
**For example, can use:**
- Shift+N to sort by PID;
- Shift+P to sort by CPU usage;
- Shift+M to sort by Memory usage;
- Shift+T to sort by Time usage;
- Shift+Z to change colors;
- C to display absolute path of command;

## 13. Sort the contents of the processes window using various parameters (for example, the amount of processor time taken up, etc.) 
**Processes sorted by the processor time usage and tthe memory usage.**

<p><img src="screenshots/7.png"/></p>

## 14. Concept of priority, what commands are used to set priority? 
**All the processes in Linux are started with a specific priority. By default, all regular processes are started with the priority equal to 20. You can change the priority using the nice and renice commands.**

-	nice if you want to start a process with an adjusted priority. 
-	renice to change the priority for a currently active process. 

When using nice or renice, we can select from priority values ranging from -20 to 19. The default niceness of a process is set to 0 (which results in the priority value of 20). By applying a negative niceness, you increase the priority. Use a positive niceness to decrease the priority. It is a good idea to use increments of 5 and see how it gradually affects the application.

## 15. Can I change the priority of a process using the top command? If so, how? 
**We can start top utility and press r. Then we will be able to enter PID and change its niceness.**

<p><img src="screenshots/8.png"/></p>

## 16. Examine the kill command. How to send with the kill command process control signal? Give an example of commonly used signals. 
**The ```kill``` command is used to send a signal to a process. The most common use is when we need to stop a process. To do this, we can use: kill PID command. The command sends the SIGTERM signal to the process, which normally causes the process to stop its activity.**

Sometimes the kill command does not work because the process we want to kill is busy. In that case, we can use ```kill -9 PID``` to send the SIGKILL signal to the process. The SIGKILL signal cannot be ignored, so it forces the process to stop, but we also risk losing data while using this command. 

**Some of the most common signals:**
- SIGTERM (15) to ask a process to stop.
- SIGKILL (9) to force a process to stop.
- The SIGHUP (1) to hang up a process resulting in rereading the configuration files of the process. This signal is useful after making modifications to a process configuration file.

## 17. Commands jobs, fg, bg, nohup. What are they for? Use the sleep, yes command to demonstrate the process control mechanism with fg, bg. 
- ```jobs``` lists the active jobs.
- ```fg``` moves a job to the foreground.
- ```bg``` moves a job to the background.
- ```nohup``` allows jobs to continue after logout. We can stop nohup process using ```kill```.

<p><img src="screenshots/9.png"/></p>
<p><img src="screenshots/10.png"/></p>

## PART 2

## 1. Check the implementability of the most frequently used OPENSSH commands in the MS Windows operating system. (Description of the expected result of the commands + screenshots: command – result should be presented) 
```ssh user@host``` and ```ssh-keygen``` commands work but ```ssh-copy-id user@host``` command doesn’t work in Windows.

<p><img src="screenshots/111.png"/></p>
<p><img src="screenshots/112.png"/></p>
<p><img src="screenshots/113.png"/></p>

## 2. Implement basic SSH settings to increase the security of the client-server connection (at least 

<p><img src="screenshots/12.png"/></p>
<p><img src="screenshots/13.png"/></p>
<p><img src="screenshots/14.png"/></p>

## 3. List the options for choosing keys for encryption in SSH. Implement 3 of them. 
**SSH supports several public key algorithms for authentication keys.**
- rsa - an old algorithm based on the difficulty of factoring large numbers. A recommended key size of at least is 2048 bits; 4096 bits is better. 
- dsa - an old US government Digital Signature Algorithm. It is based on the difficulty of computing discrete logarithms. A key size of 1024 would normally be used with it. DSA in its original form is no longer recommended.
- ecdsa - a new Digital Signature Algorithm standarized by the US government, using elliptic curves. Only three key sizes are supported: 256, 384, and 521 bits. Recommended using it with 521 bits, since the keys are still small. 
- ed25519 - a new algorithm added in OpenSSH. Support for it in clients is not yet universal. 

<p><img src="screenshots/16.png"/></p>

**We can select the algorithm using the -t option and key size using the -b option. For example:**
- ```ssh-keygen -t rsa -b 4096 ```
- ```ssh-keygen -t dsa ```
- ```ssh-keygen -t ecdsa -b 521 ```
- ```ssh-keygen -t ed25519```

## 4. Implement port forwarding for the SSH client from the host machine to the guest Linux virtual machine behind NAT.
<p><img src="screenshots/15.png"/></p>

## 5*. Intercept (capture) traffic (tcpdump, wireshark) while authorizing the remote client on the server using ssh, telnet, rlogin. Analyze the result.

finishing...
