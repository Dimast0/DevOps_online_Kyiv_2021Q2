# Task 5.1
**Dmytro Steblyna**

# Part 1

# 1-2 Log in to the system as root. Use the passwd command to change the password. Examine the basic parameters of the command. What system file does it change?

**The ```passwd``` command changes the "/etc/passwd" file that contains information about the users on the system.**
<p><img src="screenshots/1.png"/></p>



# 3) Determine the users registered in the system, as well as what commands they execute. What additional information can be gleaned from the command execution?

**We can use the ```w``` command:**
<p><img src="screenshots/2.png"/></p>

**The header displays the following fields:**
- current time,
- system uptime without rebooting (uptime),
- the number of users currently working,
- the average value of the system load for the last 1, 5 and 15 minutes (Load averages).

**The following fields are displayed in the table for each user:**
- USER is the username.
- TTY is the name of the terminal.
- FROM is the name of the remote computer or IP address.
- LOGIN is the time of logging into the system.
- IDLE - idle time.
- JCPU is the time used by all processes connected to the tty. It does not include completed background jobs, but it does include background jobs that are currently running.
- PCPU is the time used by the current process, which is specified in the WHAT field.
- WHAT is the current process (command line of the current process).


# 4) Change personal information about yourself.
**Let's use the ```usermod [options] username``` command to change some information about the user:**
<p><img src="screenshots/4.png"/></p>

**Options:**
- -c = We can add comment field for the useraccount.
- -d = To modify the directory for any existing user account.
- -e = Using this option we can make the account expiry in specific period.
- -g = Change the primary group for a User.
- -G = To add a supplementary groups.
- -a = To add anyone of the group to a secondary group.
- -l = To change the login name from tecmint to tecmint_admin.
- -L = To lock the user account. This will lock the password so we can’t use the account.
- -m = moving the contents of the home directory from existing home dir to new dir.
- -p = To Use un-encrypted password for the new password. (NOT Secured).
- -s = Create a Specified shell for new accounts.
- -u = Used to Assigned UID for the user account between 0 to 999.
- -U = To unlock the user accounts. This will remove the password lock and allow us to use the user account.

# 5)Become familiar with the Linux help system and the man and info commands. Get help on the previously discussed commands, define and describe any two keys for these commands. Give examples.
<p><img src="screenshots/5.png"/></p>


**We can use ```w -h -s``` to display the result of ```w``` command without the header and in short format:**

<p><img src="screenshots/10.png"/></p>

**We can use ```usermod username -c "Some comment/info"``` to change the comment field in the "/etc/passwd" file:**

<p><img src="screenshots/11.png"/></p>

# 6) Explore the more and less commands using the help system. View the contents of files .bash* using commands.

**```more``` is one of the oldest terminal pagers in the UNIX ecosystem. Originally, ```more``` could only scroll down, but now we can use it to scroll up one screen-full at a time, and scroll down either one line or one screen-full. On its status bar, ```more``` shows the percentage of the file read. It automatically closes when it reaches the end of the file without having to press a button.**

**```more``` has many interactive commands like:**
- space – to go to the next page in accordance with the terminal’s size
- b – to go back one page
- enter – to scroll down one line
- = – to display the current line number
- :v – to start up the vi text editor at the current line

**One of to the reasons why ```less``` was introduced was to allow backward movement line by line. It has a lot of commands that are similar to the vi text editor’s commands, and it - supports horizontal scrolling, live monitoring, and more.**

<p><img src="screenshots/6.png"/></p>

# 7) Describe in plans that you are working on laboratory work 1. Tip: You should read the documentation for the finger command.
<p><img src="screenshots/7.png"/></p>

# 8)List the contents of the home directory using the ls command, define its files and directories. Hint: Use the help system to familiarize yourself with the ls command.
<p><img src="screenshots/8.png"/></p>

# Part 2
# 1)Examine the tree command. Master the technique of applying a template, for example, display all files that contain a character c, or files that contain a specific sequence of characters. List subdirectories of the root directory up to and including the second nesting level.

**(Will finishing by the deadline)**
