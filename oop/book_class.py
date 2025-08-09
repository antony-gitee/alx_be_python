class Book:
    def __init__(self, title, author, year):
      """Constructor: Initializes the Book attributes"""
      self.title = title
      self.author = author
      self.year = year


    def __del__ (self):
       """Destructor: Called when the object is deleted"""
       print(f"Deleting {self.title}")


    def __str__(self):
       """User-friendly representation"""
       return f"{self.title} by {self.author}, published in {self.year}"
    

    
    def __repr__(self):
        """Official representation - can be used to recreate the object"""
        return f"Book('{self.title}', '{self.author}', {self.year})"
    
          



    