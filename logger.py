import logging
import os


formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

def setup_logger(name, log_file, level=logging.INFO):
    """reusable function to create logfiles"""
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)
    
    
    logger = logging.getLogger(name)
    
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

def delete_log(ind):
    """takes in the file process number and removes the respective log"""
    try:
        os.remove('./logs/{}_logfile.log'.format(ind))
    except:
        exit