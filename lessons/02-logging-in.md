Logging into a Cluster
======================
>*Learning Objectives*
>*    Student will be able to log on and off a Linux cluster using SSH from windows, mac or Linux based machines.
>*    Student will be able to use a GUI based file transfer system (something like cyberduck) to move files to and from the cluster.
>*    Student will be able to change their account password.
>*    Student will understand the importance of backing up files on their own machine.

Why Do We Have to Use a Terminal?
=================================
Wouldn’t it be easier if HPC systems had a graphical user interface (GUI) to navigate within your computer's contents with a mouse? While there is a steep learning curve associated with using a terminal, terminal-based computer systems are ideally suited for certain types of computing.

Imagine a research scientist who has data files containing the results of their research. For each run of the experiment, the scientist must make a change to each one of the files. If there are only 20 data files then clicking on each file to open it and change it, while time consuming, is doable. However, what does the scientist do for an experiment that has 200 runs, or even 2,000?

Unless they employ a lot of graduate students, our poor researcher will not be able to complete their research in a timely manner. The terminal has a nice set of features that allows us to automate such tasks so that the computer does the work for us, allowing us to complete repetitive tasks quickly and more accurately. Remember, while the terminal has a steep learning curve, it is an investment that pays itself back later by saving you time.

Logging In
==========
Since most supercomputers are Linux-based, command line systems, we need to use a tool called SSH. SSH stands for *S*ecure *SH*ell. It is a bash command that allows us securely connect to a remote computer. If you use a Mac or Linux based machine, you already have SSH installed on your computer. There is a little bit of extra setup required if using a windows computer.

Logging in from Windows
-----------------------
Putty is a free and open-source terminal emulator that supports network protocols such as SSH. First download Putty from [here](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html). Download 'putty.exe', save it to your desktop and then run it. When you start Putty, a window will open that looks like the image below.

![Putty Opening Screen](/img/putty.jpg "Putty") 

In the box labeled hostname, enter the name of the system you want to connect to: `cowboy.hpc.okstate.edu`. Make sure the Connection type is `SSH` and the Port number is `22`. In the Saved Sessions box, you can give a name for these login settings, i.e. Cowboy, then click save. The next time you open Putty, you can double click this saved session and it will open a terminal window that will be ready to log you into Cowboy. After clicking 'Open', you'll be prompted first to enter your Cowboy user name. Hit 'Enter' after you have typed your user name. Next you will be prompted to enter your password followed by 'Enter'.

>Your cursor will not move as you type. This is a safety feature of the bash shell. Don't worry, just type your password and hit 'Enter'.

If you entered your password correctly, you should get the command prompt. If it says something like permission denied or login invalid, you might have entered your password incorrectly. Remember passwords are case sensitive.

Logging in from a Mac
---------------------
 You will essentially follow the same instructions as for Linux, but you will need to find and open the terminal application first. 
* Double click on the hard drive.
* Double click on the Applications folder.
* Double click on your Utilities folder.
* Double click on the Terminal icon.

![Mac Terminal Icon](/img/terminalicon.jpg "Terminal Icon")

* Now that you are in a terminal window, follow the Linux instructions.

Logging in from Linux
---------------------
In a terminal type `ssh user_name@cowboy.hpc.okstate.edu`, where 'user_name' is your Cowboy user name. For Example, if your user name is 'pete', you would enter `ssh pete@cowboy.hpc.okstate.edu`. Next, you will be prompted to enter your password followed by 'Enter'. If you entered your password correctly, you should get the command prompt. If it says something like permission denied or login invalid, you might have entered your password incorrectly. Remember passwords are case sensitive.

>In many distributions of Linux, you can open the terminal by using the keyboard shortcut CTRL-ALT-T. If you are not sure how to open the terminal in your particular distribution, a quick Google search will often reveal the answer.

Transferring Files
==================
Now that we can log into a supercomputer, we need to be able to move our project files back and forth from our personal computer and our account on the supercomputer. There are several applications that will allow us to do this.

