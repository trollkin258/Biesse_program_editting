import os 
from os import path
def filechecking():
    print('Folder check')

    if not os.path.exists('Program_files'):
        os.makedirs('Program_files')
    
    if not os.path.exists('Program_files/Project_files'):
        os.makedirs('Program_files/Project_files')

    if not os.path.exists('Program_files/Drilling_programs'):
        os.makedirs('Program_files/Drilling_programs')
        
#filechecking()