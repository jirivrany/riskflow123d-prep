'''
Created on 18.12.2012

@author: Jiri Vrany
'''
def dictToCollections(self,workdct = 'self'):
        '''
        Converts values dir to self.li_attrname lists of attributes
        '''
        if workdct == 'self':
            workdct = self.values
        
        for key in sorted(workdct.keys()):
            tempO = workdct[key]
            vlast = [e for e in dir(tempO) if isinstance(getattr(tempO,e),(list))] 
            matStr = '%s\t%s\t%s' % (tempO.id, tempO.type, tempO.type_spec)
            self.li_materials.append(matStr)
            for attribute1 in vlast:
                atStr = False
                if len(getattr(tempO,attribute1)) > 0:
                    atStr = str(tempO.id)
                    for atVal in getattr(tempO,attribute1):
                        atStr += '\t'
                        atStr += atVal
                
                if atStr:        
                    getattr(self,'li_' + attribute1).append(atStr)  
        
    def getDictFromFile(self, fileName):
        '''@param fileName
           @return Dictionary of values'''
        self.dialog_ini_file_open(fileName)
        self.getDataFromSource()
        self.restart_app_clear()
        if len(self.values) == 0:
            raise EmptyListException("Failed to load data from Material file. Check if it's in correct format.")
        else:
            return self.values
        
         def saveDictToFile(self,fileName,dictName = 'self'):
        '''
        Stores dictionary of material objects to given file
        '''
        try:
            outFile = open(fileName,'w')
        except IOError:
            adr = os.path.dirname(fileName)
            try: 
                os.mkdir(adr)
                outFile = open(fileName,'w')
            except IOError:    
                print 'Error: file %s did not exists. Failed to create dir %s' % (fileName,adr)
                return
        
        self.cleanCollections()
        self.dictToCollections(dictName)
        
        outFile.write(fileHead)
        for mtr_prop in ORDER_OF_MTR:
            outFile.write('$'+mtr_prop+'\n')
            liname = 'li_'+mtr_prop.lower()
            if mtr_prop == 'Materials': outFile.write(str(len(self.li_materials))+'\n')
            for line in getattr(self,liname):
                outFile.write(line)
                outFile.write('\n')
            outFile.write('$End'+mtr_prop+'\n')
                        
        self.restart_app_clear(outFile)
        
        
        
        
            '''
            for attribute1 in vlast:
                atStr = False
                if len(getattr(current_material,attribute1)) > 0:
                    atStr = str(current_material.id)
                    for atVal in getattr(current_material,attribute1):
                        atStr += '\t'
                        atStr += atVal
                
                if atStr:        
                    getattr(self,'li_' + attribute1).append(atStr)         
            '''   
