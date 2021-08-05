# 1.дефиниция на класа

class Point():

    def __init__(self, x = 0, y = 0, *args, **kwargs):
        print('Point Ctor')
        # данни на обекта
        self.__x = x
        self.__y = y

    # методи на обекта
    def draw(self):
        print(f'draw point at ({self.__x}, {self.__y})')

    def move_to(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def set_x(self, x):
        assert type(x) is int and x >= 0, 'x must be positive int'
        self.__x = x

    def get_x(self):
        return self.__x    
    
    def set_y(self, y):
        assert type(y) is int and y >= 0, 'y must be positive int'
        self.__y = y

    def get_y(self):
        return self.__y    

if __name__ == '__main__':
    # 2. променлива (обект) от тип Point
    # клас - типа (Point), обект - представител на класа т.е. променливата 
    p1 = Point()
    p2 = Point(12,20)
   
    # "private" и не са достъпни
    # print(f'Point ({p1.__x}, {p1.__y})')
    # p1.__x = -20
    # p1.__y = -20

    p1.set_x(-20)
    p1.set_y(30)

    p1.draw()
   

    print('---')