### Automate batch beast job submission on the cluster

Here we're evaluating 4 models, and to ensure the integrity of the runs, we're running 4 chains per model. This allows us to check that each chain converges to the same stationary distribution.

Since that's 16 jobs to submit, it's a little tedious to submit them one by one. The following python scripts automate the job submission. I'm running these on the FHCRC cluster (Rhino).

Step by step of how to run:
1) Move beast xml files, as well as `make_command_files.py` and `run_command_files.py` to the cluster.

2) Load beast 1.8.4 on the cluster with `ml Beast/1.8.4-foss-2016b`.

3) Run `python make_command_files.py` to make a shell script for each job you're submitting. _The reason I'm doing this is because the wrap script for sbatch doesn't like the beast command arguments. The beast command is in shell script, and the shell script gets passed to the sbatch command._

3) Run `python run_command_files.py` to submit each of the jobs to Rhino via slurm.
