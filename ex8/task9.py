# """
# Refactor the code, in the exercise sheet there is a list of possible problems that you can find from this program. 
# Some of the problems are overlapping, so you might fix two problems when you are fixing the code.

# Hint. start by utilizing inheritance and method overriding, then continue with other parts of the code.
# """
# class Item:
#     def __init__(
#             self,
#             title=None,
#             author=None,
#             artist=None,
#             director=None,
#             developer=None,
#             year=None
#             ):
#         # Initialize the item with various attributes
#         self.__title = title
#         self.__author = author
#         self.__artist = artist
#         self.__director = director
#         self.__developer = developer
#         self.__year = year

#     @property
#     def title(self):
#         # Return the title of the item
#         return self.__title

#     @property
#     def author(self):
#         # Return the author of the item (only for books)
#         return self.__author

#     @property
#     def artist(self):
#         # Return the artist of the item (only for music)
#         return self.__artist

#     @property
#     def director(self):
#         # Return the director of the item (only for movies)
#         return self.__director

#     @property
#     def developer(self):
#         # Return the developer of the item (only for computer games)
#         return self.__developer

#     @property
#     def year(self):
#         # Return the year of the item
#         return self.__year

#     def print_item_description(self):
#         # Print the description of the item
#         description = f"Title: {self.title}, Year: {self.year}"
#         if self.author:
#             description += f", Author: {self.author}"
#         if self.artist:
#             description += f", Artist: {self.artist}"
#         if self.director:
#             description += f", Director: {self.director}"
#         if self.developer:
#             description += f", Developer: {self.developer}"
#         return description
    
#     def update_info(self, title=None, author=None, artist=None, director=None, developer=None, year=None):
#         # Updates the information in the item
#         if title:
#             self.__title = title
#         if author:
#             self.__author = author
#         if artist:
#             self.__artist = artist
#         if director:
#             self.__director = director
#         if developer:
#             self.__developer = developer
#         if year:
#             self.__year = year

# class Box:
#     def __init__(self):
#         self.items = {}

#     def add_item(self, key, item: Item):
#         self.items[key] = item

#     def remove_item(self, key):
#         if key in self.items:
#             del self.items[key]
#         else:
#             print("No item found")

#     def replace_item(self, old_key, new_key, new_item):
#         if old_key in self.items:
#             del self.items[old_key]
#             self.items[new_key] = new_item
#         else:
#             print("No item found")

#     def get_descriptions(self):
#         return [item.print_item_description() for item in self.items.values()]
    
#     def update_item(self, key, title=None, author=None, artist=None, director=None, developer=None, year=None):
#         #Hint! check here how to use kwarks!
#         # for example: https://realpython.com/python-kwargs-and-args/
#         if key in self.items:
#             self.items[key].update_info(title, author, artist, director, developer, year)
#         else:
#             print("No item found")

# class PackItems:
#     def __init__(self):
#         self.box = Box()
#         self.log = []

#     def user_interface(self):
#         while True:
#             print("\nOptions:")
#             print("1. Add item")
#             print("2. Remove item")
#             print("3. Replace item")
#             print("4. View items")
#             print("5. Edit item")
#             print("6. Exit")
#             choice = input("Choose an option: ")

#             if choice == "1":
#                 title = input("Enter title: ")
#                 author = input("Enter author (or leave blank): ")
#                 artist = input("Enter artist (or leave blank): ")
#                 director = input("Enter director (or leave blank): ")
#                 developer = input("Enter developer (or leave blank): ")
#                 year = input("Enter year: ")
#                 item = Item(title, author, artist, director, developer, year)
#                 self.box.add_item(title, item)
#                 self.log.append(f"Added item: {title}")
#             elif choice == "2":
#                 title = input("Enter title of item to remove: ")
#                 self.box.remove_item(title)
#                 self.log.append(f"Removed item: {title}")
#             elif choice == "3":
#                 old_title = input("Enter title of item to replace: ")
#                 new_title = input("Enter new title: ")
#                 author = input("Enter author (or leave blank): ")
#                 artist = input("Enter artist (or leave blank): ")
#                 director = input("Enter director (or leave blank): ")
#                 developer = input("Enter developer (or leave blank): ")
#                 year = input("Enter year: ")
#                 new_item = Item(new_title, author, artist, director, developer, year)
#                 self.box.replace_item(old_title, new_title, new_item)
#                 self.log.append(f"Replaced item: {old_title} with {new_title}")
#             elif choice == "5":
#                 title = input("Enter title of item to edit: ")
#                 new_title = input("Enter new title (or leave blank): ")
#                 author = input("Enter new author (or leave blank): ")
#                 artist = input("Enter new artist (or leave blank): ")
#                 director = input("Enter new director (or leave blank): ")
#                 developer = input("Enter new developer (or leave blank): ")
#                 year = input("Enter new year (or leave blank): ")
#                 self.box.update_item(title, title=new_title, author=author, artist=artist, director=director, developer=developer, year=year)
#                 self.log.append(f"Edited item: {title}")
#             elif choice == "6":
#                 self.save_log()
#                 break
#             else:
#                 print("Invalid option. Please try again.")

