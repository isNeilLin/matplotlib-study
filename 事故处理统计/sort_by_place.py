# 导入csv模块
import csv

# 设置数据文件路径
filename = '事故数据.csv'
# 打开文件，编码格式设置为UTF8，忽略error
with open(filename,encoding='gb2312', errors='ignore') as f:
    # 读取csv
    reader = csv.reader(f)
    # 获取表头内容并跳过表头
    header_row = next(reader)
    # 定义存储地址的数组
    places = []
    for row in reader:
        places.append(row[1])

# 对地址根据出现的次数进行归类
sorted_data = {}
for place in places:
    if sorted_data.get(place):
        sorted_data[place] += 1
    else:
        sorted_data[place] = 1

# 根据各地址出现的次数进行排序
# 全部数据很大，处理起来较慢。这里截取了事故量频发地址前1000处。如果需要全部的数据可以把[:1000]给去掉
times = sorted(sorted_data.values(),reverse=True)[:1000]

# 地址按出现频次排序后的结果
results = []
for time in times:
    for key, val in sorted_data.items():
        if val == time and results.count({key:val})==0:
            results.append({key:val})

# 打印结果
for v in results:
    # 取到每个对应的地址
    key = list(v.keys())[0]
    print('事故地址： '+key+' , 发生的频次 '+str(v[key]))
