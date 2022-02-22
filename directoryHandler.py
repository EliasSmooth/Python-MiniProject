from fileinput import filename
import os

def fileHandle(file):
    """Moves files from Assets dir to Archive dir after processing"""
    filename = file[9:]

    os.replace('./Assets/{}'.format(filename), './Archive/{}'.format(filename))

def fileError(file):
    """Moves file to the error directory"""
    filename = file[9:]
    try: 
        os.replace('./Assets/{}'.format(filename), './Error/{}'.format(filename))
        print("ERROR: Improper file name")
    except:
        pass

def worksheetError(file, ins):
    """Moves file with worksheet error to error directory"""
    filename = file[9:]

    try: 
        os.replace('./Assets/{}'.format(filename), './Error/{}'.format(filename))
        print('ERROR: Worksheet Error on file {}'.format(ins))
    except: 
        pass