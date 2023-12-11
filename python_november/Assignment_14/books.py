class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"{self.title} by {self.author}, published in {self.year}."


book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book2 = Book("1984", "George Orwell", 1949)

print("Title:", book1.title)
print("Author:", book1.author)
print("Year:", book1.year)
print("----------------------------")
print("Title:", book2.title)
print("Author:", book2.author)
print("Year:", book2.year)
