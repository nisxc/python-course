import csv

with open('contacts.csv', newline='') as CSVFile:
    reader = csv.DictReader(CSVFile, fieldnames=['Name', 'Phone', 'f'])
    for row in reader:
        print(row['Name'], ':', row['Phone'], row['f'])
