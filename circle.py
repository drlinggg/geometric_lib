import math


def area(r):
    '''Принимает положительное число r, возвращает площадь круга'''
    if r <= 0:
        return -1
    return math.pi * r * r


def perimeter(r):
    '''Принимает положительное число r, возвращает периметр круга'''
    if r <= 0:
        return -1
    return 2 * math.pi * r

