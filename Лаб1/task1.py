# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class LapTop:
    '''
    Класс описывает модель ноутбука
    '''
    def __init__(self, brand: str, model: str, SSD: int):
        '''
        Инициализация экземпляров класса

        :param brand: Марка ноутбука
        :param model: Модель ноутбука
        :param SSD: Объем памяти

        Пример:
        >>> my_laptop = LapTop('Apple', 'MacBook Pro', 512)
        '''
        if not isinstance(brand, str):
            raise TypeError('Марка ноутбука должна быть типа str')
        self.brand = brand
        if not isinstance(model, str):
            raise TypeError('Модель ноутбука должна быть типа str')
        self.model = model
        if not isinstance(SSD, int):
            raise TypeError('Объем памяти ноутбука должен быть целым числом')
        if SSD<0:
            raise ValueError('Объем памяти ноутбука должен быть положительным числом')
        self.SSD = SSD

    def cost(self) -> int:
        '''
        Метод рассчитывает стоимость ноутбука по его параметрам

        :return: Стоимость ноутбука

        Пример:
        >>> my_laptop = LapTop('Apple', 'MacBook Pro', 512)
        >>> my_laptop_cost = my_laptop.cost()
        '''
        ...

    def os(self) -> str:
        '''
        Метод возвращает ОС ноутбука

        :return: ОС ноутбука

        Пример:
        >>> my_laptop = LapTop('Apple', 'MacBook Pro', 512)
        >>> my_laptop_OS = my_laptop.os()
        '''
        ...

    def has_camera(self) -> bool:
        '''
        Метод определяет наличие встроенной камеры в ноутбуке

        :return: Наличие камеры

        Пример:
        >>> my_laptop = LapTop('Apple', 'MacBook Pro', 512)
        >>> my_laptop_cam = my_laptop.has_camera()
        '''
        ...

class Phone:
    '''
    Класс описывает модель телефона
    '''
    def __init__(self, brand: str, model: str, memory: int):
        '''
        Инициализация экземпляров класса

        :param brand: Марка телефона
        :param model: Модель телефона
        :param memory: Объем памяти

        Пример:
        >>> my_phone = Phone('Apple', 'Iphone 15', 512)
        '''

        if not isinstance(brand, str):
            raise TypeError('Марка телефона должна быть типа str')
        self.brand = brand
        if not isinstance(model, str):
            raise TypeError('Модель телефона должна быть типа str')
        self.model = model
        if not isinstance(memory, int):
            raise TypeError('Объем памяти телефона должен быть целым числом')
        if memory < 0:
            raise ValueError('Объем памяти телефона должен быть положительным числом')
        self.memory = memory

    def cost(self) -> int:
        '''
        Метод рассчитывает стоимость телефона по его параметрам

        :return: Стоимость телефона

        Пример:
        >>> my_phone = Phone('Apple', 'Iphone 15', 512)
        >>> my_phone_cost = my_phone.cost()
        '''
        ...

    def os(self) -> str:
        '''
        Метод возвращает ОС телефона

        :return: ОС телефона

        Пример:
        >>> my_phone = Phone('Apple', 'Iphone 15', 512)
        >>> my_phone_OS = my_phone.os()
        '''
        ...

    def count_cameras(self) -> int:
        '''
        Метод возвращает количество камер телефона

        :return: количество камер телефона

        Пример:
        >>> my_phone = Phone('Apple', 'Iphone 15', 512)
        >>> my_phone_cam = my_phone.count_cameras()
        '''
        ...

class Car:
    '''
    Класс описывает автомобили
    '''
    def __init__(self, brand: str, model: str, year: int):
        '''
        Инициализация экземпляров класса

        :param brand: Марка автомобиля
        :param model: Модель автомобиля
        :param year: Год выпуска

        Пример:
        >>> my_car = Car('BMW', 'X5', 2020)
        '''

        if not isinstance(brand, str):
            raise TypeError('Марка автомобиля должна быть типа str')
        self.brand = brand
        if not isinstance(model, str):
            raise TypeError('Модель автомобился должна быть типа str')
        self.model = model
        if not isinstance(year, int):
            raise TypeError('Год выпуска должен быть целым числом')
        if year < 1990:
            raise ValueError('Год выпуска должен быть не раньше 1990 года')
        self.year = year

    def cost(self) -> int:
        '''
        Метод рассчитывает стоимость автомобиля по его параметрам

        :return: Стоимость автомобился

        Пример:
        >>> my_car = Car('BMW', 'X5', 2020)
        >>> my_car_cost = my_car.cost()
        '''
        ...

    def hp(self) -> int:
        '''
        Метод возвращает количество лошадиных сил

        :return: количество лошадиных сил

        Пример:
        >>> my_car = Car('BMW', 'X5', 2020)
        >>> my_car_hp = my_car.hp()
        '''
        ...

    def mileage(self) -> int:
        '''
        Метод возвращает пробег авто в км

        :return: пробег авто в км

        Пример:
        >>> my_car = Car('BMW', 'X5', 2020)
        >>> my_car_hp = my_car.hp()
        '''
        ...



if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
