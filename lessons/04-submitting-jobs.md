Submitting Jobs (one possibility is to have several versions of this module for common schedulers)
====================================================================================
>*Learning Objectives*
>*    Student will be able to demonstrate understanding of what a scheduler is and why it is important.
>*    Student will be introduced to some of the common schedulers in use on different clusters and will understand that they each have their own syntax.
>*    Student will be able to complete the following tasks using `qsub` and a pre-made submit script: submit a job, check on the status of a job, cancel a job, check the output once a job has been completed.

On Cowboy (or any HPC cluster) you won't run your job on the login node. You can edit files here, but when it's time to run a job, you will need to use the batch scheduler command to move you to a compute node. The job scheduler takes some information from you, finds the best compute node(s) to use and runs your job there.

![Cowboy Network](/img/cowboynetwork.png "Cowboy Network")
 
*ALL JOBS AND SCRIPTS SHOULD BE RUN THROUGH THE SCHEDULER*. If we run our jobs on a login node it will slow down and other users will not be able to log into Cowboy. Cowboy is a shared resource with many users all competing for compute time and the only fair way to split compute time between different users is to use the scheduler. The scheduler is also how our jobs gain access to Cowboy’s compute nodes.

The most efficient way to use Cowboy is as follows: 
* Login
* Set up jobs with submit scripts
* Submit them 
* Log out. 
* Have the scheduler email you when your jobs are finished.

>While almost every HPC cluster uses a scheduler to manage different jobs from different users, there are many, *many* different types of schedulers in use. Check with your local HPC staff to see what scheduler they use. They should be able to get you resources about what commands to use for that particular scheduler. Different scheulers emphasize different features, but all schedulers are tasked with the job of determining the most equitible and efficient way of running multiple jobs from multiple users on the cluster. They do this by queing jobs and determining which jobs are assigned to which nodes. For the purposes of this lesson, we will use Cowboy's scheduler [qsub](http://docs.adaptivecomputing.com/torque/4-0-2/Content/topics/commands/qsub.htm).

In order to use a scheduler, we must use a submit script. A submit script is a special [bash script](http://swcarpentry.github.io/shell-novice/ "Software-Carpentry Bash Lessons") that tells the scheduler what to do. Essentially, we type the commands that run our job into a text file and give that file to the scheduler. Then, when it is our job's turn in line, the scheduler will look inside the file and execute whatever commands we have put inside.

THE STORY CONTINUES ON. OUR GRADUATE STUDENT WILL USE THE FOLLOWING COMMAND AS THE STORY CONTINUES: `qsub`, `showq`, `showq | grep`, `showq -u`, `qpeek`, `qdel`.
