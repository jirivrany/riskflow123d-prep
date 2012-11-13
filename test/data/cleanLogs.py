'''
Created on 25.1.2012

@author: albert
'''
import os

def clean(dir_name):
    '''rekurzivne projde podadresare dir_name, a smaze nalezene soubory flow123.0.log'''
    smazano = 0
    for root, dirs, files in os.walk(dir_name):
        for f1 in files:
            tpth = '/'.join([root, f1])
            if f1 == 'flow123.0.log' or f1.startswith('cluster.sh.o'):
                try:
                    os.remove(tpth)
                    smazano += 1
                except os.error:
                    print 'nelze smazat flow.log log / chyba pristupu'    
    
    print 'smazano {} souboru flow123.0.log a clusters.sh.o'.format(smazano)
    
if __name__ == '__main__':
    clean(os.curdir)