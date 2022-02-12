#Define function to read and write to the log
import openpyxl
import glob
import csv

files = glob.glob('./Assets/*.xlsx')
data = []

months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}

#Creates the CSV file needed for reading
def writeCSV(sheet):
    with open('test.csv', 'w', newline="") as file_handle:
        csv_writer = csv.writer(file_handle)
        for row in sheet.iter_rows(): 
            csv_writer.writerow([cell.value for cell in row])

#Process derives the proper date formating and matches it to the applicable data
def getData(file): 
    wb = openpyxl.load_workbook(file)
    sh = wb.active
    
    month = file[32:35]
    month = month[0].upper() + month[1:]

    def monthMatch(month):
        for i in months:
            if i == month:
                return (months[month])
            else: pass

    year = file[38:42]
    formatted = year + "-" + monthMatch(month)

    writeCSV(sh)

    #Next process processes the excel and turns it into iterable CSV
    with open("test.csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file, dialect="excel")
        for line in csv_reader:
            print(line[0][0:7])
            if line[0][0:7] == formatted:
                print("sucess")
                for x in line:
                    if x != '' or 0:
                        data.append(x)
                        print(data)



for file in files:
    getData(file)





