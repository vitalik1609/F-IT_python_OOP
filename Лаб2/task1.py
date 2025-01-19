BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:

    def __init__(self, id, name, pages):
        """
        Инициализация экземпляров класса

        :param id: Идентификатор
        :param name: Название книги
        :param pages: Количество страниц
        """
        self.id = id
        self.name = name
        self.pages = pages

    def __str__(self):
        """
         Метод __str__ должен возвращать строку формата, где "название_книги"
         берется с помощью атрибута name

        :return: Строка с названием книги
        """
        return f'Книга "{self.name}"'

    def __repr__(self):
        """
        Метод __repr__ должен возвращать валидную python строку,
        по которой можно инициализировать точно такой же экземпляр.

        :return: Строка по которой можно инициализировать точно такой же экземпляр.
        """
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"






if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
