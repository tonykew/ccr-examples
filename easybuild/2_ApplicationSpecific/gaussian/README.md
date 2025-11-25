# Example Gaussian Easybuild

This is an example of installing Gaussian with Easybuild on a CCR compile node.  Gaussian is not provided in CCR's central software repository due to licensing restrictions.  Each group must obtain the installation media and install Gaussian in their own project directory.  Here we provide instructions for using an Easybuild recipe to install this in your group's project space.

Prior to starting this installation, you should be familiar with CCR's [software environments](https://docs.ccr.buffalo.edu/en/latest/software/modules/) and how to use software modules.  Please read the instructions on [building your own software](https://docs.ccr.buffalo.edu/en/latest/software/building/) - specifically on [building software for your group](https://docs.ccr.buffalo.edu/en/latest/software/building/#building-modules-for-your-group).

## Installation Steps  

The steps for this process are as follows:  

If you've never installed software with Easybuild, you will need to create a directory in your group's project space and setup your environment to see your group's modules.  Complete the steps in #1.  If you've previously installed software and this is already configured, skip to step #2.  

1. Login to CCR login node and setup your Easybuild installation environment.  This can be done with SSH (as shown here) or using the OnDemand terminal app.  

```
ssh [CCRusername]@vortex.ccr.buffalo.edu
```

If you don't already have an Easybuild directory for your group, create one:  
NOTE: substitute YOURGROUPNAME for your PI group directory name

```
$ mkdir /projects/academic/YOURGROUPNAME/easybuild 
```

If you've never installed software with Easybuild, you will need to setup your environment to see your group's modules by setting the `CCR_CUSTOM_BUILD_PATHS` env variable. Note: this only has to be done once per user account.  If the `~/.ccr/modulepaths` file already exists, please edit this file and add this new directory to the existing line and separate the directory names with a colon `:`

```
$ export CCR_BUILD_PREFIX=/projects/academic/YOURGROUPNAME/easybuild
$ export CCR_CUSTOM_BUILD_PATHS=$CCR_BUILD_PREFIX

# To ensure this path gets picked up on login
$ mkdir -p $HOME/.ccr
$ echo $CCR_CUSTOM_BUILD_PATHS > ~/.ccr/modulepaths
$ exit  (to log out of the vortex login node)
```


2. Login to a login node and then into a [compile node](https://docs.ccr.buffalo.edu/en/latest/hpc/clusters/#compile-nodes)   
```
ssh [CCRusername]@vortex.ccr.buffalo.edu
$ ssh compile
```

3. Upload your Gaussian software installation file to CCR and place in your home or project directory

4. Create Gaussian Easybuild recipe  
In the folder that your Gaussian software was uploaded to, create a file called `Gaussian-16.C.02-AVX2.eb`  Copy the contents from [this example](Gaussian-16.C.02-AVX2.eb) Easybuild recipe and place them in your new recipe file.  Edit the file as described, save and exit the editor.  There are several things to be aware of with this recipe file:  
- You MUST name the file in the same way that CCR provides in this example
- If you're installing a different version of Gaussian, you must update the Easybuild recipe name with the updated version number AND change the version number within your Easybuild recipe on line 7.  
- You MUST update line 32 of your Easybuild recipe with the full path of where you've stored your installation media. What we have for that line in our example is simply a placeholder.  
- You will need to update the checksum value on line 33 to match the checksum of your software installation media.  To get the checksum of a file, run:  `sha256sum filename`  

5. Prepare to install the software

Load the Easybuild module: 
```
$ module load easybuild
```

Set your installation path location to match your group's easybuild directory:  
```
$ export CCR_BUILD_PREFIX=/projects/academic/YOURGROUPNAME/easybuild
```

6. Install the software

```
$ eb Gaussian-16.C.02-AVX2.eb --umask=007
```

## Using your module  

Once the installation completes successfully, when you search for the module you should see it listed in a section at the top with your group's installation path listed.  For example:  

```
$ module spider gaussian

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  gaussian: gaussian/16.C.02-AVX2
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    Description:
      Gaussian provides state-of-the-art capabilities for electronic structure modeling. Gaussian 09 is licensed for a wide variety of computer systems. All versions of Gaussian 09 contain every scientific/modeling feature, and none imposes any
      artificial limitations on calculations other than your computing resources and patience. This is the official gaussian AVX2 build.

    Properties:
      Chemistry libraries/apps

    This module can be loaded directly: module load gaussian/16.C.02-AVX2

    Help:

      Description
      ===========
      Gaussian provides state-of-the-art capabilities for electronic structure
      modeling. Gaussian 09 is licensed for a wide variety of computer
      systems. All versions of Gaussian 09 contain every scientific/modeling
      feature, and none imposes any artificial limitations on calculations
      other than your computing resources and patience.

      This is the official gaussian AVX2 build.


      More information
      ================
       - Homepage: https://www.gaussian.com/
```

If you're not seeing your module, make sure you've setup your custom module paths correctly, as described [here](https://docs.ccr.buffalo.edu/en/latest/software/building/#building-modules-for-your-group) and demonstrated in step 1 above.  

To load the module run:
```
$ module load gaussian/16.C.02-AVX2
$ gaussian --help
```

## Troubleshooting  

This installation will take awhile.  If it does not complete successfully, please refer to the log files it reports in the output of the installation attempt to see what the issue might be.  They are verbose but very informative. 

We provide a full [Easybuild tutorial](https://docs.ccr.buffalo.edu/en/latest/howto/easybuild/) to better understand how this tool works.  We highly recommend referring to it if you run into any issues.  The [Frequently Asked Questions](https://docs.ccr.buffalo.edu/en/latest/howto/easybuild/#frequently-asked-questions) section covers most common errors.

If you have any issues with these instructions, please contact [CCR Help](https://docs.ccr.buffalo.edu/en/latest/help/)

