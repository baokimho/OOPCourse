class LibraryItem:
    def __init__(self, title, author, year, item_id):
        self.title = title
        self.author = author
        self.year = year
        self.item_id = item_id
        self.is_borrowed = False

    def display_info(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        print(f"ID: {self.item_id} | Title: {self.title} | Author: {self.author} | Year: {self.year} | Status: {status}")


class Book(LibraryItem):
    def __init__(self, title, author, year, item_id, genre):
        super().__init__(title, author, year, item_id)
        self.genre = genre

    def display_info(self):
        super().display_info()
        print(f"Genre: {self.genre}")


class Magazine(LibraryItem):
    def __init__(self, title, author, year, item_id, issue):
        super().__init__(title, author, year, item_id)
        self.issue = issue

    def display_info(self):
        super().display_info()
        print(f"Issue: {self.issue}")


class DVD(LibraryItem):
    def __init__(self, title, director, year, item_id, duration):
        super().__init__(title, director, year, item_id)
        self.duration = duration

    def display_info(self):
        super().display_info()
        print(f"Duration: {self.duration} minutes")


class LibraryCatalog:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.item_id] = item
        print(f"Added: {item.title}")

    def remove_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
            print(f"Item ID {item_id} removed.")
        else:
            print("Item not found.")

    def search_item(self, title):
        results = [item for item in self.items.values() if title.lower() in item.title.lower()]
        if results:
            for item in results:
                item.display_info()
        else:
            print("No matching items found.")

    def borrow_item(self, item_id):
        if item_id in self.items and not self.items[item_id].is_borrowed:
            self.items[item_id].is_borrowed = True
            print(f"Item ID {item_id} borrowed.")
        else:
            print("Item not available for borrowing.")

    def return_item(self, item_id):
        if item_id in self.items and self.items[item_id].is_borrowed:
            self.items[item_id].is_borrowed = False
            print(f"Item ID {item_id} returned.")
        else:
            print("Item was not borrowed.")


if __name__ == "__main__":
    catalog = LibraryCatalog()

    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, 101, "Fiction")
    magazine1 = Magazine("National Geographic", "Various", 2023, 102, "June Edition")
    dvd1 = DVD("Inception", "Christopher Nolan", 2010, 103, 148)

    catalog.add_item(book1)
    catalog.add_item(magazine1)
    catalog.add_item(dvd1)

    print("\nSearching for 'Great':")
    catalog.search_item("Great")

    print("\nBorrowing Item 101:")
    catalog.borrow_item(101)
    catalog.search_item("Great")

    print("\nReturning Item 101:")
    catalog.return_item(101)
    catalog.search_item("Great")
