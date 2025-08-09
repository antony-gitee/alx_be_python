# book_class.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        print(f"Book '{self.title}' by {self.author} has been created.")

    def __del__(self):
        print(f"Book '{self.title}' is being deleted.")

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"

          



    