import glob
from WriteToLog import getData
from processChecker import append, check, fil

#Retreives all files in the chosen directory that belong to the .xlsx filetype
files = glob.glob('./Assets/*.xlsx')


if files != []: 
    for file in range(len(files)):
        if check(files[file]):
            pass
        else: 
            instance = files[file] + "\n"
            getData(files[file], file)
            append(instance)

else: 
    print("No Files")