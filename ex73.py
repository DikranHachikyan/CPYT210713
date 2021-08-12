from draw.point import Point

from draw.rectangle import Rectangle
from draw.point import Point


if __name__ == '__main__':
    
    shapes = [Point(2,5), Rectangle(3,5,100,200), Point(8,9)]

    for s in shapes:
        s.draw()
        print('---' * 10)

    print('---')