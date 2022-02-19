#Define function to read and write to the log
from errno import errorcode
from openpyxl import load_workbook

import csv
import logging

from writeCSV import writeCSV
from monthMatch import monthMatch
from processChecker import append, check
from logger import setup_logger

def getData(file, ind): 
    #workbook definitions and workpage definitions
    wp = load_workbook(file)
    
    wp1 = wp["Summary Rolling MoM"] 
    wp2 = wp["VOC Rolling MoM"]

    #Grabs first three characters in the month and the year, converts the month to a matchable counterpart
    month = file[32:35]
    month = month[0].upper() + month[1:]
    year = file[-9:-5]

    #final iteration of the month added to the year for matching purposes
    formatted = year + "-" + monthMatch(month)

    #Initiates the log file and location
    setup_logger('{}_logger'.format(ind), './logs/{}_logfile.log'.format(ind))

    #Logger variable for writing
    logger = logging.getLogger('{}_logger'.format(ind))

    #reusable function that takes in the number of the worksheet and reads the generated CSV from the function above.
    def readCSV(number):
        with open("./csv/{0}{1}.csv".format(ind, number), 'r') as csv_file:
            csv_reader = csv.reader(csv_file, dialect="excel")
                
            if wp.active == wp1:
                process = True
                for line in csv_reader:
                    if line[0][0:7] == formatted: 
                        for x in line:
                            if x != '' or 0:
                                logger.info(x)
                            if process:
                                logger.info('Sheet one finished processing')
                                process = False
                    
            if wp.active == wp2:
                index = 0
                for line,ele in enumerate(csv_reader):
                    print(ele)
                    if line == 0:
                        for item,n in enumerate(ele):
                            if n[0:7] == formatted:
                                index = item  
                    if index != 0:
                        if "." in ele[index]:
                            continue
                        else:
                            try:
                                if int(ele[index]) > 200 and line == [2]:
                                    logger.info("Base Size " + ele[index]) 
                                else: 
                                    logger.info(ele[index] + " Bad Score")
                            except: 
                                pass      
                    else:
                        logger.info('No data on sheet 2')
                        break

    #Iterates for each workpage, reads and uploads the info to the log file.        
    if wp.active == wp1:
        writeCSV(wp1, "1", ind)
        logger.debug('Sheet 1: Date, Call Count, "%" of abandons after 30s, "%" FCR, "%" DSAT, "%" CSAT')
        readCSV("1")
        logger.debug('')

    wp.active = wp2 

    if wp.active == wp2:
        writeCSV(wp2, "2", ind)
        logger.debug('Sheet 2: Base Size, Promoters (number and percentage), Passives (number and percentage), Dectractors (number and percentage), AARP total "%" for (NPS"%", Agent"%", DSAT"%"')
        readCSV("2")
        logger.info('Sheet two finished processing')
        logger.debug('')


    
#Iterates through all files and runs the program











