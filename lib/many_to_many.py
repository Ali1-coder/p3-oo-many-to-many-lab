class Author:
    all = []
    
    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise Exception("Name must be a non-empty string")
        self.name = name
        Author.all.append(self)

    def __repr__(self):
        return f"Author('{self.name}')"

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return list(set(contract.book for contract in self.contracts()))

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())



class Book:
    all = []
    
    def __init__(self, title):
        if not isinstance(title, str) or not title.strip():
            raise Exception("Title must be a non-empty string")
        self.title = title
        Book.all.append(self)

    def __repr__(self):
        return f"Book('{self.title}')"
    
    def contracts(self):
        """Returns a list of contracts associated with this book."""
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        """Returns a list of authors who have contracts for this book."""
        return list(set(contract.author for contract in self.contracts()))


class Contract:
    all = []
    
    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author class")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book class")
        if not isinstance(date, str) or not date.strip():
            raise Exception("Date must be a non-empty string")
        if not isinstance(royalties, int) or royalties < 0:
            raise Exception("Royalties must be a non-negative integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    def __repr__(self):
        return f"Contract({self.author.name}, {self.book.title}, {self.date}, {self.royalties}%)"

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]