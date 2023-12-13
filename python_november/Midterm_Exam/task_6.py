# Создаем класс Book с атрибутами название, автор, и год публикации
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_print(self):
        print(f"Название: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Год публикации примерно): {self.year}")

# Варианты для класса Book
book1 = Book("Капитан Блад", "Рафаэль Сабатини", 1806)
book2 = Book("Лайли ва Маджнун", "Джалолидин Руми", 904)
book3 = Book("Богатый папаб Бедный папа", "Роберт Кийосаки", 1991)

# Создаем список для хранения вариантов класса Book
books = [book1, book2, book3]

# Выводим информацию книгах
for book in books:
    book.display_print()
    print()
