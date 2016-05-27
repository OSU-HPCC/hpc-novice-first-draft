Modules
=======
>*Learning Objectives*
>*    Student will demonstrate an understanding of what modules are and why they are important.
>*    Student will be able to find out if the software s/he needs to use is installed on the cluster.
>*    Student will be able to load the software that s/he needs in order to run his/her job using `module load`.
>*    Student will be able to verify that the correct environment has been loaded using `module list`.

We now know how to log in, but what good is a supercomputer if we cannot use the software on it? Windows has the Start Menu and Macs have the launch bar, but how do we find out what programs or software are available on Cowboy when all we have is the command prompt? The answer is modules. Modules are an extremely powerful system that allows multiple users with different versions of software all to use the same machine at the same time. 
>Modules are implemented a little bit differently on each HPC cluster. In fact, some HPC clusters don't even use modules! We will be using Cowboy's module system for this lesson. To see other kinds of module systems that exist, see here.

First, it would be nice to know what software Cowboy has available for us to use.

```shell
module avail
```

```shell
---------------------------- /opt/modulefiles/Compilers -----------------------------
   cmake/3.0.0               mpich2/intel                  (D)
   cmake/3.1.3               mvapich/gnu
   cmake/3.2.2       (D)     mvapich/gnu-4.6.2
   cuda/toolkit-4.2          mvapich/intel                 (D)
   cuda/toolkit-5.5  (D)     mvapich2-1.8/gnu
   gcc-4.6.2                 mvapich2-1.8/gnu-4.6.2
   gcc-4.7.2                 mvapich2-1.8/intel            (D)
   gcc-4.8.4                 openmpi-1.4/gnu
   gcc-4.9.2                 openmpi-1.4/gnu-4.6.2
   intelmpi/4.1.0            openmpi-1.4/intel             (D)
   intelmpi/5.0.2    (D)     openmpi-1.6/gnu
   mpich2/gnu                test-dont-use/devtoolset-1.1
   mpich2/gnu-4.6.2

--------------------------- /opt/modulefiles/Applications ---------------------------
    R/2.15.1                               last/320
   R/2.15.2                       (D)     lastz/1.02
   R/3.0.2                                lastz/1.03.02
   R/3.1.2                                lastz/1.03.54                      (D)
   R/3.1.3                                libint/2.0.3
   R/3.2.1                                libxc/2.0.2-openmpi-intel
   abinit/6.12.3-openmpi-gnu              libxc/2.0.2
   abinit/7.0.4-openmpi-intel     (D)     libxc/2.2.1                        (D)
   abyss/1.3.7-openmpi-intel              log4cpp/1.1.1
   activeperl/5.18.1.1800                 lynx/2.8.7
   alignreads/2.4.0                       macaulay2/2.1.6
   alignreads/2.5.2-b-3           (D)     makedepend/1.0.5
   alignreads/2.23                        maker/2.28-openmpi-intel
   allpaths-lg/45553                      maker/2.28                         (D)
   amber/amber12                          mathematica/9.0.1
   amber/amber14                  (D)     mathematica/10.0.0                 (D)
   amos/3.0.0                             matio/1.5.2
   anaconda/1.6.1                 (D)     matlab/R2012b
   anaconda/2.2.0                         matlab/R2014a                      (D)
   ansys/15                               mauve/20120607
   antismash/2.0.2                        megacc/7.00-beta
   arb/5.5                                megan/megan5
   armadillo/4.300.8                      metapathways/1.0
   armadillo/4.550.2              (D)     metasim/0.9.5
   augustus/2.6.1                         mgltools/1.5.6
   augustus/3.0.1                 (D)     mgltools/1.5.7rc1                  (D)
   autoconf/2.69                          migrate-n/3.4.4-gcc
   autodock-vina/1.1.2                    migrate-n/3.4.4-openmpi-1.4-intel  (D)
   automake/1.15                          mira/3.4.1.1
--More--
```

>Notice the `--More--` at the end of the output. The shell is using a program called More to output the results since they go off the screen. To see more, press SPACE-BAR to page down one page at a time and press ENTER to scroll down one line at a time. The normal promt will return again once you reach the end of the list.

Here we have a table listing all the software installed on Cowboy. Notice there are two general categories: Compilers, and Applications. Compilers are used by users who are writing their own code, while Applications work the exact same way as Applications in Windows or on a Macintosh (except no GUI). Look through the list and see if you can find `mathematica`. There are two entries: `mathematica/9.0.1` and `mathematica/10.0.0`. That’s because there are two different versions of Mathematica installed on Cowboy and users are able to use either one. Next notice that some of the modules have a (D) next to them. Since there are multiple versions of each piece of software, certain versions are designated as default. In the case of Mathematica, if the user tells the computer to load Mathematica, but doesn’t tell it which version to load, it will automatically load version 10.0.0.

We can also search to see if a particular piece of software is installed on Cowboy by using the module search tool, spider:

```shell
module spider mrbayes
```

```shell
Rebuilding cache file, please wait ... done

  ---------------------------------------------------------------------------------
     mrbayes:
  ---------------------------------------------------------------------------------
       Description:
      See http://mrbayes.sourceforge.net/ 

     Versions:
        mrbayes/3.1.2-openmpi-intel
        mrbayes/3.2.1-openmpi-intel
        mrbayes/3.2.2-openmpi-intel

  ---------------------------------------------------------------------------------
     To find detailed information about mrbayes please enter the full name.
  For example:

     $ module spider mrbayes/3.2.2-openmpi-intel
  ---------------------------------------------------------------------------------
```

In order to use a particular piece of software, we need to 'load' it.

```shell
module load mathematica
```

We can also check to see what software we have loaded so far.

```shell
module list
```

```shell
1) mathematica/10.0.0
```

Let's remove Mathematica and load MrBayes instead.

```shell
module rm mathematica
module load mrbayes
```

Checking on what we have loaded now, we see something interesting.

```shell
module list
```

```shell
1) mrbayes/3.2.2-openmpi-intel    2) openmpi-1.4/intel    3) beagle/1.0
```

Wait a minute, why are there so many modules? Didn’t we just load MrBayes? The beauty of modules is that it automatically loads MrBayes and any other software that MrBayes depends on to run. Lets remove all our software and start again with a clean slate.

```shell
module purge
```

GRADUATE STUDENT STORY CONTINUES HERE, WORK IN `module swap` SHORTCUT INTO THE STORY.
