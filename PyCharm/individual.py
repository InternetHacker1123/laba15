#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


# Объявляем функцию для вычисления площади круга
def calculate_circle_area(radius):
    return math.pi * radius**2


# Объявляем декоратор для вывода сообщения
def print_circle_area_message(func):
    def wrapper(radius):
        result = func(radius)
        print(f"Площадь круга равна = {result}")
    return wrapper


# Применяем декоратор к функции
decorated_calculate_circle_area = print_circle_area_message(
    calculate_circle_area)

if __name__ == '__main__':
    decorated_calculate_circle_area(5)
