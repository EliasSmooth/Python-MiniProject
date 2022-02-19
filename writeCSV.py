import csv

#Creates the CSV file needed for reading
def writeCSV(sheet, name, ind):
        with open('./csv/{0}{1}.csv'.format(ind, name), 'w', newline="") as file_handle:
            csv_writer = csv.writer(file_handle)
            for row in sheet.iter_rows():
                try: 
                    csv_writer.writerow([cell.value for cell in row])
                except:
                    pass

