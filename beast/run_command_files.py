import os
import glob

for cmdfile in glob.glob('*.sh'):
    submit_cmd = 'sbatch --time=30-0 -c 4 -N 1 --mem=32000 --wrap="$PWD/{}"'.format(cmdfile)
    print submit_cmd
    os.system(submit_cmd)
