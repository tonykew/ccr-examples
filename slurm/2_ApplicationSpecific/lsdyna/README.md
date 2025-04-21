# LS-DYNA  

  LS-DYNA is a general-purpose finite element program capable of simulating complex real world problems. 

# LS-DYNA executables

LS-DYNA is now part of the Ansys software bundle. To load the module, use `module load ansys/2023R1` 

The lsdyna executables do not show up in the path any longer. To use them properly, you'll need to use these commands:

- Single Precision - shared memory parallel (SMP): `$EBROOTANSYS/v231/ansys/bin/linx64/lsdyna_sp.e`
- Double Precision - SMP: `$EBROOTANSYS/v231/ansys/bin/linx64/lsdyna_dp.e`
- Single precision - message passing parallel (MPP): `$EBROOTANSYS/v231/ansys/bin/linx64/lsdyna_sp_mpp.e`
- Double precision - MPP: `mpiexec $EBROOTANSYS/v231/ansys/bin/linx64/lsdyna_dp_mpp.e`

## Example Scripts:  

Provided in this repo are two example lsdyna slurm jobs: [lsdyna.sh](./lsdyna_single_node_smp.sh) a script for running shared memory parallel (SMP) LS-DYNA, [lsdyna_single_node_mpp.sh](./lsdyna_single_node_smp.sh) and [lsdyna_multi_node_mpp.sh](./lsdyna_multi_node_mpp.sh) scripts with examples for message passing parallel (MPP) LS-DYNA.  We provide examples of single and double precision for both options.  Please uncomment the line with the command you want to use and add a `#` to the beginning of the line with the command you don't want to use.  SMP should be run on a single node.  MPP can run on multiple cores of a single node or potentially across multiple nodes.  You can find an example input file `ball_and_plate.k` for testing purposes on CCR's systems in `/util/software/examples/lsdyna`.  These scripts may need to be modified to properly work for your problem.  Please refer to the Ansys LS-DYNA [manuals](https://lsdyna.ansys.com/manuals/) for further information and options.

## Memory Specification:

The LS-DYNA command line option MEMORY specifies memory per node with a base unit words. This is not the same thing as requesting memory (or RAM) for your job.  The argument can be specified in words or megawords (denoted by m). For single precision LS-DYNA, a word is 4 bytes and a megaword is 4 MB. For double precision, a word is 8 bytes and a megaword is 8MB.

Example: (Single Precision)

```
MEMORY=300m     #300 megawords = 300 megawords * 4 MB = 1200 MB (~1.2GB)
MEMORY=600      #600 words = 600 words * 4 B = 2400 KB
```

Example: (Double Precision)

```
MEMORY=300m     #300 megawords = 300 megawords * 8 MB = 2400 MB (~2.4GB)
MEMORY=600      #600 words = 600 words * 8 B = 4800 KB
```

Thanks to [Texas A&M](https://hprc.tamu.edu/kb/Software/LST/ls-dyna/) for their excellent documentation.
