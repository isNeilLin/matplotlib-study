import pygal
from die import Die

die_1 = Die()
die_2 = Die(10)

# 随机掷几次骰子，将结果存储在list中
results = [die_1.roll() + die_2.roll() for roll in range(5000)]

#分析结果
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2,max_result+1)]

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"
x_labels = list(range(2,17))
hist.x_labels = x_labels
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6+D10',frequencies)
hist.render_to_file('die.svg')