#     def save_log(self):
#         with open("log.txt", "w") as file:
#             for entry in self.log:
#                 file.write(entry + "\n")

# # Example usage:
# """
# This is for testing the Item class
# if __name__ == "__main__":
#     item1 = Item(title="1984", author="George Orwell", year=1949)
# item2 = Item(title="Thriller", artist="Michael Jackson", year=1982)
# item3 = Item(title="Inception", director="Christopher Nolan", year=2010)
# item4 = Item(title="The Legend of Zelda", developer="Nintendo", year=1986)

# print(item1.print_item_description())
# print(item2.print_item_description())
# print(item3.print_item_description())
# print(item4.print_item_description())"""

# """
# This to for testing the Box class
# if __name__ == "__main__":
#     box = Box()
#     box.add_item("1984", Item(title="1984", author="George Orwell", year=1949))
#     box.add_item("Thriller", Item(title="Thriller", artist="Michael Jackson", year=1982))

#     print("Before replacement:")
#     for description in box.get_descriptions():
#         print(description)

#     box.replace_item("1984", "1984", Item(title="1984", author="George Orwell", year=1950))

#     print("\nAfter replacement:")
#     for description in box.get_descriptions():
#         print(description)"""

# if __name__ == "__main__":
#     pack_items = PackItems()
#     pack_items.user_interface()

from abc import ABC, abstractmethod

# Base Item class
class Item(ABC):
    def __init__(self, title, year):
        if not title:
            raise ValueError("Title cannot be empty")
        if not year.isdigit():
            raise ValueError("Year must be numeric")
        self.title = title
        self.year = int(year)

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def update_info(self, **kwargs):
        pass


class Book(Item):
    def __init__(self, title, year, author):
        super().__init__(title, year)
        if not author:
            raise ValueError("Author cannot be empty")
        self.author = author

    def get_description(self):
        return f"Book - Title: {self.title}, Year: {self.year}, Author: {self.author}"

    def update_info(self, **kwargs):
        self.title = kwargs.get("title", self.title)
        self.year = int(kwargs.get("year", self.year))
        self.author = kwargs.get("author", self.author)


class Music(Item):
    def __init__(self, title, year, artist):
        super().__init__(title, year)
        if not artist:
            raise ValueError("Artist cannot be empty")
        self.artist = artist

    def get_description(self):
        return f"Music - Title: {self.title}, Year: {self.year}, Artist: {self.artist}"

    def update_info(self, **kwargs):
        self.title = kwargs.get("title", self.title)
        self.year = int(kwargs.get("year", self.year))
        self.artist = kwargs.get("artist", self.artist)


class Movie(Item):
    def __init__(self, title, year, director):
        super().__init__(title, year)
        if not director:
            raise ValueError("Director cannot be empty")
        self.director = director

    def get_description(self):
        return f"Movie - Title: {self.title}, Year: {self.year}, Director: {self.director}"

    def update_info(self, **kwargs):
        self.title = kwargs.get("title", self.title)
        self.year = int(kwargs.get("year", self.year))
        self.director = kwargs.get("director", self.director)


class Game(Item):
    def __init__(self, title, year, developer):
        super().__init__(title, year)
        if not developer:
            raise ValueError("Developer cannot be empty")
        self.developer = developer

    def get_description(self):
        return f"Game - Title: {self.title}, Year: {self.year}, Developer: {self.developer}"

    def update_info(self, **kwargs):
        self.title = kwargs.get("title", self.title)
        self.year = int(kwargs.get("year", self.year))
        self.developer = kwargs.get("developer", self.developer)


