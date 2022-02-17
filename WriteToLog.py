#Define function to read and write to the log
from openpyxl import Workbook, load_workbook
import glob
import csv
import logging

#Retreives all files in the chosen directory that belong to the .xlsx filetype
files = glob.glob('./Assets/*.xlsx')

#months dictionary used for extracting date values out of name identifiers
months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}



#Process derives the proper date formating and matches it to the applicable data
def getData(file, ind): 
    print(file)
    #Initiates the log file and location
    logging.basicConfig(filename='{}.txt'.format(ind),
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

    #workbook definitions and workpage definitions
    wp = load_workbook(file)
    
    wp1 = wp["Summary Rolling MoM"] 
    wp2 = wp["VOC Rolling MoM"]
    wp3 = wp["Monthly Verbatim Statements"]

    #Grabs first three characters in the month and the year, converts the month to a matchable counterpart
    month = file[32:35]
    month = month[0].upper() + month[1:]
    year = file[-9:-5]

    #Function searches through month array and returns the numerical value of a given month
    def monthMatch(month):
        for i in months:
            if i == month:
                return (months[month])
            else: pass

    #final iteration of the month added to the year for matching purposes
    formatted = year + "-" + monthMatch(month)

    #Creates the CSV file needed for reading
    def writeCSV(sheet, name):
        with open('./csv/{0}{1}.csv'.format(ind, name), 'w', newline="") as file_handle:
            csv_writer = csv.writer(file_handle)
            for row in sheet.iter_rows():
                try: 
                    csv_writer.writerow([cell.value for cell in row])
                except:
                    pass

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
                            logging.info(ele[index])
                        else:
                            logging.info('No data on sheet 2')
                            break

                if wp.active == wp3:
                    for line in csv_reader:
                        if line[0][0:7] == formatted:
                            for x in line:
                                logging.info(x)

    #Iterates for each workpage, reads and uploads the info to the log file.        
    if wp.active == wp1:
        writeCSV(wp1, "1")
        logging.debug('Sheet 1: Date, Call Count, "%" of abandons after 30s, "%" FCR, "%" DSAT, "%" CSAT')
        readCSV("1")
        logging.debug('')

    wp.active = wp2 

    if wp.active == wp2:
        writeCSV(wp2, "2")
        logging.debug('Sheet 2: Base Size, Promoters (number and percentage), Passives (number and percentage), Dectractors (number and percentage), AARP total "%" for (NPS"%", Agent"%", DSAT"%"')
        readCSV("2")
        logging.info('Sheet two finished processing')
        logging.debug('')

    wp.active = wp3
 
    if wp.active == wp3:
        writeCSV(wp3, "3")
        logging.debug('Sheet 3: Date, Itinerary Number, Additional feedback')
        readCSV("3")
        logging.info('Sheet three finished processing')
        logging.debug('')
    
#Iterates through all files and runs the program
for file in range(len(files)):
    getData(files[file], file)










