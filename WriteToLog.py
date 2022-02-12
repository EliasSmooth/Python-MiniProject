#Define function to read and write to the log
from fnmatch import fnmatch
from openpyxl import Workbook, load_workbook
import glob
import csv

files = glob.glob('./Assets/*.xlsx')

sumdata = []
vocdata = []
monthdata = []

months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}

#Creates the CSV file needed for reading
def writeCSV(sheet, name):
    with open('{}.csv'.format(name), 'w', newline="") as file_handle:
        csv_writer = csv.writer(file_handle)
        for row in sheet.iter_rows():
            try: 
                csv_writer.writerow([cell.value for cell in row])
            except:
                pass


#Process derives the proper date formating and matches it to the applicable data
def getData(file): 
    wp = load_workbook(file)
    wp1 = wp["Summary Rolling MoM"] 
    wp2 = wp["VOC Rolling MoM"]
    wp3 = wp["Monthly Verbatim Statements"]

    month = file[32:35]
    month = month[0].upper() + month[1:]
    year = file[38:42]

    def monthMatch(month):
        for i in months:
            if i == month:
                return (months[month])
            else: pass

    formatted = year + "-" + monthMatch(month)

    def readCSV(number):
            with open("{}.csv".format(number), 'r') as csv_file:
                csv_reader = csv.reader(csv_file, dialect="excel")
                if wp.active == wp1:
                    for line in csv_reader:
                        if line[0][0:7] == formatted:
                            print("sucess")
                            for x in line:
                                if x != '' or 0:
                                    sumdata.append(x)
                                    print(sumdata)
                if wp.active == wp2:
                    for line in csv_reader:          
                        for x in line[0]:
                            var = x[0:7]
                            if var == formatted:       
                                vocdata.append(line[x])
                if wp.active == wp3:
                    for line in csv_reader:
                        if line[0][0:7] == formatted:
                            for x in line:
                                monthdata.append(x)
                        
                            

    if wp.active == wp1:
        writeCSV(wp1, "1")
        readCSV("1")

    wp.active = wp2 

    if wp.active == wp2:
        writeCSV(wp2, "2")
        readCSV("2")
        
    wp.active = wp3
 
    if wp.active == wp3:
        writeCSV(wp3, "3")
        readCSV("3")

    

    #Next process processes the excel and turns it into iterable CSV
    



for file in files:
    getData(file)





