# -*- coding: utf-8 -*-
'''
Created on 9.10.2012

@author: albert
'''
import os
import sys
SEPARATOR = '/'

SUBMIT_ALL = 'submit_all.sh'
COMPRESS = 'compress.sh'
CLEAN_LOGS = 'clean_logs.sh'
CLUSTER = 'cluster.sh'
DEFAULT_LAUNCHER = '/share/apps/flow123d/bin/flow123d'

def create_launcher_scripts(inifile, local = False, cluster = False):
    '''
    wrapper for creating of all launcher scripts
    used by all solvers
    '''
    if local:
        create_local_launcher(inifile, local)
        
    if cluster:
        create_cluster_launcher(inifile, cluster)      
               

def create_cluster_batch(adr):
    '''wrap up - calls all file creators'''    
    create_cluster_submit_all(adr)
    create_cluster_clean(adr)
    create_cluster_compress(adr)
        
    

def create_cluster_launcher(inifile, launcher = None):
    '''creates a sh for cluster / hydra by default''' 
    if not launcher or type(launcher) != type('filename'):
        launcher = DEFAULT_LAUNCHER
    
    adr, inifname  = os.path.split(inifile)
    file_name = adr + SEPARATOR + CLUSTER
    with open(file_name, 'w') as oufile:
        oufile.write('#!/bin/bash\n')
        oufile.write('#$ -cwd\n')
        oufile.write('#$ -j y\n')
        oufile.write('#$ -S /bin/bash\n')
        oufile.write('{} -S {}\n'.format(launcher, inifname))

def create_local_launcher(inifile, flow_exec):
    '''creates a batch file for windows
    '''
    adr, inifname = os.path.split(inifile)
    
    if sys.platform.find('win') > -1:
        file_name = adr + SEPARATOR + 'run.bat'
    else:
        file_name = adr + SEPARATOR + 'run.sh' 
     
    with open(file_name, 'w') as oufile:
        oufile.write('{} -S {}\n'.format(flow_exec, inifname))

def create_cluster_submit_all(adr):
    '''creates submit all batch'''
    file_name = adr + SEPARATOR + SUBMIT_ALL
    with open(file_name, 'w') as oufile:
        oufile.write(cluster_launcher_batch('cluster.sh'))
        
def create_cluster_compress(adr):
    '''
    creates compress shell file
    '''
    file_name = adr + SEPARATOR + COMPRESS
    with open(file_name, 'w') as oufile:
        oufile.write(cluster_compress())
    
def create_cluster_clean(adr):
    '''
    creates cleanup shell file
    '''
    file_name = adr + SEPARATOR + CLEAN_LOGS
    with open(file_name, 'w') as oufile:
        oufile.write(cluster_cleanup())
    

def cluster_launcher_batch(fname):
    '''
    creates launcher batch for Cluster
    '''
    text = '#!/bin/bash\n#\n# search for batchfile name\n'
    text += 'BF={}\n'.format(fname)
    text += '# QSUB\n# -j y\n# -cwd\n# -b y\n# -S /bin/bash\n'
    text += 'for file in *; do\n'
    text += '   if [ -d "$file" ]; then\n\n'
    text += '       echo "Submit: $file/$BF"\n'
    text += '       wd=`pwd`\n'
    text += '       cd $file\n'
    text += '       qsub -j y -cwd -S /bin/bash $BF\n'
    text += '       cd $wd\n'
    text += '   fi\n'
    text += 'done\n'
    return text


def cluster_cleanup():
    '''
    creates launcher for cleanup of data on Cluster
    '''
    text = '#!/bin/bash\n#clean flow logs\n/share/apps/tools/clean_flow_logs/clean_logs.py -d $PWD'
    return text

def cluster_compress():
    '''
    creates launcher for compress  of data on Cluster
    '''
    text = '#!/bin/bash\n#submit compress script to qsub\nqsub -j y -cwd -S /bin/bash /share/apps/tools/transport/compress.qsub'
    return text

if __name__ == '__main__':
    import doctest
    doctest.testmod()
