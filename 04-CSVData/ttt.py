import csv
from datetime import datetime

filename = './csv/事故数据.csv'
with open(filename,encoding='utf-8', errors='ignore') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates = [row[0] for row in reader]
    data = {}
    for date in dates:
        date = date.split('-')
        month = int(date[1])
        if data.get(month):
            data[month].append(date)
        else:
            data[month] = [date]

months = list(range(1,13))
for month in months:
    print(len(data[month]))
            
       



    