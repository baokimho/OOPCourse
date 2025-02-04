class Book:
    def __init__(self,name:str,author:str,genre:str,year:int):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year

python = Book("Fluent Python","Luciano Ramalho","Programming",2015 )
everest = Book("Into Thin Air","Jon Krakauer","Adventure",1997)
print(f"{python.author}: {python.name} ({python.year})")
print(f"the genre of the book {everest.name} is {everest.genre}")
