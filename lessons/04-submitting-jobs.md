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

THE STORY CONTINUES ON. OUR GRADUATE STUDENT WILL USE THE FOLLOWING COMMAND AS THE STORY CONTINUES: `qsub`, `showq`, `showq | grep`, `showq -u`, `qpeek`, `qdel`.
