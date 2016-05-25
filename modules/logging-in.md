Logging into a Cluster
======================
*Learning Objectives*
*    Student will be able to log on and off a Linux cluster using ssh from windows, mac or linux based machines.
*    Student will be able to use a gui based file transfer system (something like cyberduck) to move files to and from the cluster.
*    Student will understand best practices in security for users of a remote system.
*    Student will be able to change their account password.
*    Student will understand best practices in file and data management (backing up files on your own machine).

Why Do We Have to Use a Terminal?
=================================
Wouldn’t it be easier if HPC systems had a graphical user interface (GUI) to navigate within your computer's contents with a mouse? While there is a steep learning curve associated with using a terminal, terminal-based computer systems are ideally suited for certain types of computing.

Imagine a research scientist who has data files containing the results of their research. For each run of the experiment, the scientist must make a change to each one of the files. If there are only 20 data files then clicking on each file to open it and change it, while time consuming, is doable. However, what does the scientist do for an experiment that has 200 runs, or even 2,000?

Unless they employ a lot of graduate students, our poor researcher will not be able to complete their research in a timely manner. The terminal has a nice set of features that allows us to automate such tasks so that the computer does the work for us. Remember, while the terminal has a steep learning curve, it is an investment that pays itself back later by saving you time.

Logging In
==========
Since most supercomputers are linux-based, command line systems, we need to use a tool called ssh. ssh stands for *S*ecure *Sh*ell. It is a bash command that allows us securely connect to a remote computer. If you use a Mac or Linux based machine, you already have ssh installed on your computer. There is a little bit of extra setup required if using a windows computer.

Logging in from Windows
-----------------------
Putty is a free and open-source terminal emulator that supports network protocols such as ssh. First download Putty from [here](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html) Download 'putty.exe', save it to your desktop and then run it.
Start Putty. A window will open that looks like the image below.
   
In the box labelled hostname, enter the name of the system you want to connect to: cowboy.hpc.okstate.edu
Make sure the Connection type is SSH and the Port number is 22.
In the Saved Sessions box, you can give a name for these login settings, i.e. Cowboy. Click save.
The next time you open Putty, you can double click this saved session and it will open a terminal window that will be ready to log you into Cowboy.
After clicking 'Open', you'll be prompted first to enter your Cowboy username. Hit 'Enter' after you've typed your username.
Next you'll be prompted to enter your password followed by 'Enter'.
(**NOTE** your password will not show up on the screen as you type)
If you entered your password correctly, you should get the command prompt.
​If it says something like permission denied or login invalid, you might have entered your password incorrectly. Remember passwords are case sensitive.
If everything has worked according to these instructions, you are ready to continue the tutorial.

