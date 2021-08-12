# 1.

import draw.point as dp


if __name__ == '__main__':
    # 2. променлива (обект) от тип Point
    print(f'Point n inst. {dp.Point.count}')
    
    p1 = dp.Point(4,6)
    print(f'{p1} (n inst. {p1.count})')

    p2 = dp.Point(4,6)
    print(f'{p2} (n inst. {p2.count})')
    
    del p1

    print(f'Point n inst. {dp.Point.count}')
    print('---')