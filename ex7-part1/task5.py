class LibraryItem:
    def __init__(self, itemID, title, author, publicationYear, publisher, isbn, available=True):
        self.itemID = itemID
        self.title = title
        self.author = author
        self.publicationYear = publicationYear
        self.publisher = publisher
        self.isbn = isbn
        self.available = available

class Book(LibraryItem):
    def __init__(self, itemID, title, author, publicationYear, publisher, isbn, genre, edition, numberOfPages, available=True):
        super().__init__(itemID, title, author, publicationYear, publisher, isbn, available)
        self.genre = genre
        self.edition = edition
        self.numberOfPages = numberOfPages

class Periodical(LibraryItem):
    def __init__(self, itemID, title, author, publicationYear, publisher, isbn, issueNumber, volumeNumber, issueDate, available=True):
        super().__init__(itemID, title, author, publicationYear, publisher, isbn, available)
        self.issueNumber = issueNumber
        self.volumeNumber = volumeNumber
        self.issueDate = issueDate

class DVD(LibraryItem):
    def __init__(self, itemID, title, author, publicationYear, publisher, isbn, director, actors, runningTime, rating, available=True):
        super().__init__(itemID, title, author, publicationYear, publisher, isbn, available)
        self.director = director
        self.actors = actors
        self.runningTime = runningTime
        self.rating = rating

class AudioCD(LibraryItem):
    def __init__(self, itemID, title, author, publicationYear, publisher, isbn, artist, numberOfTracks, available=True):
        super().__init__(itemID, title, author, publicationYear, publisher, isbn, available)
        self.artist = artist
        self.numberOfTracks = numberOfTracks

class EBook(LibraryItem):
    def __init__(self, itemID, title, author, publicationYear, publisher, isbn, fileFormat, downloadLink, available=True):
        super().__init__(itemID, title, author, publicationYear, publisher, isbn, available)
        self.fileFormat = fileFormat
        self.downloadLink = downloadLink

class Magazine(Periodical):
    def __init__(self, itemID, title, author, publicationYear, publisher, isbn, issueNumber, volumeNumber, issueDate, available=True):
        super().__init__(itemID, title, author, publicationYear, publisher, isbn, issueNumber, volumeNumber, issueDate, available)

class Journal(Periodical):
    def __init__(self, itemID, title, author, publicationYear, publisher, isbn, issueNumber, volumeNumber, issueDate, available=True):
        super().__init__(itemID, title, author, publicationYear, publisher, isbn, issueNumber, volumeNumber, issueDate, available)

class Newspaper(Periodical):
    def __init__(self, itemID, title, author, publicationYear, publisher, isbn, issueNumber, volumeNumber, issueDate, available=True):
        super().__init__(itemID, title, author, publicationYear, publisher, isbn, issueNumber, volumeNumber, issueDate, available)