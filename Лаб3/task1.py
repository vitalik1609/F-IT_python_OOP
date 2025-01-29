class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__()
        if not isinstance(pages, int):
            raise TypeError('Неправильный тип данных, должно быть число (int)')
        else:
            self.pages = pages

    def __str__(self):
        return f"Бумажная книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages!r})"



class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__()
        if not isinstance(duration, float):
            raise TypeError('Неправильный тип данных, должно быть число (float)')
        else:
            self.duration = duration


    def __str__(self):
        return f"Аудиокнига {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration!r})"


