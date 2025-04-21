# Example AlphaFold job

Provided is an example AlphaFold slurm job and [T11050.fasta](./T1050.fasta) is a protein sequence.

A couple notes on running AlphaFold:

- AlphaFold does not currently support nvidia H100 cards. So you'll want to use any of our A100 or V100 GPU nodes.
- CCR has downloaded the full genetic databases and model parameters and the path is automatically included when running run_alphafold.py. The full path can be found here:
```
echo $ALPHAFOLD_DATA_DIR
/util/software/data/alphafold
```
- Many of the examples you'll find online run AlphaFold in docker. You do not want to do this. Instead just substitute python3 docker/run_docker.py with the script provided by the alphfold module 
run_alphafold.py. They will have the same CLI arguments.
