import glob
import logging

from WriteToLog import getData
from processChecker import append, check
from logger import setup_logger


#Retreives all files in the chosen directory that belong to the .xlsx filetype
files = glob.glob('./Assets/*.xlsx')


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