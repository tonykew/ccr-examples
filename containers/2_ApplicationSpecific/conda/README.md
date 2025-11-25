# Example conda container  

CCR does not support running Anaconda on its HPC systems natively for [these reasons](https://docs.ccr.buffalo.edu/en/latest/software/modules/#anaconda-python).  We realize many applications are only available via conda so, as an alternative, users can utilize conda in an Apptainer container.  Utilizing a container for conda eliminates many of the problems it creates on our systems.  This is not a perfect solution though and does require some technical expertise on your part as the CCR user.  We provide this information as an example for installing and creating a conda environment. You can modify these files to install the conda packages you require.  Any issues you may encounter will need to be worked out on your own.  

## Building the container  

Please refer to CCR's [container documentation](https://docs.ccr.buffalo.edu/en/latest/howto/containerization/) for information on building and using Apptainer.  This example provides an Apptainer definition file (`conda.def`) which lists a number of packages and installation steps so Apptainer can install these in an Ubuntu container environment.  This example also uses an environment file (`environment.yml`) to specify which conda packages to install during the build.  For most use cases, you will only need to modify the `environment.yml` file where you'll add additional Python and conda packages to install in your environment. This example utilizes the [conda-forge environment](https://conda-forge.org/) to align with the most recent appropriate use license guidance from Anaconda.

1. Start an interactive job

Apptainer is not available on the CCR login nodes and the compile nodes may not provide enough resources for you to build a container.  We recommend requesting an interactive job on a compute node to conduct this build process.  This will allow you to test your build after completion as well.  Please refer to our documentation on [running jobs](https://docs.ccr.buffalo.edu/en/latest/hpc/jobs/#interactive-job-submission) for more information.  This is provide as an example only and not all users will have access to the resources in this example:  

```
$ salloc --cluster=ub-hpc --partition=general-compute --qos=general-compute --mem=32GB --time=02:00:00
salloc: Pending job allocation 19319338
salloc: job 19319338 queued and waiting for resources
salloc: job 19319338 has been allocated resources
salloc: Granted job allocation 19319338
salloc: Nodes cpn-h23-04 are ready for job
CCRusername@cpn-h23-04:~$

```

2. Navigate to your build directory & set a temp directory for cache  

You should now be on the compute node allocated to you.  In this example we're using our project directory for our build directory. Ensure you've placed your `conda.def` and `environment.yml` file in your build directory  

```
CCRusername@cpn-h23-04:~$ cd /projects/academic/[YourGroupName]/[CCRusername]  
CCRusername@cpn-h23-04:~$ mkdir cache  
CCRusername@cpn-h23-04:~$ export APPTAINER_CACHEDIR=/projects/academic/[YourGroupName]/[CCRusername]/cache  

```

3. Build your container  

```
CCRusername@cpn-h23-04:~$ apptainer build conda-$(arch).sif conda.def
...
...
INFO:    Adding environment to container
INFO:    Creating SIF file...
INFO:    Build complete: conda.sif
```

NOTE: Whenever you modify the `environment.yml` file to add more Python packages to install via conda or pip, you will need to rebuild your container.  

## Running the container  

For our example, we have no additional conda packages installed.  However, we can test this container by running Python: 

```
CCRusername@cpn-h23-04:~$ apptainer exec conda-$(arch).sif python
Python 3.10.16 | packaged by conda-forge | (main, Apr  8 2025, 20:53:32) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Alternatively, you can first get shell access into the container and then run Python, as shown here:   

```
CCRusername@cpn-h23-04:~$ apptainer shell conda-$(arch).sif
Apptainer> python
Python 3.10.16 | packaged by conda-forge | (main, Apr  8 2025, 20:53:32) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Please refer to the CCR [container documentation](https://docs.ccr.buffalo.edu/en/latest/howto/containerization/) for more info on accessing project directories, using GPUs, and other important topics.
