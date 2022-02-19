import os

fil = open('./Archive/files.txt', "w")

filesize = os.path.getsize("./Archive/files.txt")

def append(file): 
    fil.write(file)

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
    