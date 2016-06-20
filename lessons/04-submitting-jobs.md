Submitting Jobs (one possibility is to have several versions of this module for common schedulers)
====================================================================================
>*Learning Objectives*
>*    Student will be able to demonstrate understanding of what a scheduler is and why it is important.
>*    Student will be introduced to some of the common schedulers in use on different clusters and will understand that they each have their own syntax.
>*    Student will be able to complete the following tasks using `sub` and a pre-made submit script: submit a job, check on the status of a job, cancel a job, check the output once a job has been completed.

On Cowboy (or any HPC cluster) you won't run your job on the login node. You can edit files here, but when it's time to run a job, you will need to use the batch scheduler command to move you to a compute node. The job scheduler takes some information from you, finds the best compute node(s) to use and runs your job there.

![Cowboy Network](/img/cowboynetwork.png "Cowboy Network")
 
*ALL JOBS AND SCRIPTS SHOULD BE RUN THROUGH THE SCHEDULER*. If we run our jobs on a login node it will slow down and other users will not be able to log into Cowboy. Cowboy is a shared resource with many users all competing for compute time and the only fair way to split compute time between different users is to use the scheduler. The scheduler is also how our jobs gain access to Cowboy’s compute nodes.

The most efficient way to use Cowboy is as follows: 
* Login
* Set up jobs with submit scripts
* Submit them 
* Log out. 
* Have the scheduler email you when your jobs are finished.

>While almost every HPC cluster uses a scheduler to manage different jobs from different users, there are many, *many* different types of schedulers in use. Check with your local HPC staff to see what scheduler they use. They should be able to get you resources about what commands to use for that particular scheduler. Different schedulers emphasize different features, but all schedulers are tasked with the job of determining the most equitable and efficient way of running multiple jobs from multiple users on the cluster. They do this by queuing jobs and determining which jobs are assigned to which nodes. For the purposes of this lesson, we will use Cowboy's scheduler [qsub](http://docs.adaptivecomputing.com/torque/4-0-2/Content/topics/commands/qsub.htm).

