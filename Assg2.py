class EBookStore:
    '''This class represents the e-book store.'''

    def __init__(self, name, address):
        self.__name = name
        self.__address = address
        self.__catalog = Catalog()

    # Getter and Setter for name
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # Getter and Setter for address
    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def register_customer(self, customer):
        pass  # Registers a new customer to the store

    def process_order(self, order):
        pass  # Processes an order for e-books

    def __str__(self):
        return "EBookStore(Name: " + self.__name + ", Address: " + self.__address + ")"


class Catalog:
    '''This class maintains a catalog of available e-books.'''

    def __init__(self):
        self.__ebooks = []

    def add_ebook(self, ebook):
        # Adds an e-book to the catalog
        self.__ebooks.append(ebook)

    def remove_ebook(self, ebook):
        # Removes an e-book from the catalog
        if ebook in self.__ebooks:
            self.__ebooks.remove(ebook)

    def search_ebook(self, title):
        # Searches for an e-book by title
        for ebook in self.__ebooks:
            if ebook.get_title() == title:
                return ebook
        return None

    def get_ebooks(self):
        return self.__ebooks

    def __str__(self):
        return "Catalog(EBooks: " + str([ebook.get_title() for ebook in self.__ebooks]) + ")"


class Customer:
    '''This class represents a customer in the store.'''

    def __init__(self, name, contact_info):
        self.__name = name
        self.__contact_info = contact_info
        self.__shopping_cart = ShoppingCart()

    # Getter and Setter for name
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # Getter and Setter for contact_info
    def get_contact_info(self):
        return self.__contact_info

    def set_contact_info(self, contact_info):
        self.__contact_info = contact_info

    def get_shopping_cart(self):
        return self.__shopping_cart

    def browse_catalog(self, catalog):
        pass  # Browses through the catalog

    def view_cart(self):
        # Displays the items in the shopping cart
        return str(self.__shopping_cart)

    def purchase(self):
        # Completes the purchase of items in the cart
        order = Order()
        for item in self.__shopping_cart.get_items():
            order.add_item(item)

    def __str__(self):
        return "Customer(Name: " + self.__name + ", Contact Info: " + self.__contact_info + ")"


class ShoppingCart:
    '''This class represents a shopping cart for a customer.'''

    def __init__(self):
        self.__items = []

    def add_item(self, ebook):
        # Adds an e-book to the shopping cart
        self.__items.append(ebook)

    def remove_item(self, ebook):
        # Removes an e-book from the shopping cart
        if ebook in self.__items:
            self.__items.remove(ebook)

    def update_quantity(self, ebook, qty):
        pass  # Updates the quantity of a particular e-book

    def get_items(self):
        return self.__items

    def __str__(self):
        return "ShoppingCart(Items: " + str([item.get_title() for item in self.__items]) + ")"


class EBook:
    '''This class represents an e-book in the store.'''

    def __init__(self, title, author, price, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__price = price
        self.__genre = genre
        self.__publication_date = publication_date

    # Getters and Setters for attributes
    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_genre(self):
        return self.__genre

    def get_publication_date(self):
        return self.__publication_date

    def apply_discount(self, discount):
        # Applies a discount to the e-book's price
        self.__price *= (1 - discount)

    def __str__(self):
        return ("EBook(Title: " + self.__title + ", Author: " + self.__author +
                ", Price: " + str(self.__price) + ", Genre: " + self.__genre +
                ", Published: " + str(self.__publication_date) + ")")


class Order:
    '''This class represents an order containing e-books.'''

    def __init__(self):
        self.__items = []
        self.__total_amount = 0

    def add_item(self, ebook):
        # Adds an e-book to the order
        self.__items.append(ebook)

    def calculate_total(self):
        # Calculate and return the total amount of all e-books in the order
        self.__total_amount = sum(item.get_price() for item in self.__items)
        return self.__total_amount

    def generate_invoice(self):
        pass  # Generates an invoice for the order

    def __str__(self):
        return "Order(Items: " + str([item.get_title() for item in self.__items]) + ")"


class Invoice:
    '''This class represents an invoice for an order.'''

    def __init__(self, total_amount):
        self.__total_amount = total_amount

    def generate_invoice_details(self):
        # Generates details for the invoice
        pass

    def __str__(self):
        return "Invoice(Total Amount: " + str(self.__total_amount) + ")"


class Discount:
    '''This class represents available discounts for orders.'''

    def __init__(self, loyalty_discount, student_discount):
        self.__loyalty_discount = loyalty_discount
        self.__student_discount = student_discount

    def apply_loyalty_discount(self, price):
        # Applies loyalty discount to the price
        return price * (1 - self.__loyalty_discount)

    def apply_student_discount(self, is_student, price):
        # Applies student discount to the price if the customer is a student
        if is_student:
            return price * (1 - self.__student_discount)
        return price

    def __str__(self):
        return "Discount(Loyalty: " + str(self.__loyalty_discount * 100) + "%, Student: " + str(
            self.__student_discount * 100) + "%)"