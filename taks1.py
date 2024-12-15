import doctest
# TODO Написать 3 класса с документацией и аннотацией типов
class Human:
    def __init__(self, age: int, children: int):
        """
              Создание и подготовка к работе объекта "Человек"

              :param age: Количество лет
              :param children: Количество детей

              Примеры:
              >>> human = Human(12, 0)  # инициализация экземпляра класса
              """
        if not isinstance(age, int):
            raise TypeError("Количество лет должно быть int")
        if age < 0:
            raise ValueError("Количество лет должно быть неотрицательным")
        self.age = age

        if not isinstance(children, int):
            raise TypeError("Количество детей у человека должно быть int")
        if children < 0:
            raise ValueError("Количество детей должно быть неотрицательным")
        self.children = children  # количество детей

    def is_human_an_adult(self) -> bool:
        """
        Функция которая проверяет является ли человек совершеннолетним

        :return: Является ли человек совершеннолетним

        Примеры:
        >>> human = Human(25, 1)
        >>> human.is_human_an_adult()
        """
        ...

    def is_human_many_children(self) -> bool:
        """
        Функция которая проверяет является ли человек многодетным

        :return: Является ли человек многодетным

        Примеры:
        >>> human = Human(32, 3)
        >>> human.is_human_many_children()
        """
        ...

class Exams:
    def __init__(self, subject: str, mark: int, people: int):
        """
        Создание и подготовка к работе объекта "Экзамены"

        :param subject: Предмет, по которому экзамен
        :param mark: Полученная оценка
        :param people: Количестрво человек, сдавших экзамен

        Примеры:
        >>> exam = Exams("Math", 5, 7)  # инициализация экземпляра класса
        """
        self.subject = subject
        if not isinstance(mark, int):
            raise TypeError("Оценка должна быть типа int")
        if mark < 0:
            raise ValueError("Оценка должна быть положительным числом")
        self.mark = mark

        if not isinstance(people, int):
            raise TypeError("Количество сдавших человек должно быть типа int")
        if people < 0:
            raise ValueError("Количество сдавших человек должно быть положительным числом")
        self.people = people

    def is_exam_pass(self) -> bool:
        """
        Функция которая проверяет сдал ли человек экзамен

        :return: Сдал ли человек экзамен

        Примеры:
        >>> exam = Exams("Math", 4, 8)
        >>> exam.is_exam_pass()
        """
        ...

    def add_pass_people(self, person: int) -> None:
        """
        Добавление людей ко сдавшим экзамен.
        :param person: Количество сдавших людей, которых надо добавить
        :raise ValueError: Если количество людей меньше 0

        Примеры:
        >>> exam = Exams("Math", 4, 9)
        >>> exam.add_pass_people(2)
        """
        if not isinstance(person, int):
            raise TypeError("Количество людей должно быть типа int")
        if person < 0:
            raise ValueError("Количество людей должно положительным числом")
        ...

class Book:
    def __init__(self, pages: int, read_pages: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param pages: Количество страниц
        :param read_pages: Количество прочитанных страниц

        Примеры:
        >>> book = Book(500, 200)  # инициализация экземпляра класса
        """
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages

        if not isinstance(read_pages, int):
            raise TypeError("Количество прочитанных страниц должно быть int")
        if read_pages < 0:
            raise ValueError("Количество прочитанных страниц не может быть отрицательным числом")
        self.read_pages = read_pages

    def is_start_read(self) -> bool:
        """
        Функция которая проверяет начали ли читать книгу

        :return: Начали ли читать книгу

        Примеры:
        >>> book = Book(500, 0)
        >>> book.is_start_read()
        """
        ...

    def add_read_pages(self, page: int) -> None:
        """
        Добавление страниц к прочитанным.
        :param page: Прочитанные страницы

        :raise ValueError: Если количество прочитанных страниц превышает общее количество страниц, то вызываем ошибку

        Примеры:
        >>> book = Book(500, 0)
        >>> book.add_read_pages(200)
        """
        if not isinstance(page, (int, float)):
            raise TypeError("Количество прочитанных страниц должно быть типа int")
        if page < 0:
            raise ValueError("Количество страниц должно положительным числом")
        ...




if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()  # тестирование примеров, которые находятся в документации
