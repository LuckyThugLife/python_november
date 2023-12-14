class Item:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def display_details(self):
        print(f" Title: {self.title} Author: {self.author}, Publication Year: {self.publication_year}.")

class Book(Item):
    def __init__(self, title, author, publication_year, isbn):
        super().__init__(title, author, publication_year)
        self.isbn = isbn

    def display_details(self):
        super().display_details()
        print(f"ISBN: {self.isbn}.")

class Journal(Item):
    def __init__(self, title, author, publication_year, issn):
        super(). __init__(title, author, publication_year)
        self.issn = issn
    def display_details(self):
        super().display_details()
        print(f"ISSN {self.issn}.")


class Library:
    def __init__(self):
        self.catalog = []

    def addItem(self, Item):
        self.catalog.append(Item)

    def display_catalog(self):
        for Item in self.catalog:
            Item.display_details()

Library = Library()
book = Book("Captain Blud", "Rafael Sabatini", 1888, "9087345890-9")
journal = Journal("AsiaPlus", "Nature Publishing Group", 2022, "08457609380-89")
Library.addItem(book)
Library.addItem(journal)
Library.display_catalog()



