# 1.дефиниция на класа

class Point():

    def __init__(self):
        print('Point Ctor')
        # данни на обекта
        self.x = 10
        self.y = 20

    # методи на обекта
    def draw(self):
        print(f'draw point at ({self.x}, {self.y})')


if __name__ == '__main__':
    # 2. променлива (обект) от тип Point
    # клас - типа (Point), обект - представител на класа т.е. променливата 
    p = Point()
   
    print(f'Point: ({p.x}, {p.y})')

    p.draw()
    print('---')