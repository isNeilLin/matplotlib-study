from random import choice

class RandomWalk():
    """ 一个生成随机漫步数据的类 """
    def __init__(self,num_points=5000):
        """ 初始化随机漫步的属性 """
        self.num_points = num_points
        # 所有随机漫步都始于(0,0)
        self.x_value = [0]
        self.y_value = [0]
    def fill_walk(self):
        while len(self.x_value) < self.num_points:
            distance = list(range(0,9))
            x_step = self.get_step(distance)
            y_step = self.get_step(distance)

            # 拒绝原地踏步
            if x_step==0 and y_step==0:
                continue
            
            next_x = self.x_value[-1] + x_step;
            next_y = self.y_value[-1] + y_step;
            self.x_value.append(next_x)
            self.y_value.append(next_y)

    def get_step(self,distance=[0,1,2,3,4]):
        # 决定前进方向以及沿这个方向前进的距离
        direction = choice([1,-1])
        distance = choice(distance)
        step = direction * distance
        return step