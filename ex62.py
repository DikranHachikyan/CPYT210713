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

if __name__ == '__main__':
    # 2. променлива (обект) от тип Point
    # клас - типа (Point), обект - представител на класа т.е. променливата 
    p1 = Point()
    p2 = Point(12,20)
   
    print(f'Point: ({p1.x}, {p1.y})')
    p1.draw()
    p2.draw()
    p2.move_to(-5, 10)
    p2.draw()

    print('---')