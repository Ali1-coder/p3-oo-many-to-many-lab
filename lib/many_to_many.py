class Author:
    pass


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