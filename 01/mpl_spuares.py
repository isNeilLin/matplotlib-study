import matplotlib.pyplot as plt
inputValues = [1,2,3,4,5,6]
squares = [1,4,9,16,25,36]
plt.plot(inputValues,squares,linewidth=5)
# 设置图标标题，并给坐标轴加上标签
plt.title("Squares Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both',labelsize=14)
plt.show()