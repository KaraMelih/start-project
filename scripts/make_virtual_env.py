import argparse
import sys
import os

# Handle command line arguments
parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog="""
DESCRIPTION:
  This script is first to execute when `make_project.sh` is called
  It starts by creating a new environment file and loading some basic
  libraries.
  It then executes two other scripts that sets up folder structure and
  matplotlib parameters.

AUTHOR:
Melih Kara (kara@kit.edu)
"""
)
parser.add_argument('-n', '--name', nargs=1, required=True, 
                    type=str, help='name of the virtual environment')

parser.add_argument('-c', '--useconda', nargs=1, required=False, 
                    default=True, type=bool,
                    help='Use conda to create environment')

parser.add_argument('-v', '--verbose', nargs=1, required=False,
                    default='True', type=str, help='Verbose Output')

parser.add_argument('-r', '--requirements', nargs=1, required=False, 
                    default='Basic_requirements.txt',
                    help='requirements file, default: Basic_requirements.txt')

args = parser.parse_args()

# give meaningful variablenames to the command line
# arguments:
venv_name = args.name[0]
requirements = args.requirements
conda = args.useconda
verbose_ = args.verbose[0]
verbose = True
if (verbose_.lower()=='false' or verbose_.lower()!=str(1)):
    verbose = False
# this will print the outputs only if the verbose is True
verboseprint = print if verbose else lambda *a, **k: None

active_env = ''
existing_environments = []
stream = os.popen('conda env list')
output = stream.readlines()

verboseprint(f'You are using Python {sys.version}')
verboseprint(f'\nYou have {len(output[2:-1])} existing environments')
for line in output[2:-1]:
    venv = line.split('/')[0].strip()
    loc = '/'.join([l.strip() for l in line.split('/')[1:]])
    if '*' in venv:
        venv = venv.split('*')[0].strip()
        active_env = venv
        verboseprint(f'({venv} is the active environment)')
    verboseprint(f'{venv:15s} at location: {loc}')
    existing_environments.append(venv)
    
# Turns out that conda already checks this and raises an error
# not needed.
if venv_name in existing_environments:
    if venv_name.lower() == 'base':
        sys.exit('Cannot overwrite base!\n...Exiting!')
    overwrite = input(f'\n{venv_name} already exists!\nDo you want to overwrite it (y/n)? ')
    if overwrite.lower().strip() != 'y':
        sys.exit('...Exiting!')


# make virtual environment
# for now, stick with conda
os.system(f'conda create -n {venv_name} python')

# copy the 'activator'
venv_loc = f'/{"/".join(loc.split("/")[:-1])}/{venv_name}/bin/'
os.system(f'cp ./activate_this.py {venv_loc}')

# activate the environment within this script
activator = venv_loc + 'activate_this.py'
with open(activator) as f:
    exec(f.read(), {'__file__': activator})

# conda install --file requirements.txt
# os.system(f'conda activate {venv_name}')




# print(os.system(''))
## install notebook (not recommended)
## conda install conda_nb

# or tell python about your new environment
## in your new environment
# conda install ipykernel
# python -m ipykernel install --user --name MYENV --display-name "name to display"

## exit the environment and in your base env
## call jupyter notebook, select this new kernel