class Box:
    def __init__(self):
        self.items = {}

    def add_item(self, key, item):
        self.items[key] = item

    def remove_item(self, key):
        return self.items.pop(key, None)

    def replace_item(self, old_key, new_key, new_item):
        self.remove_item(old_key)
        self.add_item(new_key, new_item)

    def update_item(self, key, **kwargs):
        item = self.items.get(key)
        if item:
            item.update_info(**kwargs)

    def get_descriptions(self):
        return [item.get_description() for item in self.items.values()]


class PackItems:
    def __init__(self):
        self.box = Box()
        self.log = []

    def user_interface(self):
        while True:
            print("\nOptions:")
            print("1. Add item")
            print("2. Remove item")
            print("3. Replace item")
            print("4. View items")
            print("5. Edit item")
            print("6. Exit")

            choice = input("Choose an option: ")
            if choice == "1":
                self.add_item_ui()
            elif choice == "2":
                self.remove_item_ui()
            elif choice == "3":
                self.replace_item_ui()
            elif choice == "4":
                self.view_items_ui()
            elif choice == "5":
                self.edit_item_ui()
            elif choice == "6":
                self.save_log()
                print("Exiting. Log saved.")
                break
            else:
                print("Invalid option. Please try again.")

    def prompt_item_data(self, item_type):
        title = input("Enter title: ")
        year = input("Enter year: ")
        creator = input(f"Enter {item_type} creator (e.g. author, artist, etc.): ")
        return title, year, creator

    def add_item_ui(self):
        item_type = input("Enter item type (book/music/movie/game): ").lower()
        try:
            title, year, creator = self.prompt_item_data(item_type)
            item = self.create_item(item_type, title, year, creator)
            self.box.add_item(title, item)
            self.log.append(f"Added {item_type}: {title}")
            print("Item added successfully.")
        except Exception as e:
            print(f"Error: {e}")

    def remove_item_ui(self):
        key = input("Enter title of item to remove: ")
        if self.box.remove_item(key):
            self.log.append(f"Removed item: {key}")
            print("Item removed.")
        else:
            print("No item found with that title.")

    def replace_item_ui(self):
        old_key = input("Enter old item title: ")
        item_type = input("Enter new item type (book/music/movie/game): ").lower()
        try:
            new_title, year, creator = self.prompt_item_data(item_type)
            new_item = self.create_item(item_type, new_title, year, creator)
            self.box.replace_item(old_key, new_title, new_item)
            self.log.append(f"Replaced item: {old_key} with {new_title}")
            print("Item replaced.")
        except Exception as e:
            print(f"Error: {e}")

    def view_items_ui(self):
        descriptions = self.box.get_descriptions()
        if not descriptions:
            print("No items in the box.")
        else:
            print("\nCurrent items:")
            for desc in descriptions:
                print(desc)

    def edit_item_ui(self):
        key = input("Enter title of item to edit: ")
        item = self.box.items.get(key)
        if not item:
            print("Item not found.")
            return

        print("Leave fields empty to keep current value.")
        title = input("Enter new title: ") or None
        year = input("Enter new year: ") or None

        if isinstance(item, Book):
            creator = input("Enter new author: ") or None
            self.box.update_item(key, title=title, year=year, author=creator)
        elif isinstance(item, Music):
            creator = input("Enter new artist: ") or None
            self.box.update_item(key, title=title, year=year, artist=creator)
        elif isinstance(item, Movie):
            creator = input("Enter new director: ") or None
            self.box.update_item(key, title=title, year=year, director=creator)
        elif isinstance(item, Game):
            creator = input("Enter new developer: ") or None
            self.box.update_item(key, title=title, year=year, developer=creator)

        self.log.append(f"Edited item: {key}")
        print("Item updated.")

    def create_item(self, item_type, title, year, creator):
        item_type = item_type.lower()
        if item_type == "book":
            return Book(title, year, creator)
        elif item_type == "music":
            return Music(title, year, creator)
        elif item_type == "movie":
            return Movie(title, year, creator)
        elif item_type == "game":
            return Game(title, year, creator)
        else:
            raise ValueError("Invalid item type")

    def save_log(self):
        with open("log.txt", "w") as f:
            for entry in self.log:
                f.write(entry + "\n")


if __name__ == "__main__":
    PackItems().user_interface()
