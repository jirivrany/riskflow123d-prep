'''
Created on 20.12.2012

@author: Jiri Vrany
'''

def identify_task(problem_type, work_dir):
    '''
    Save problem identifier file into given work_dir
    '''
    try:
        task_file = open(work_dir + '/problem.type', 'w')
        print >> task_file, problem_type
        task_file.close()
    except IOError:
        print 'oh crap'

