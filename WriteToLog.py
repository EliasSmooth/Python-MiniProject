#Define function to read and write to the log
from openpyxl import load_workbook

import csv
import logging
import sys

from writeCSV import writeCSV
from monthMatch import monthMatch
from logger import setup_logger, delete_log
from directoryHandler import worksheetError

def getData(file, ind): 
    #deletes the previous log
    delete_log(ind)

    #Initiates the log file and location
    setup_logger('{}_logger'.format(ind), './logs/{}_logfile.log'.format(ind))

    #Logger variable for writing
    logger = logging.getLogger('{}_logger'.format(ind))

    #workbook definitions and workpage definitions
    wp = load_workbook(file)

    wp1 = ""
    wp2 = ""
    
    try: 
        wp1 = wp["Summary Rolling MoM"] 
        wp2 = wp["VOC Rolling MoM"]
    except:
        worksheetError(file, ind)
        logger.info('Missing Worksheet')
        

    #Grabs first three characters in the month and the year, converts the month to a matchable counterpart
    month = file[32:35]
    month = month[0].upper() + month[1:]
    year = file[-9:-5]

    #final iteration of the month added to the year for matching purposes

    formatted = year + "-" + monthMatch(month)

    #reusable function that takes in the number of the worksheet and reads the generated CSV from the function above.
    def readCSV(number):
        with open("./csv/{0}{1}.csv".format(ind, number), 'r') as csv_file:
            csv_reader = csv.reader(csv_file, dialect="excel")
                
            if wp.active == wp1:
                for line in csv_reader:
                    if line[0][0:7] == formatted: 
                        for x in line:
                            if x != '' or 0:
                                logger.info(x)
                    
            if wp.active == wp2:
                index = 0
                for line,ele in enumerate(csv_reader):
                    if line == 0:
                        for item,n in enumerate(ele):
                                if n[0:7] == formatted:
                                    index = item  
                                elif n[0:3] == month:
                                    index = item
                    if index != 0:
                        if "." in ele[index]:
                            next
                        else:
                            try:
                                #transforms value to int for comparison operators
                                proper = int(ele[index])
                                #Prints proper data and rating for each datapoint on sheet 2
                                if proper and line == 2:
                                    logger.info("Base Size: " + ele[index]) 
                                
                                if proper > 200 and line == 3: 
                                    logger.info(ele[index] + " - Good Promoters")
                                elif proper < 200 and line == 3:
                                    logger.info(ele[index] + " - Bad Promoters")

                                if proper > 100 and line == 5:
                                    logger.info(ele[index] + " - Good Passives")
                                elif proper < 100 and line == 5:
                                    logger.info(ele[index] + " - Bad Passives")

                                if proper > 100 and line == 7: 
                                    logger.info(ele[index] + " - Good Dectrators")
                                elif proper < 100 and line == 7:
                                    logger.info(ele[index] + " - Bad Dectrators")
                                
                            except: 
                                pass      
                    else:
                        logger.info('No data on sheet 2')
                        break

    #Iterates for each workpage, reads and uploads the info to the log file.        
    if wp.active == wp1:
        writeCSV(wp1, "1", ind)
        logger.info('Sheet 1: Date, Call Count, "%" of abandons after 30s, "%" FCR, "%" DSAT, "%" CSAT')
        readCSV("1")
        logger.info('Sheet one finished processing')
        logger.info('')

    try:
        wp.active = wp2 
    except: 
        pass

    if wp.active == wp2:
        writeCSV(wp2, "2", ind)
        logger.info('Sheet 2: Base Size, Promoters, Passives, Dectractors')
        readCSV("2")
        logger.info('Sheet two finished processing')


    
#Iterates through all files and runs the program











