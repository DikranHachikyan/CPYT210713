from draw.point import Point

class Rectangle(Point):

    def __init__(self, x = 0, y = 0, width = 0, height = 0, *args, **kwargs):
        super().__init__(x,y) # констр. на родител  
        print('Rectangle Ctor')
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        assert width >= 0, 'width must be >= 0'
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        assert height >= 0, 'height must be >= 0'
        self.__height = height

    # Специални методи
    def __str__(self):
        point_str = super().__str__()
        return f'{point_str}[{self.width}x{self.height}]'

    def draw(self):
        super().draw()
        print(f'draw rectangle:[{self.width}x{self.height}]')


if __name__ == '__main__':
    
    rc = Rectangle(10,20,120,340)

    print(f'{rc}')

    rc.draw()
    rc.move_to(4,-7)
    rc.draw()
    print('---')