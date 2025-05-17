class Book:
    def __init__(self, title, author, genre, price):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price

    def get_price(self):
        return self.price

class EBook(Book):
    def __init__(self, title, author, genre, price, file_size):
        super().__init__(title, author, genre, price)
        self.file_size = file_size

class PrintedBook(Book):
    def __init__(self, title, author, genre, price, pages):
        super().__init__(title, author, genre, price)
        self.pages = pages

class Bookstore:
    def __init__(self):
        self.books = []
        self.orders = []

    def add_book(self, book):
        self.books.append(book)

    def place_order(self, customer_name, book_titles):
        total = sum(book.get_price() for book in self.books if book.title in book_titles)
        self.orders.append((customer_name, book_titles, total))
        print(f"Order placed by {customer_name}. Total: Rs.{total}")


store = Bookstore()
store.add_book(EBook("Python Basics", "pranjal patil", "Programming", 500, "5MB"))
store.add_book(PrintedBook("Data Science", "pranjal patil", "Technology", 800, 350))
store.place_order("isha", ["Python Basics", "Data Science"])
