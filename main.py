import glob

from WriteToLog import getData
from processChecker import append, check


#Retreives all files in the chosen directory that belong to the .xlsx filetype
files = glob.glob('./Assets/*.xlsx')

#Loops through the array of filenames and runs the main process for each one
if files != []: 
    for file in range(len(files)):
        if check(files[file]):
            next
        else: 
            instance = files[file] 
            formatted = instance + "\n"
            getData(files[file], file)
            append(formatted, instance)

else: 
    print("No Files")