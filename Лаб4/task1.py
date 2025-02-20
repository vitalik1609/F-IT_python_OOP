class Laptop:
    """
    Базовый класс для ноутбуков.
    """

    def __init__(self, brand: str, model: str, processor: str, memory: int, price: float) -> None:
        self.brand = brand
        self.model = model
        self.processor = processor
        self.memory = memory
        self.price = price

    def __str__(self) -> str:
        return f"{self.brand} {self.model} - {self.processor}, {self.memory}GB"

    def __repr__(self) -> str:
        return (f"Laptop(brand={self.brand!r}, model={self.model!r}, "
                f"processor={self.processor!r}, memory={self.memory!r}, price={self.price!r})")

    def calculate_discount(self, discount: float) -> float:
        return self.price * (1 - discount / 100)

    def get_specs(self) -> str:
        return f"{self.brand} {self.model} - {self.processor}, {self.memory}GB"


class AppleLaptop(Laptop):
    """
    Класс для ноутбуков Apple.
    """

    def __init__(self, model: str, processor: str, memory: int, price: float,
                 release_year: int, has_touch_bar: bool) -> None:
        super().__init__("Apple", model, processor, memory, price)
        self.release_year = release_year
        self.has_touch_bar = has_touch_bar

    def __str__(self) -> str:
        return f"{self.brand} {self.model} ({self.release_year}) - {self.processor}, {self.memory}GB"

    def calculate_discount(self, discount: float) -> float:
        max_discount = 15.0
        applied_discount = min(discount, max_discount)
        return self.price * (1 - applied_discount / 100)


class LenovoLaptop(Laptop):
    """
    Класс для ноутбуков Lenovo.
    """

    def __init__(self, model: str, processor: str, memory: int, price: float, series: str) -> None:
        super().__init__("Lenovo", model, processor, memory, price)
        self.series = series

    def __str__(self) -> str:
        return f"{self.brand} {self.series} {self.model} - {self.processor}, {self.memory}GB"

    def calculate_discount(self, discount: float) -> float:
        max_discount = 25.0
        applied_discount = min(discount, max_discount)
        return self.price * (1 - applied_discount / 100)


if __name__ == "__main__":
    macbook = AppleLaptop("MacBook Pro", "M1", 16, 2000.0, 2023, True)
    print(macbook)
    print(macbook.calculate_discount(20))  # Применится скидка 15%, а не 20%
    
    lenovo = LenovoLaptop("Legion 5", "Ryzen 7", 32, 1500.0, "Gaming")
    print(lenovo)
    print(lenovo.calculate_discount(30))  # Применится скидка 25%, а не 30%
