# 导入csv模块
import csv
# 导入pygal图标绘制库（第三方库，安装方式: pip3 install pygal ）
import pygal
# 导入正则表达式模块
import re

# 创建正则表达式的实例
pattern = re.compile(r'(.*\s)(\d+):')

# 设置数据文件路径
filename = '事故数据.csv'
# 打开文件，编码格式设置为UTF8，忽略error
with open(filename,encoding='utf-8', errors='ignore') as f:
    # 读取csv
    reader = csv.reader(f)
    # 获取表头内容并跳过表头
    header_row = next(reader)
    # 获取第一列的，即时间列
    dates = [row[0] for row in reader]
    # 创建存储结果的字典
    data,hourdata = {}, {}
    """
        最后data的结果应该是像如下的结构:
        data = {
            1: ['2015-01-12 12:30:12','2015-01-22 12:30:12','2015-01-16 16:30:12',...],
            2: ['2015-02-12 12:30:12','2015-02-22 12:30:12','2015-02-16 16:30:12',...],
            3: ['2015-03-12 12:30:12','2015-03-22 12:30:12','2015-03-16 16:30:12',...],
            4: ['2015-04-12 12:30:12','2015-04-22 12:30:12','2015-04-16 16:30:12',...],
            5: ['2015-05-12 12:30:12','2015-05-22 12:30:12','2015-05-16 16:30:12',...],
            6: ['2015-06-12 12:30:12','2015-06-22 12:30:12','2015-06-16 16:30:12',...],
            7: ['2015-07-12 12:30:12','2015-07-22 12:30:12','2015-07-16 16:30:12',...],
            8: ['2015-08-12 12:30:12','2015-08-22 12:30:12','2015-08-16 16:30:12',...],
            9: ['2015-09-12 12:30:12','2015-09-22 12:30:12','2015-09-16 16:30:12',...],
            10: ['2015-10-12 12:30:12','2015-10-22 12:30:12','2015-10-16 16:30:12',...],
            11: ['2015-11-12 12:30:12','2015-11-22 12:30:12','2015-11-16 16:30:12',...],
            12: ['2015-12-12 12:30:12','2015-12-22 12:30:12','2015-12-16 16:30:12',...]
        }
    """
    # 遍历所有的时间
    for date in dates:
        # 获取当前时间月份
        mdate = date.split('-')
        # 得到正则表达式的匹配
        match = pattern.match(date)
        month = int(mdate[1])
        # 截取到小时
        hour = int(match.groups()[1])
        # 如果字典中存在当前月份,则向改月份对应的数组追加数据
        if data.get(month):
            data[month].append(date) 
        # 如果不存在当前月份，则创建该月份并将该月份添加到对应的数组里
        else:
            data[month] = [date]  
         
        if hourdata.get(hour):
            hourdata[hour].append(date)
        else:
            hourdata[hour] = [date]

# 生成一个从1到12的数组
months = list(range(1,13))
hours = list(range(0,24))
# 生成一个1月到12月事故量的数组
month_results = [len(value) for value in data.values()]
hour_results = [len(value) for value in hourdata.values()]
# 创建pygal折线图的实例
m_hist = pygal.Line()
h_hist = pygal.Line()
# 添加图表标题
m_hist.title = '贵阳市2015各月份事故量'
h_hist.title = '贵阳市2015各时间段事故量'
# 添加横坐标
m_hist.x_labels = months
h_hist.x_labels = hours
# 添加对应数据
m_hist.add('月份', month_results)
h_hist.add('小时', hour_results)
# 生成svg文件
m_hist.render_to_file('month.svg')
h_hist.render_to_file('hour.svg')
""" 将svg文件直接拖进浏览器就可以打开 """
            
       



    