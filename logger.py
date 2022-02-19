import logging
import os
import glob

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

def setup_logger(name, log_file, level=logging.INFO):

    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)
    
    
    logger = logging.getLogger(name)
    
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

def delete_log(ind):
    try:
        os.remove('./logs/{}_logfile.log'.format(ind))
    except:
        exit