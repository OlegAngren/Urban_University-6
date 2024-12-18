import random


class Animal:
    """
    Базовый класс для описания животных.
    """

    live = True  # Все животные живые
    sound = None  # Звук животного, по умолчанию отсутствует
    _DEGREE_OF_DANGER = 0  # Степень опасности животного

    def __init__(self, speed: float):
        """
        Инициализация базового животного.

        Args:
            speed (float): Скорость передвижения животного.
        """
        self._cords = [0, 0, 0]  # Координаты животного в пространстве
        self.speed = speed  # Скорость передвижения

    def move(self, dx: float, dy: float, dz: float):
        """
        Перемещает животное по координатам с учетом скорости.

        Args:
            dx (float): Изменение по оси X.
            dy (float): Изменение по оси Y.
            dz (float): Изменение по оси Z.
        """
        # Проверка на допустимость изменения координаты Z
        if self._cords[2] + dz * self.speed < 0:
            print("It's too deep, i can't dive :(")
        else:
            # Изменяем координаты с учетом скорости
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] += dz * self.speed

    def get_cords(self):
        """
        Возвращает текущие координаты животного.
        """
        print(f"X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}")

    def attack(self):
        """
        Реакция животного при атаке.
        """
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        """
        Издает звук животного.
        """
        if self.sound:
            print(self.sound)
        else:
            print("This animal is silent.")


class Bird(Animal):
    """
    Класс для птиц, наследуется от Animal.
    """

    beak = True  # У птиц всегда есть клюв

    def lay_eggs(self):
        """
        Птица откладывает яйца.
        """
        eggs = random.randint(1, 4)  # Случайное количество яиц от 1 до 4
        print(f"Here are(is) {eggs} eggs for you")


class AquaticAnimal(Animal):
    """
    Класс для водных животных, наследуется от Animal.
    """

    _DEGREE_OF_DANGER = 3  # Водные животные немного опасны

    def dive_in(self, dz: float):
        """
        Погружение животного в воду.

        Args:
            dz (float): Глубина погружения.
        """
        dz = abs(dz)  # Всегда погружаемся вниз
        new_depth = self._cords[2] - dz * (self.speed / 2)
        if new_depth < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[2] = new_depth


class PoisonousAnimal(Animal):
    """
    Класс для ядовитых животных, наследуется от Animal.
    """

    _DEGREE_OF_DANGER = 8  # Ядовитые животные крайне опасны


class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    """
    Класс для утконоса, наследуется от Bird, AquaticAnimal и PoisonousAnimal.
    """

    sound = "Click-click-click"  # Звук утконоса

    def __init__(self, speed: float):
        """
        Инициализация утконоса.

        Args:
            speed (float): Скорость передвижения утконоса.
        """
        # Инициализируем базовый класс Animal (через Bird, первый в mro())
        super().__init__(speed)


# Проверяем программу

# Создаем утконоса с указанной скоростью
db = Duckbill(10)

# Утконос жив и у него есть клюв
print(db.live)  # True
print(db.beak)  # True

# Утконос издает звук и атакует
db.speak()  # Click-click-click
db.attack()  # Be careful, i'm attacking you 0_0

# Перемещаем утконоса
db.move(1, 2, 3)
db.get_cords()  # X: 10 Y: 20 Z: 30

# Утконос ныряет
db.dive_in(6)
db.get_cords()  # X: 10 Y: 20 Z: 0

# Утконос откладывает яйца
db.lay_eggs()  # Here are(is) <1-4> eggs for you


''' Объяснение кода:
1. Базовый класс Animal:

    Содержит основные атрибуты и методы для любого животного.
    Скрытые атрибуты (_cords, _DEGREE_OF_DANGER) предотвращают их прямое изменение.

2. Наследники Bird, AquaticAnimal, PoisonousAnimal:

    Каждый добавляет уникальные свойства и поведение.
    Bird: атрибут beak и метод для откладывания яиц.
    AquaticAnimal: метод dive_in для погружения.
    PoisonousAnimal: высокая степень опасности.

3. Класс Duckbill:

Наследуется от всех трех классов, что отражает особенности утконоса.
Порядок наследования важен, так как Bird идет первым в mro(). Это позволяет move() и speed корректно работать.

4. Особенности методов:

    move() и dive_in() проверяют координаты, чтобы предотвратить "слишком глубокое" погружение.
    Метод lay_eggs() демонстрирует наследование от класса Bird.

5. Результат:

    Утконос издает звук, атакует, перемещается, ныряет и откладывает яйца.'''