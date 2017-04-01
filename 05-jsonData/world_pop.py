import json
from pygal.maps.world import World
from pygal.style import RotateStyle as RS, LightColorizedStyle as LS
from country_code import get_country_code
# 将数据加载到一个列表中
with open('population_data.json') as f:
    pop_data = json.load(f)

# 创建一个包含人口数量的字典
world_populations = {}
# 打印每个国家2010年的人口
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            world_populations[code] = population
# 根据人口数量，将所有国家分成三组
pop1, pop2, pop3 = {}, {}, {}
for code, population in world_populations.items():
    if population < 10000000:
        pop1[code] = population
    elif population < 1000000000:
        pop2[code] = population
    else:
        pop3[code] = population

wm_style = RS('#336699',base_style=LS)
wm = World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m',pop1)
wm.add('10m-10bn',pop2)
wm.add('>10bn',pop3)
wm.render_to_file('world_population.svg')
