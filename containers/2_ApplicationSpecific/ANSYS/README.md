# ANSYS container

[ANSYS](https://ansys.synopsys.com) is a commercial suite of engineering simulation software products.

> [!WARNING]
> ANSYS is a suite of commercial programs.
> You MUST have appropriate licenses for every ANSYS product you use
> Roswell Park researchers and other commercial users should utilize their own license with ANSYS products

UB provides an educational license for ANSYS.  The license is for
**academic purposes only**  
All the [examples](./EXAMPLES.md) use the academic license file.


CCR providses a couple of pre-built ANSYS container:

ANSYS release 2026 R1 - installed from CD (no service packs applied)

```bash
/util/software/containers/x86_64/ANSYS-2026_R1-x86_64.sif
```

ANSYS release 2026 R1 - installed from CD, with Service Pack 4 applied

```bash
/util/software/containers/x86_64/ANSYS-2026_R1.04-x86_64.sif
```

The following link will always point to the lastest patched version:

```bash
/util/software/containers/x86_64/ANSYS-x86_64.sif 
```


If these containers don't fit your needs, for example, you want to create a smaller
container file with a subset of the applications, you can use the following
instructions to build an ANSYS container.


## Building the container

A brief guide to building the ANSYS container follows:  
Please refer to CCR's [container documentation](https://docs.ccr.buffalo.edu/en/latest/howto/containerization/) for more detailed information on
building and using Apptainer.

The .def file is writtten to build an ANSYS in one of three ways: 
from CD .iso files, CD .iso files with a Service Pack tarball, and with
an ANSYS installer scrtipt.  The latter is untested & requires access to
https://id.ansys.com to generate an AnsysID token for the script to run,
however this should work.


1. Start an interactive job

Apptainer is not available on the CCR login nodes and the compile nodes may not
provide enough resources for you to build a container.  We recommend requesting
an interactive job on a compute node to conduct this build process.  
Note: a GPU is NOT needed to build the ANSYS container  
See CCR docs for more info on [running jobs](https://docs.ccr.buffalo.edu/en/latest/hpc/jobs/#interactive-job-submission)
The build can take two hours to complete.

```bash
export SBATCH_ACCOUNT="[SlurmAccountName]"
```

```bash
salloc --cluster="ub-hpc" --partition=general-compute --qos=general-compute \
 --exclusive --mem=0 --time=2:30:00
```

Sample outout:

> ```
> salloc: Granted job allocation 26368781
> salloc: Nodes cpn-b02-31-01 are ready for job
> CCRusername@cpn-b02-31-01$ 
> ```


2. Navigate to your build directory and use the Slurm job local temporary directory for cache

You should now be on the compute node allocated to you.  
In this example we're using our project directory for our build directory.  

Change to your ANSYS directory

```bash
cd /projects/academic/[YourGroupName]/ANSYS
```

...and fetch the .def file:

```bash
curl -LO https://raw.githubusercontent.com/ubccr/ccr-examples/refs/heads/main/containers/2_ApplicationSpecific/ANSYS/ANSYS.def
```

If you wish to install a subset of the appications, you can edit the .def file
and change the ./INSTALL line.  For example, to install only LS-DYNA add
"-lsdyna" to the line:

```bash
[...]
  bash ./INSTALL ${extra_args} -silent -lsdyna
[...]
```


3. Build your container

There are three ways to install ANSYS - see the comments section at the top of
the ANSYS.def file for more information

CD images, Service Packs and the ANSYS installer script, can be downloaded
from the [ANSYS customer website](https://customer.ansys.com)  
The installer script install requires an AnsysID token from the [ANSYS ID Portal](https://id.ansys.com/)


### CD image only install

The CD build process requires the ANSYS .iso files e.g.

```bash
ls -1 *.iso
```

Sample outout:

> ```
> ANSYS2026R1_LINX64_DISK01.iso
> ANSYS2026R1_LINX64_DISK02.iso
> ANSYS2026R1_LINX64_DISK03.iso
> ANSYS2026R1_LINX64_DISK04.iso
> ANSYS2026R1_LINX64_DISK05.iso
> ANSYS2026R1_LINX64_DISK06.iso
> ANSYS2026R1_LINX64_DISK07.iso
> ANSYS2026R1_LINX64_DISK08.iso
> ANSYS2026R1_LINX64_DISK09.iso
> ANSYS2026R1_LINX64_DISK10.iso
> ANSYS2026R1_LINX64_DISK11.iso
> ANSYS2026R1_LINX64_DISK12.iso
> ANSYS2026R1_LINX64_DISK13.iso
> ```

In the case the base name for the CD is "ANSYS2026R1_LINX64_DISK" i.e. all the
CD .iso files start with "ANSYS2026R1_LINX64_DISK"

This example uses INSTALL_CD_BASENAME="ANSYS2026R1_LINX64_DISK"
based on the name of the .iso files as noted above.

Building the ANSYS container takesabout one and a half hours...

```bash
export APPTAINER_CACHEDIR="${SLURMTMPDIR}"
apptainer build \
 --build-arg TMPDIR="${SLURMTMPDIR}" \
 --build-arg INSTALL_CD_BASENAME="ANSYS2026R1_LINX64_DISK" \
 --bind "/scratch":"/scratch" \
 --bind "$(pwd)":"/tmp/installer_dir" \
 "ANSYS-$(arch).sif" "ANSYS.def"
```

Sample truncated output:

> ```
> [....]
> INFO:    Adding environment to container
> INFO:    Creating SIF file...
> INFO:    Build complete: ANSYS-x86_64.sif
> ```


### Service Pack install

The build process requires the ANSYS CD .iso files as documented above, and an
ANSYS Service Pack Tarball

This example uses INSTALL_CD_BASENAME="ANSYS2026R1_LINX64_DISK" based
on the CD .iso filenames as documented in the [CD image only install section](#cd-image-only-install).
We also provide the Service Pack tarball name with
SERVICE_PACK_TARBALL="ANSYS_2026R1.04_LINX64.tgz"

Building the ANSYS container can take up to two hours...

```bash
export APPTAINER_CACHEDIR="${SLURMTMPDIR}"
apptainer build \
 --build-arg TMPDIR="${SLURMTMPDIR}" \
 --build-arg INSTALL_CD_BASENAME="ANSYS2026R1_LINX64_DISK" \
 --build-arg SERVICE_PACK_TARBALL="ANSYS_2026R1.04_LINX64.tgz" \
 --bind "/scratch":"/scratch" \
 --bind "$(pwd)":"/tmp/installer_dir" \
 "ANSYS-$(arch).sif" "ANSYS.def"
```

Sample truncated output:

> ```
> [....]
> INFO:    Adding environment to container
> INFO:    Creating SIF file...
> INFO:    Build complete: ANSYS-x86_64.sif
> ```


### ANSYS Installer script install

The installer script installation requires the insrtaller script
"AnsysInstaller.sh" and an AnsysID token from the [ANSYS ID Portal](https://id.ansys.com/)

The installer script filename is passed to the build in the INSTALL_SCRIPT
variable and the AnsysID token is passed in the ANSYSID_TOKEN variable

```bash
export APPTAINER_CACHEDIR="${SLURMTMPDIR}"
apptainer build \
 --build-arg TMPDIR="${SLURMTMPDIR}" \
 --build-arg INSTALL_SCRIPT="AnsysInstaller.sh" \
 --build-arg ANSYSID_TOKEN="_ansys_token_here_" \
 --bind "/scratch":"/scratch" \
 --bind "$(pwd)":"/tmp/installer_dir" \
 "ANSYS-$(arch).sif" "ANSYS.def"
```

Sample truncated output:

> ```
> [....]
> INFO:    Adding environment to container
> INFO:    Creating SIF file...
> INFO:    Build complete: ANSYS-x86_64.sif
> ```


See the [EXAMPLES file](./EXAMPLES.md) for information on running applications
in an ANSYS container.  

## Sample Slurm scripts

[ANSYS LS-DYNA example batch script](https://raw.githubusercontent.com/ubccr/ccr-examples/refs/heads/main/containers/2_ApplicationSpecific/ANSYS/ANSYS_lsdyna_single_node_MPI.bash)  
[ANSYS LS-DYNA example batch script](https://raw.githubusercontent.com/ubccr/ccr-examples/refs/heads/main/containers/2_ApplicationSpecific/ANSYS/ANSYS_lsdyna_single_node_OpenMP.bash)  

## Documentation Resources

For more information on ANSYS see the [ANSYS Help Center](https://ansyshelp.ansys.com/public/account/secured?returnurl=/Views/Secured/main_page.htm) and the [ANSYS YouTube Channel](https://www.youtube.com/channel/UCdymxOTZSP8RzRgFT8kpYpA)

