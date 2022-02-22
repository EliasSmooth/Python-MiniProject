import glob

from WriteToLog import getData
from processChecker import append, check, skip
from directoryHandler import fileError


#Retreives all files in the chosen directory that belong to the .xlsx filetype
files = glob.glob('./Assets/*.xlsx')

#Loops through the array of filenames and runs the main process for each one
if files != []: 
    for file in range(len(files)):
        instance = files[file] 
        if check(files[file]):
            skip(instance)
            next 
        else: 
            formatted = instance + "\n"
            
            num = files[file][-9:-5] 
            try:
                int(num)
                getData(files[file], file)
                append(formatted, instance)
            except:
                fileError(files[file])
        
else: 
    print("No Files")