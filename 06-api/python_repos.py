import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status Code: ', r.status_code)

# 将API响应存储在一个变量中
response = r.json()
print('Total repositories: ', response['total_count'])

# 有关仓库的信息
repos = response['items']
print('Repositories returned: ',len(repos))

print('selected information about first repositories: ')
# for repo in repos:
#     print('\nName:', repo['name'])
#     print('Owner:', repo['owner']['login'])
#     print('Stars:', repo['stargazers_count'])
#     print('Repository:', repo['html_url'])
#     print('Description:', repo['description'])

names, plot_dicts = [], []
for repo in repos:
    names.append(repo['name'])
    
    plot_dicts.append({
        'value':repo['stargazers_count'],
        'label':repo['description'],
        'xlink':repo['html_url']
    })

# 可视化
mystyle = LS('#333366',base_style=LCS)
myconfig = pygal.Config()
myconfig.x_label_rotation = 45
myconfig.show_legend = False
myconfig.title_font_size = 20
myconfig.label_font_size = 14
myconfig.major_label_font_size = 18
myconfig.truncate_label = 15  # 将较长的项目名缩 为15个字符
myconfig.show_y_guides = False
myconfig.width = 1000

chart = pygal.Bar(myconfig,style=mystyle)
chart.title = 'Most-Starred Python Projects on Github'
chart.add('',plot_dicts)
chart.render_to_file('python_repos.svg')