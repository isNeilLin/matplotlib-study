import matplotlib.pyplot as plt

x_values = list(range(1,6))
y_values = [x**3 for x in x_values]
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Greens,edgecolor="none",s=40)
# 设置图标标题并给坐标轴加上标签
plt.title("Squares of Number",fontsize=16)
plt.xlabel("Value",fontsize=12)
plt.ylabel("Squares of Value",fontsize=12)
# 设置刻度标记的大小
plt.tick_params(axis='both',which="major",labelsize=14)
# 设置每个坐标轴的取值范围
# plt.axis([0,1100,0,1100000])

# 自动保存图表为图片
plt.savefig('scatter.png',bbox_inches="tight")


