'''
Created on 8.1.2013

@author: Jiri Vrany
'''

class MonteLogger(object):
    '''
    logging tool for monte carlo method
    '''


    def __init__(self, output_dir):
        '''
        Constructor - creates log file
        '''
        file_name = '{}{}.log'.format(output_dir, 'montecarlo')
        try:
            self.log_file = open(file_name, 'w')
        except IOError:
            print "failed to create monte carlo log file"
            return False
        
    def log_message(self, loop_nr, material_id, hydraulic_cond, new_value):
        '''
        log message to file
        '''
        print >> self.log_file, '{} {} {} {}'.format(\
                 loop_nr, material_id, hydraulic_cond, new_value)
   
    def close(self):
        '''
        closes self file
        '''
        self.log_file.close()             