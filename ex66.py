# 1.дефиниция на класа

class Point():

    def __init__(self, x = 0, y = 0, *args, **kwargs):
        print('Point Ctor')
        # данни на обекта
        self.x = x
        self.y = y

    # методи на обекта
    def draw(self):
        print(f'draw point at ({self.x}, {self.y})')

    def move_to(self, dx, dy):
        self.x += dx
        self.y += dy

    # getter
    @property
    def x(self):
        return self.__x

    # setter
    @x.setter
    def x(self,x):
        assert type(x) is int and x >= 0, 'x must be positive number'
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        assert type(y) is int and y >= 0, 'y must be positive number'
        self.__y = y

    # специални методи
    

if __name__ == '__main__':
    # 2. променлива (обект) от тип Point
    # клас - типа (Point), обект - представител на класа т.е. променливата 
    p1 = Point()
    p2 = Point(12,20)

    print(f'point ({p1.x}, {p1.y}) (getters)')

    p1.x = 14
    p1.y = 32

    p1.draw()
   

    print('---')