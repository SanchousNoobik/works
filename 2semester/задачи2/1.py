class Book:
    def __init__(self, name, avtor):
        self.avtor = avtor  
        self.name = name
        
book1 = Book("Преступление и наказание", "Достоевский")
book2 = Book("Война и мир", "Толстой")

print(book1.name +" - "+ book1.avtor)
print(book2.avtor)