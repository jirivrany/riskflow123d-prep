'''
Created on 20.12.2012

@author: Jiri Vrany
'''
import os
import shutil
import glob

PROBLEMS = {
            'basic': 'basicProblem',
            'monte': 'MonteCarlo',
            'sens': 'Sensitivity'
            }


def normalize_result_stora_poro(value):
    '''
    the new value for storativity or porosity has to be in <0.00001, 0.99999>
    '''
    try:
        value = float(value)
    except ValueError:
        value = 0.00001

    result = round_to_positive_zero(value)
    if result > 1:
        return 0.99999
    else:
        return result


def round_porosity(value):
    '''
    takes a text value, convert it to float, round it and return
    str again
    '''
    try:
        value = float(value)
    except ValueError:
        value = 0.00001

    return str(round_to_positive_zero(value))


def round_to_positive_zero(value):
    '''
    takes a value convert it to 0.00001 if it's zero
    '''
    if value < 0.00001:
        return 0.00001
    else:
        return value


def create_task_identifier(problem_type, work_dir):
    '''
    Save problem identifier file into given work_dir
    '''
    try:
        task_file = open(work_dir + '/problem.type', 'w')
        print >> task_file, PROBLEMS[problem_type]
        task_file.close()
    except IOError:
        print 'oh crap'


def copy_master_files(flow_ini, output_dir, separator):
    '''
    create a copy of original basic problem
    @param output_dir - where to copy
    @param flow_ini - a FlowIni object
    '''
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    original_dir = flow_ini.dir_name

    shutil.copy2(flow_ini.file_name, output_dir)

    copy_boudnary_cond_files(original_dir, output_dir)

    for master_file_name in flow_ini.dict_files.values():
        src = original_dir + separator + master_file_name
        try:
            shutil.copy2(src, output_dir)
        except IOError:
            pass

def copy_boudnary_cond_files(original_dir, output_dir):
    '''
    Fix for Flow1.6.6 boundary conditions in time change
    '''
    files = glob.iglob(os.path.join(original_dir, "*.bct_*"))
    for file_name in files:
        if os.path.isfile(file_name):
            shutil.copy2(file_name, output_dir)

if __name__ == '__main__':
    print round_porosity('0')
    print round_porosity('0.0001')
    print round_porosity('0.00001')
    print round_porosity('')
