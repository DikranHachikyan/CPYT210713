from math import sqrt

class Point():
    # променлива на класа (статична)
    label = 'A'
    count = 0

    def __init__(self, x = 0, y = 0, *args, **kwargs):
        print('Point Ctor')
        # данни на обекта
        self.x = x
        self.y = y
        Point.label = 'B'
        Point.count += 1

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
    def __str__(self):
        return f'({self.x},{self.y})'

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        raise TypeError('Expected instance of Point')

    def __gt__(self, other):
        if not isinstance(other,Point):
            raise TypeError('Expected instance of Point')
        
        dx1 = self.x ** 2
        dy1 = self.y ** 2
        dist1 = sqrt(dx1 + dy1)
        
        dx2 = other.x ** 2
        dy2 = other.y ** 2
        dist2 = sqrt(dx2 + dy2)

        return dist1 > dist2    
    
    def __add__(self, other):
        if isinstance(other, Point):
            new_x = self.x + other.x
            new_y = self.y + other.y
        elif isinstance(other, (int, float)):
            new_x = self.x + other
            new_y = self.y + other
        else:
            raise TypeError('Expected instance of Point, int or float')

        return Point(new_x, new_y)
 
    def __del__(self):
        # destructor
        print('Object Dtor')
        Point.count -=1

print(f'module name:{__name__}')

if __name__ == '__main__':
    print(f'Test class Point')

    p1 = Point(10,20)

    p1.draw()

    p1.move_to(-5,2)

    p1.draw()