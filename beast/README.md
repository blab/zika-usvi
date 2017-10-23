## Phylogeographic Analysis

**Outline: Basic steps of our two-step BEAST analysis pipeline**
1) Use BEAST to sample a posterior distribution of time-resolved phylogenies.
2) Assess convergence by looking at traces ensuring that separate chain (I've run 4 per model) converge on the same values.
3) Remove burnin from the posterior samples, and remove the outgroup used to root the tree from each tree in the posterior sample.
4) Combine the `.trees` files from each chain that used the same model.
5) Use the combined `.trees` file as the `EmpiricalTreesDistribution` input for the GLM analysis.

##### Automate batch beast job submission on the cluster

Here we're evaluating 4 models, and to ensure the integrity of the runs, we're running 4 chains per model. This allows us to check that each chain converges to the same stationary distribution.

Since that's 16 jobs to submit, it's a little tedious to submit them one by one. The following python scripts automate the job submission. I'm running these on the FHCRC cluster (Rhino).

Step by step of how to run:
1) Move beast xml files, as well as `make_command_files.py` and `run_command_files.py` to the cluster.

2) Load beast 1.8.4 on the cluster with `ml Beast/1.8.4-foss-2016b`.

3) Run `python make_command_files.py` to make a shell script for each job you're submitting. _The reason I'm doing this is because the wrap script for sbatch doesn't like the beast command arguments. The beast command is in shell script, and the shell script gets passed to the sbatch command._

3) Run `chmod 777 *.sh` to ensure that all of the shell files are executable.

4) Run `python run_command_files.py` to submit each of the jobs to Rhino via slurm.

##### Removing outgroups and burnin, and combining `.trees` files together.

[This script](../scripts/remove-outgroup.ipynb) will remove trees that are burnin, and also remove outgroup taxa.

Trees files are combined using the `logcombiner` tool in the BEAST suite.
