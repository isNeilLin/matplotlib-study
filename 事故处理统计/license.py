# 导入csv模块
import csv
# 导入转化省份全程的模块
from transform import transform

# 设置数据文件路径
filename = '事故数据.csv'
# 打开文件，编码格式设置为UTF8，忽略error
with open(filename,encoding='gb2312', errors='ignore') as f:
    # 读取csv
    reader = csv.reader(f)
    # 获取表头内容并跳过表头
    header_row = next(reader)
    # 定义存储车牌号的数组
    license = []
    for row in reader:
        license.append(row[6])
        license.append(row[9])

# 各个简写省份出现的次数
places = {}
for value in license:
    if places.get(value[0]):
        places[value[0]] += 1
    else:
        places[value[0]] = 1

# 根据各省份出现的次数进行排序
times = sorted(places.values(),reverse=True)
# 省份简拼的结果
results = []
for time in times:
    for key, val in places.items():
        if val == time and results.count({key:val})==0:
            results.append({key:val})

# # 打印省份简拼结果
for v in results:
    # 取到每个省份简拼
    key = list(v.keys())[0]
    print('省份简拼： '+key+' , 事故量： '+str(v[key]))

# 省份全称的结果
full_name_results = []
for obj in results:
    for key in obj.keys():
        if transform(key):
            full_name = transform(key)
            full_name_results.append({full_name:obj[key]})
        else:
            print(key,'简拼错误，没有查询到该省')

for v in full_name_results:
    # 取到每个省份简拼
    key = list(v.keys())[0]
    print('省份： '+key+' , 事故量： '+str(v[key]))
