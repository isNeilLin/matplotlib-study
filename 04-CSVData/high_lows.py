import csv
from matplotlib import pyplot as plt
from datetime import datetime

file = './csv/death_valley_2014.csv'
with open(file) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # 从文件中获取最高气温
    highs,dates,lows = [], [], []
    for row in reader:
        try:
            date = datetime.strptime(row[0],"%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(date,'missing data')
        else:
            highs.append(high)
            dates.append(date)
            lows.append(low)

# 根据数据绘制图形
fig = plt.figure(figsize=(10,6))
plt.plot(dates,highs,c='r',alpha=0.5)
plt.plot(dates,lows,c='b',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='b',alpha=0.2)
# # 设置图形的格式
plt.title('Daily high and low temperatures-2014',fontsize=16)
plt.xlabel('',fontsize=12)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)',fontsize=12)
plt.tick_params(axis='both',which='major',labelsize=20)
plt.show()

