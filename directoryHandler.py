import os

def fileHandle(file):
    """Moves files from Assets dir to Archive dir after processing"""
    filename = file[9:]

    os.replace('./Assets/{}'.format(filename), './Archive/{}'.format(filename))
