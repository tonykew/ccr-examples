# ANSYS container examples

[ANSYS](https://ansys.synopsys.com) is a commercial suite of engineering simulation software products.

> [!WARNING]
> ANSYS is a suite of commercial programs.
> You MUST have appropriate licenses for every ANSYS product you use
> Roswell Park researchers and other commercial users should utilize their own license with ANSYS products

UB provides an educational license for ANSYS.  The license is for **academic purposes only**
All the examples use the academic license file.

To run the GUI version of an application, use the [CCR OnDemand portal](https://ondemand.ccr.buffalo.edu)
Most of the GUI applications require a GPU to proveide GLX graphic support, as
shown in the example below.  

For example:

Open a browser window to our [OnDemand portal](https://ondemand.ccr.buffalo.edu)

[UB-HPC & Faculty Cluster Desktop]

Cluster: UB-HPC  
Slurm Account: [Your Slurm account]  
Partition: [general-compute]  
Quality of Service: [general-compute]  
Number of Hours Requested: 4  
Number of Cores: 28  
Amount of Memory: 128000  
Number of GPUs: 1  

[Launch]

Once the Slurm job starts you can press the button that appears
[Launch UB-HPC & Faculty Cluster Desktop]

A new window will open with the GUI displayed.

Open a terminal with:
[Applications][Terminal Emulator]

load VirtualGL with:

```bash
module load gcc virtualgl
export VGL_DISPLAY="$(ls -d /sys/bus/pci/devices/$(nvidia-smi --query-gpu=gpu_bus_id --format=csv,noheader | sed 's/^0000//' | tr '[:upper:]' '[:lower:]')/drm/card* | sed -E 's|^.*(card[0-9]+)$|/dev/dri/\1|')"
```

Note: If you want to verify that the VirtualGL acceleration is working, running
"glxspheres64" unaccelerated should generate 30 to 40 frames per second:

```bash
glxspheres64
```

Whereas running glxspheres64 with "vglrun" should generate over 260 frames per
second:

```bash
vglrun glxspheres64 
```

This example runs the ANSYS GUI application "cfx5"

```bash
export CCR_GROUP="[YourGroupName]"
```

```bash
vglrun apptainer run --nv --no-env=XDG_DATA_DIRS --writable-tmpfs \
 --bind "/util":"/util","/scratch":"/scratch" \
 --bind "/projects/academic/${CCR_GROUP}":"/projects/academic/${CCR_GROUP}" \
 --bind "/util/software/licenses/ansyslmd.ini":"/opt/ansys_inc/shared_files/licensing/ansyslmd.ini":ro \
 "/util/software/containers/x86_64/ANSYS-2026_R1-x86_64.sif" \
 cfx5
```

You can replace "cfx5" in the example above with any of the following:
cfx5launch, cfx5pre, cfx5solve, cfx5posta, fluent, icemcfd, cfxtg, runSherlock, runwb2

Note that, currently, "icepak" does not run in GUI mode, but the non GUI
"icepak_batch" can be used, for example:


```bash
apptainer run --nv --no-env=XDG_DATA_DIRS --writable-tmpfs \
 --bind "/util":"/util","/scratch":"/scratch" \
 --bind "/projects/academic/${CCR_GROUP}":"/projects/academic/${CCR_GROUP}" \
 --bind "/util/software/licenses/ansyslmd.ini":"/opt/ansys_inc/shared_files/licensing/ansyslmd.ini":ro \
 "/util/software/containers/x86_64/ANSYS-2026_R1-x86_64.sif" \
 icepak_batch [...]
```

