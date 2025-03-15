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



class Contract:
    pass