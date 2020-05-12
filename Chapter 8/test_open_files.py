#!/usr/bin/python3
import files_module

empty_str =''
print('TESTING files_modele FUNCTIONS')

try:
    smoking_datafile, cancer_datafile = files_module.openFiles()

    print('Data files opened')
    
    smoking_data, cancer_data = files_module.readFiles(smoking_datafile, cancer_datafile)
    print ('\n List of smoking data read')
    print(smoking_data)
    
    print('\n List of cancer data read')
    print(cancer_data)
    
except IOError as e:
    print(str(e))
    print('Too many attempts to open files')
    print('Program terminated')
