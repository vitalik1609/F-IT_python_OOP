if __name__ == "__main__":
    class Laptop:
        """
        Базовый класс для ноутбуков.

        Attributes:
            brand (str): Производитель ноутбука.
            model (str): Модель ноутбука.
            processor (str): Тип процессора.
            memory (int): Объем оперативной памяти (в ГБ).
            price (float): Цена ноутбука.
        """

        def __init__(self, brand: str, model: str, processor: str, memory: int, price: float) -> None:
            """
            Инициализирует экземпляр класса Laptop.

            Args:
                brand (str): Производитель ноутбука.
                model (str): Модель ноутбука.
                processor (str): Тип процессора.
                memory (int): Объем оперативной памяти в ГБ.
                price (float): Цена ноутбука.
            """
            self.brand: str = brand
            self.model: str = model
            self.processor: str = processor
            self.memory: int = memory
            self.price: float = price

        def __str__(self) -> str:
            """
            Возвращает строковое представление объекта для пользователя.

            Returns:
                str: Читаемая информация о ноутбуке.
            """
            return f"{self.brand} {self.model} - {self.processor}, {self.memory}GB, ${self.price}"

        def __repr__(self) -> str:
            """
            Возвращает строковое представление объекта для разработчика.

            Returns:
                str: Точное представление объекта.
            """
            return (f"Laptop(brand={self.brand!r}, model={self.model!r}, "
                    f"processor={self.processor!r}, memory={self.memory!r}, price={self.price!r})")

        def calculate_discount(self, discount: float) -> float:
            """
            Вычисляет цену после применения скидки.

            Args:
                discount (float): Процент скидки (например, 10.0 означает 10%).

            Returns:
                float: Цена после применения скидки.
            """
            return self.price * (1 - discount / 100)


    class AppleLaptop(Laptop):
        """
        Класс для ноутбуков Apple, наследуемый от базового класса Laptop.

        Дополнительные атрибуты:
            release_year (int): Год выпуска ноутбука.
            has_touch_bar (bool): Наличие Touch Bar.
        """

        def __init__(self, model: str, processor: str, memory: int, price: float,
                     release_year: int, has_touch_bar: bool) -> None:
            """
            Инициализирует экземпляр AppleLaptop.

            Args:
                model (str): Модель ноутбука.
                processor (str): Тип процессора.
                memory (int): Объем оперативной памяти в ГБ.
                price (float): Цена ноутбука.
                release_year (int): Год выпуска ноутбука.
                has_touch_bar (bool): True, если ноутбук оснащен Touch Bar, иначе False.
            """
            # Для всех ноутбуков Apple бренд фиксирован
            super().__init__("Apple", model, processor, memory, price)
            self.release_year: int = release_year
            self.has_touch_bar: bool = has_touch_bar

        def __str__(self) -> str:
            """
            Возвращает строковое представление объекта AppleLaptop для пользователя.

            Returns:
                str: Читаемая информация о ноутбуке Apple.
            """
            touch_bar_str: str = "с Touch Bar" if self.has_touch_bar else "без Touch Bar"
            return (f"{self.brand} {self.model} ({self.release_year}) - {self.processor}, "
                    f"{self.memory}GB, {touch_bar_str}, ${self.price}")

        def __repr__(self) -> str:
            """
            Возвращает строковое представление объекта AppleLaptop для разработчика.

            Returns:
                str: Точное представление объекта.
            """
            return (f"AppleLaptop(model={self.model!r}, processor={self.processor!r}, "
                    f"memory={self.memory!r}, price={self.price!r}, "
                    f"release_year={self.release_year!r}, has_touch_bar={self.has_touch_bar!r})")

        def calculate_discount(self, discount: float) -> float:
            """
            Перегруженный метод вычисления цены после скидки для ноутбуков Apple.

            Обоснование перегрузки:
            В случае с ноутбуками Apple часто применяется ограничение на максимальную величину скидки
            (например, не более 15%), чтобы защитить имидж бренда и поддерживать ценовую политику.
            Поэтому, если переданный процент скидки превышает 15%, применяется максимум 15%.

            Args:
                discount (float): Процент скидки.

            Returns:
                float: Цена после применения ограниченной скидки.
            """
            max_discount: float = 15.0
            applied_discount: float = discount if discount <= max_discount else max_discount
            return self.price * (1 - applied_discount / 100)


    class LenovoLaptop(Laptop):
        """
        Класс для ноутбуков Lenovo, наследуемый от базового класса Laptop.

        Дополнительные атрибуты:
            series (str): Серия ноутбука (например, "IdeaPad", "Legion" и т.д.).
        """

        def __init__(self, model: str, processor: str, memory: int, price: float, series: str) -> None:
            """
            Инициализирует экземпляр LenovoLaptop.

            Args:
                model (str): Модель ноутбука.
                processor (str): Тип процессора.
                memory (int): Объем оперативной памяти в ГБ.
                price (float): Цена ноутбука.
                series (str): Серия ноутбука.
            """
            # Для всех ноутбуков Lenovo бренд фиксирован
            super().__init__("Lenovo", model, processor, memory, price)
            self.series: str = series

        def __str__(self) -> str:
            """
            Возвращает строковое представление объекта LenovoLaptop для пользователя.

            Returns:
                str: Читаемая информация о ноутбуке Lenovo.
            """
            return f"{self.brand} {self.series} {self.model} - {self.processor}, {self.memory}GB, ${self.price}"

        def __repr__(self) -> str:
            """
            Возвращает строковое представление объекта LenovoLaptop для разработчика.

            Returns:
                str: Точное представление объекта.
            """
            return (f"LenovoLaptop(model={self.model!r}, processor={self.processor!r}, "
                    f"memory={self.memory!r}, price={self.price!r}, series={self.series!r})")
    pass
