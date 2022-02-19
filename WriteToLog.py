#Define function to read and write to the log
from errno import errorcode
from openpyxl import load_workbook

import csv
import logging

from writeCSV import writeCSV
from monthMatch import monthMatch
from processChecker import append, check

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
    logging.basicConfig(filename='./logs/{}.txt'.format(formatted),
                            filemode='w',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

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
                                logging.info(x)
                            if process:
                                logging.info('Sheet one finished processing')
                                process = False
                    
            if wp.active == wp2:
                index = 0
                for line,ele in enumerate(csv_reader):

                    if line == 0:
                        for item,n in enumerate(ele):
                            if n[0:7] == formatted:
                                index = item  
                    if index != 0:
                        if "." in ele[index]:
                            continue
                        else:
                            try:
                                if int(ele[index]) > 200:
                                    logging.info(ele[index] + " Good Score") 
                                else: 
                                    logging.info(ele[index] + " Bad Score")
                            except: 
                                pass      
                    else:
                        logging.info('No data on sheet 2')
                        break

    #Iterates for each workpage, reads and uploads the info to the log file.        
    if wp.active == wp1:
        writeCSV(wp1, "1", ind)
        logging.debug('Sheet 1: Date, Call Count, "%" of abandons after 30s, "%" FCR, "%" DSAT, "%" CSAT')
        readCSV("1")
        logging.debug('')

    wp.active = wp2 

    if wp.active == wp2:
        writeCSV(wp2, "2", ind)
        logging.debug('Sheet 2: Base Size, Promoters (number and percentage), Passives (number and percentage), Dectractors (number and percentage), AARP total "%" for (NPS"%", Agent"%", DSAT"%"')
        readCSV("2")
        logging.info('Sheet two finished processing')
        logging.debug('')


    
#Iterates through all files and runs the program