In order to use a scheduler, we must use a submit script. A submit script is a special [bash script](http://swcarpentry.github.io/shell-novice/ "Software-Carpentry Bash Lessons") that tells the scheduler what to do. Essentially, we type the commands that run our job into a text file and give that file to the scheduler. Then, when it is our job's turn in line, the scheduler will look inside the file and execute whatever commands we have put inside.

Let's look at Pete's submission script.

```bash
cd
cd hpc-novice/twitter-data
ls
```

```bash
parse_tweets.py  raw-tweets.csv  twitter-submit-script.pbs
```

```bash
cat twitter-submit-script.pbs
```

```bash
#! /bin/bash
#PBS -q batch 
#PBS -l nodes=1:ppn=1,walltime=10:00
#PBS -j oe

cd $PBS_O_WORKDIR

module load python

echo "Began parsing tweets..."

python parse_tweets.py raw-tweets.csv parsed-tweets.csv 

echo "Tweets parsed successfully. Have a good day."
```

Let's look at what each part of the script means. First, note that ‘#’ is a comment marker in scripts. Anything typed after the ‘#’ character is ignored by the computer. That is so humans can write notes in their files. This script is a little bit special. Since it is for Cowboy's batch scheduler, qsub, there are a few comment lines that are followed by PBS. These are special commands just for qsub, not for bash. Let’s look at them:

```bash
#PBS -q batch
```

This tells qsub which queue to put your job in. Cowboy has four queues:

batch: The ‘batch’ queue is the default queue. The wall time limit is 120 hours (120:00:00). If your job needs to run longer than this and your software does not have checkpoint/restart capabilities, please email us for assistance as far in advance of your need as possible.

express: The ‘express’ queue is for short jobs and debugging/testing scripts. The express queue contains 2 compute nodes and has a wall time limit of one hour (1:00:00).

bigmem: The ‘bigmem’queue directs jobs to one of the two compute nodes that have 256 GB RAM and a NVIDIA Tesla C2075 GPU card. The wall time limit is 120 hours (120:00:00).

killable: The ‘killable’ queue is for long running jobs that are unable to use a checkpoint/restart feature. The wall time limit is 504 hours (504:00:00). Jobs in this queue are subject to being killed, at the discretion of HPCC administrators, for hardware and software issues.

```bash
#PBS -l nodes=1:ppn=1,walltime=10:00
```

This tells qsub how many compute nodes we want to request for our job and how many processors we want from each node. In this case nodes=1 asks the scheduler for 1 compute node and ppn=1 requests 1 processor from the compute node. `walltime` tells the computer the time limit at which it should kill the program. In this case, 10:00 refers to 10 minutes.

Finally, we have:

```bash
#PBS -j oe
```

By default Linux treats the normal output to your screen and error output as two different objects. This command puts them together and makes sure that if anything goes wrong with your job you will have all the error messages saved in your output file. This helps both you and OSU-HPCC staff figure out how to fix any problems that may occur.

These lines all help us setup our job, but we still need to run it. That is what the rest of the script addresses.

```bash
cd $PBS_O_WORKDIR
```

This line tells the compute node to move into our project's directory so that it can work with our files.

```bash
echo "Began parsing tweets..."

python parse_tweets.py raw-tweets.csv parsed-tweets.csv 

echo "Tweets parsed successfully. Have a good day."
```

The last three lines actually execute Pete's script on his twitter data while updating us with what it is doing. We see that the job gives us a helpful message when it begins. It then runs Pete's Python code. Pete's Python code is called `parse_tweets.py`. It takes `raw-tweets.csv` as its input, and outputs the nicely formatted twitter data into a file called `parsed-tweets.csv`.

Pete's Tweets
=============

Pete is now ready to submit his job. He was a little frustrated writing his submit script from scratch as he had to look up so many things. Since he will be submitting lots of jobs, he would like it to be easier next time. Fortunately, he remembers that the HPCC staff have created a sample submissions script. He decides to get a copy so he can just edit the parts he needs next time. He decides to store the example script in his scratch folder.

```bash
cd /scratch/pete
```

Since space in Pete's home folder is limited he can use his scratch folder for storing large data sets. Unfortunately, with multiple users scratch does fill up and occasionally needs to be cleaned out. While it is not a permanent place to leave his data it will be a good place for him to store his example script for now.

```bash
cp /opt/examples/sample.qsub .
```

He now has a copy of the template next time he wants to create a submission script. He now returns to his folder in order to submit his job.

```bash
cd ~/hpc-novice/twitter-data
qsub twitter-submit-script.pbs
```

```bash
592964.mgmt1
```

The batch scheduler gives him back a job number. Pete can use this job number to interact with the scheduler and check on the status of his job. Unfortunately, he remembers that he forgot to change something in the script! He needs to delete his job and remove it from the queue.

> You will use whatever number the scheduler returned to you when you submitted the job. Do not use the actual number printed below!

```bash
qdel 592965.mgmt1
```

He forgot that he wants to have the scheduler email him when the job is finished. He needs to edit his submit script.

```bash
nano twitter-submit-script.pbs
```

He adds the following special comment at the end of the special comments section:

```bash
#PBS -m abe -M EMAIL_ADDRESS@HERE.edu
```

Now it's ready. He resubmits the job.
```bash
qsub twitter-submit-script.pbs
```

```bash
592965.mgmt1
```

Pete knows that the job will email him when it has finished, but he's getting a little bit impatient. He decides to check on the status of his job.

```bash
showq -u pete
```

```bash
ACTIVE JOBS--------------------
JOBNAME            USERNAME      STATE  PROC   REMAINING            STARTTIME

592965              pete       Running     1     4:00:00  Mon Jun 20 16:11:01

          1 Active Job     2813 of 3204 Processors Active (87.80%)
                            245 of  257 Nodes Active      (95.33%)

IDLE JOBS----------------------
JOBNAME            USERNAME      STATE  PROC     WCLIMIT            QUEUETIME


0 Idle Jobs

BLOCKED JOBS----------------
JOBNAME            USERNAME      STATE  PROC     WCLIMIT            QUEUETIME
```

Pete sees that his job has started running. It should email him soon.
