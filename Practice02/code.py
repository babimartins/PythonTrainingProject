class Author:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date
    def __str__(self):
        return self.name + " born in " + self.birth_date
    @property
    def name(self):
        return "{last_name} {first_letter_name}.".format(last_name=self.last_name.upper(), first_letter_name=self.first_name[0].upper())
    @name.setter
    def name(self, value):
        arr_names = value.split(" ")
        self.first_name = arr_names[0] 
        if len(arr_names)>0:
            self.last_name = " ".join(arr_names[1:])

class Book:
    def __init__(self, title, year, authors_list=[]):
        self.title = title
        self.year = year
        self.authors_list = authors_list
    def __repr__(self):
        return self.title + " - " + str(self.authors_list)
    @property
    def authors(self):
        return self.authors_list
    @property
    def titles(self):
        return self.title
    @titles.setter
    def titles(self, name):
        if(name == "" or name == None):
            raise ValueError("You need to insert a title to the book")
        else:
            self.title = name

class Library:
    def __init__(self, books_list):
        self.books_list = books_list
    def __repr__(self):
        return str(self.books_list)
    @property
    def books_per_author(self):
        books_per_author = {}
        for book in self.books_list:
            for author in book.authors_list:
                if author not in books_per_author:
                    books_per_author[author] = [book.title]
                else:
                    books_per_author[author].append(book.title)
        return books_per_author

if __name__ == "__main__":
    pedro = Author("Pedro", "13/01/2001")
    pedro.name = "Pedro Paulo"
    print(pedro.name)
    fmf = Book("Fazendo meu filme", 2008, ["Paula Pimenta"])
    lotr = Book("Lord of the rings", 1954, ["J. r. R. Tolkien", "Alan Lee"])
    mvfs = Book("Minha vida fora de serie", 2008, ["Paula Pimenta"])
    print(str(lotr.authors_list))
    library = Library([fmf, lotr, mvfs])
    print(str(library.books_per_author))    