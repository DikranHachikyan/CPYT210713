# 1.
# import draw.point as dp
# 
#  p1 = dp.Point()


# 2.
from draw.point import Point
# p2 = Point()

# 2.1 
# from draw.point import Point as P

# p2 = P(1,2)

if __name__ == '__main__':
    # 2. променлива (обект) от тип Point
    print(f'Point n inst. {Point.count}')
    
    p1 = Point(4,6)
    print(f'{p1} (n inst. {p1.count})')

    p2 = Point(4,6)
    print(f'{p2} (n inst. {p2.count})')
    
    del p1

    print(f'Point n inst. {Point.count}')
    print('---')