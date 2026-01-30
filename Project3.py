
"""
Design a console based library management system a Liabrary item is the base(abstract) idea book and
 magazine are different type of items borrowing rules behave diff for each of them a
 liabraryApp controles items (HAS-A) use oops concepts and return value, not only print


get_item_id() → returns unique id

get_title() → returns title

is_available() → returns True / False

borrow(user_id) → abstract → returns success / failure message

return_item() → abstract → returns status

calculate_fine(days_late) → abstract → returns fine amount

"""

class LibraryItem():
    def __init__(self, item_id, title):
        self.item_id = item_id
        self.title = title


    def borrow(self, days):                 # Abstract
        pass


class Book(LibraryItem):              # Inheritance
    def borrow(self, days):
        if days <= 14:
            return "Book Borrowed "
        else:
            return "Books can be borrowed for max 14 days"

class Magazine(LibraryItem):          # Inheritance
    def borrow(self, days):
        if days <= 7:
            return "Magazine Borrowed Successfully"
        else:
            return "Magazines can be borrowed for max 7 days"


class LibraryApp:                     # has a Relationship  ---------->>Composition
    def __init__(self):
        self.item = None

    def add_item(self, item_type):
        if item_type == "book":
            self.item = Book(101, "Python OOPS")
        else:
            self.item = Magazine(201, "Tech Monthly")
        return "Item Added Successfully"

    def borrow_item(self, days):
        return self.item.borrow(days) # Polymorphism


app = LibraryApp()
print(app.add_item("book"))
print(app.borrow_item(10))

print(app.add_item("magazine"))
print(app.borrow_item(10))
