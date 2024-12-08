import math


class Figure:
    """
    Базовый класс для геометрических фигур.
    """

    sides_count = 0  # Количество сторон (по умолчанию 0)

    def __init__(self, color, *sides):
        """
        Инициализация фигуры.

        Args:
            color (tuple): Цвет фигуры в формате RGB.
            sides (int): Стороны фигуры.
        """
        # Проверка корректности сторон при создании объекта
        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count  # Устанавливаем единичные стороны
        else:
            self.__sides = list(sides)

        self.__color = list(color)  # Устанавливаем цвет
        self.filled = False  # Фигура не закрашена по умолчанию

    def __is_valid_color(self, r, g, b):
        """
        Проверка корректности цвета.

        Args:
            r, g, b (int): Компоненты цвета.

        Returns:
            bool: True, если цвет корректен, иначе False.
        """
        return all(isinstance(val, int) and 0 <= val <= 255 for val in (r, g, b))

    def set_color(self, r, g, b):
        """
        Устанавливает новый цвет для фигуры.

        Args:
            r, g, b (int): Компоненты цвета.
        """
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            print("Invalid color. The color was not changed.")

    def get_color(self):
        """
        Возвращает текущий цвет фигуры.

        Returns:
            list: Цвет фигуры в формате RGB.
        """
        return self.__color

    def __is_valid_sides(self, *new_sides):
        """
        Проверка корректности новых сторон.

        Args:
            new_sides (int): Новые стороны.

        Returns:
            bool: True, если стороны корректны, иначе False.
        """
        return (
                len(new_sides) == self.sides_count
                and all(isinstance(side, int) and side > 0 for side in new_sides)
        )

    def set_sides(self, *new_sides):
        """
        Устанавливает новые стороны фигуры.

        Args:
            new_sides (int): Новые стороны.
        """
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        else:
            print("Invalid sides. The sides were not changed.")

    def get_sides(self):
        """
        Возвращает текущие стороны фигуры.

        Returns:
            list: Стороны фигуры.
        """
        return self.__sides

    def __len__(self):
        """
        Возвращает периметр фигуры (сумму сторон).

        Returns:
            int: Периметр фигуры.
        """
        return sum(self.__sides)


class Circle(Figure):
    """
    Класс для круга.
    """

    sides_count = 1  # У круга одна сторона (длина окружности)

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.__calculate_radius()

    def __calculate_radius(self):
        """
        Рассчитывает радиус круга по длине окружности.

        Returns:
            float: Радиус круга.
        """
        circumference = self.get_sides()[0]  # Длина окружности
        return circumference / (2 * math.pi)

    def get_square(self):
        """
        Возвращает площадь круга.

        Returns:
            float: Площадь круга.
        """
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    """
    Класс для треугольника.
    """

    sides_count = 3  # У треугольника три стороны

    def get_square(self):
        """
        Рассчитывает площадь треугольника по формуле Герона.

        Returns:
            float: Площадь треугольника.
        """
        a, b, c = self.get_sides()
        s = sum(self.get_sides()) / 2  # Полупериметр
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cube(Figure):
    """
    Класс для куба.
    """

    sides_count = 12  # У куба 12 рёбер

    def __init__(self, color, *sides):
        """
        Инициализация куба.

        Args:
            color (tuple): Цвет в формате RGB.
            sides (int): Ребро куба.
        """
        if len(sides) == 1:
            sides = [sides[0]] * self.sides_count
        super().__init__(color, *sides)

    def get_volume(self):
        """
        Рассчитывает объём куба.

        Returns:
            float: Объём куба.
        """
        side = self.get_sides()[0]  # Все рёбра одинаковы
        return side ** 3


# Тестирование классов

circle1 = Circle((200, 200, 100), 10)  # Цвет и длина окружности
cube1 = Cube((222, 35, 130), 6)  # Цвет и длина ребра

# Проверка изменения цветов
circle1.set_color(55, 66, 77)  # Корректный цвет
print(circle1.get_color())  # [55, 66, 77]

cube1.set_color(300, 70, 15)  # Некорректный цвет
print(cube1.get_color())  # [222, 35, 130]

# Проверка изменения сторон
cube1.set_sides(5, 3, 12, 4, 5)  # Некорректное количество сторон
print(cube1.get_sides())  # [6, 6, 6, ..., 6]

circle1.set_sides(15)  # Корректная длина окружности
print(circle1.get_sides())  # [15]

# Периметр (длина окружности)
print(len(circle1))  # 15

# Объём куба
print(cube1.get_volume())  # 216


''' Объяснение кода: 
1. Класс Figure:

    Общий для всех фигур, отвечает за работу с цветом и сторонами.
    Инкапсуляция защищает важные атрибуты (__color, __sides).
    Методы set_color, set_sides проверяют корректность входных данных.

2. Классы-наследники:

    Circle:
        Рассчитывает радиус на основе длины окружности.
        Метод get_square возвращает площадь круга.
    Triangle:
        Метод get_square использует формулу Герона.
    Cube:
        Инициализирует список сторон с одинаковыми значениями.
        Метод get_volume рассчитывает объём куба.

3. Проверки:

    Данные корректно обрабатываются на всех этапах.
    Некорректные значения не меняют атрибуты объектов.'''