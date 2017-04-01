import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 只要程序处于活动状态就不断的模拟随机漫步
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk(50000)
    rw.fill_walk()
    # 设置绘图窗口的尺寸  放在描点之前
    plt.figure(figsize=(10,6))

    ponit_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_value,rw.y_value,c=ponit_numbers,cmap=plt.cm.Blues,edgecolor="none",s=2)
   
    # 突出起点和终点
    plt.scatter(0,0,c='green',edgecolor='none',s=50)
    plt.scatter(rw.x_value[-1],rw.y_value[-1],c='red',edgecolor='none',s=50)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()
    
    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break