Cyberduck
---------
 You can download Cyberduck [here](https://cyberduck.io/ "Cyberduck Download"). Make sure to click the "Download" icons below the duck -- the "Start Download" icon to the right of the duck is an ad. After downloading and opening the application, you should have a window that looks like this (on a Mac):

![Cyberduck Opening Screen](/img/cyberduck.jpg "Cyberduck")

Click on the 'Open Connection' icon at the top left. In the pop up window, you will edit the following:
* Choose the 'SFTP (SSH File Transfer Protocol)' option in the drop down menu at the top.
* Set 'Server' to: `cowboy.hpc.okstate.edu`.
* Change 'Port' to: `22`.
* Enter your Cowboy user name and password.
* Click 'Connect'.
After connecting, your Cyberduck window should now look like the window below, listing the contents of your home directory on Cowboy:

![Cyberduck File Screen](/img/cyberduckfiles.jpg "Cyberduck Files")

From here you can click on and navigate your directories and files in your home directory on Cowboy. To move a file from Cowboy to your local machine, you can drag and drop the file onto your Desktop or right-click the file or directory to download it onto your local machine. To move a file from your local machine to Cowboy, navigate inside of Cyberduck to the Cowboy directory you want and then drag and drop the file from your local machine into the window. You can also choose the 'Action' drop down menu at the top of the Cyberduck window and choose the 'Upload' option.

>If you are using Linux or a Mac, you can also transfer files using the command line. To copy a file from Cowboy to your local machine open a terminal on your local machine and type `scp yourusername@cowboy.hpc.okstate.edu:/directory/yourfilename .` Be sure to include a space and a period in the command.
>To copy a file from your local machine to Cowboy, open a terminal on your local machine, navigate to the directory where your file is located and type the following command: `scp yourfilename yourusername@cowboy.hpc.okstate.edu:/directory/path/`.

>If you are using a public computer with Windows and do not have priviledges that allow you install new software, you can use [WinSCP](http://winscp.net/eng/download.php). Download the 'Portable Executable' version. Save the excutable to your desktop and double click the file to start the program. You should see the following screen:
>
>![WinSCP Screen](/img/WinSCP.JPG "WinSCP")
>
>In the `hostname` box enter the hostname of the hpc system you wish to use: `cowboy.hpc.okstate.edu`. In the `username` box enter your username (or leave it blank and it will prompt you for it later). Press enter and it will begin connecting. When Using WinSCP you should be greeted with a window similar to the one below. **NOTE:** On the left is your local disk and on the right is your home directory on the hpc system. From here you can drag and drop to copy files in either direction. You may be asked to confirm that you want to copy files.
>
>![WinSCP File Screen](/img/winscpfiles.JPG "WinSCP Files")

Other Options
-------------
Cyberduck is one of many options available for transferring files. To see others, you can check out the OSU HPCC site [here](https://hpcc.okstate.edu/content/uploading-and-downloading-files-0).

Pete's Tweets
=============

After receiving an account from HPCC staff, Pete logs into Cowboy for the first time. He opens up a terminal and uses SSH.

```bash
ssh pete@cowboy.hpc.okstate.edu
```
   
```bash
pete@cowboy.hpc.okstate.edu's password: 
```

He enters his password and is greeted by the welcome screen.

```bash
Last login: Fri May 27 14:31:05 2016 from 123.45.678.901
Welcome to Cowboy!  

Please see the HPC Website for helpful usage information:
   hpcc.okstate.edu


Cowboy is funded by NSF MRI award OCI-1126330.  For acknowledgment
instructions see the Website.

Please report all grants and publications facilitated by usage to 
dana.brunson@okstate.edu

Please direct all other questions, comments and support requests
to hpcc@okstate.edu

NOTE:

ALL applications must be run through the scheduler.



Quota information:
You have used 0.0 GB of your allocated 25 GB in /home/pete.
```

Since this is his first time, Pete realizes that it is a good practice to change the default password given to him by HPCC staff to one that is more secure and easy for him to remember.

```bash
passwd
```

```bash
Changing password for user pete.
Current Password:
```

Pete enters his current password and then enters the new password twice. From now on, he will use this password to log into Cowboy. Pete begins by looking around. He first wants to know where he is on Cowboy. He does this by using the command `pwd`.

```bash
pwd
```

He sees that he is in his home directory.

```bash
/home/pete
```

Next, Pete wants to know what files he has in his home directory. He can do this using the list command.

```bash
ls
```

There is no output since his home directory is empty. Pete needs to move his twitter data to Cowboy so that he can begin working on his project. He does this by moving the hpc-novice directory to his home directory on cowboy using Cyberduck. Now when he checks to see what files are in his home directory, he sees that the hpc-novice files are now in his home folder.

```bash
ls
```

```bash
hpc-novice
```

He can move into the project directory by using the change directory command.

```bash
cd hpc-novice
ls
```

```bash
twitter-data
```

Now Pete is ready to begin working with his data. He moves back to his home directory.

```bash
cd
```

>For more information on shell commands, see the [Software Carpentry Shell Lesson](http://swcarpentry.github.io/shell-novice/ "The Unix Shell").
