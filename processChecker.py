import os

from directoryHandler import fileHandle

fil = open('./Archive/files.txt', 'w')


filesize = os.path.getsize("./Archive/files.txt")

def append(formatted, instance): 
    #writes filename in doc
    fil.write(formatted)
    fileHandle(instance)
                

def check(file):
    if filesize == 0:
        exit
    else:
        for line in fil:
            if line:
                if file in line:
                    return True
                    break
            else:
                pass
    